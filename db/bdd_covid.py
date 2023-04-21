import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, insert, delete, ForeignKey, Date, Float
import time

# Créations des dataframes pour chaque table à partir des csv
def creation_dataframe_states():
    df = pd.read_csv('us-states.csv')
    df_states = df.drop(['date','deaths','cases'], axis =1)
    df_states = df_states.drop_duplicates()
    df_states = df_states.sort_values(by = 'state', ascending = True)
    df_states = df_states.rename(columns={"state": "name"})
    df_states = df_states.reset_index()
    df_states = df_states.drop('index', axis=1)
    df_states = df_states.reset_index()
    df_states = df_states.rename(columns={"index": "id"})
    return df_states

def creation_dataframe_counties():
    df = pd.read_csv('us-counties-2020.csv')
    df_counties = df.drop(['date','deaths','cases'], axis =1)
    df_counties = df_counties.drop_duplicates()
    df_counties = df_counties.sort_values(by = 'county', ascending = True)
    df_counties = df_counties.rename(columns={"county": "name"})
    df_counties = df_counties.iloc[:, [0,2,1]]
    df_counties = df_counties.reset_index()
    df_counties = df_counties.drop('index', axis=1)
    df_counties = df_counties.reset_index()
    df_counties = df_counties.rename(columns={"index": "id"})
    df_states = creation_dataframe_states()
    df_merged = pd.merge(df_counties, df_states, left_on='state', right_on='name', how='left')
    df_merged = df_merged.drop(['name_y','fips_y','state'], axis =1)
    df_counties = df_merged.rename(columns={"id_x": "id","name_x":"name","fips_x":"fips","id_y":"id_state"})
    return df_counties 

def creation_dataframe_counts(counts_csv):
    df = pd.read_csv(counts_csv)
    df_counts = df.drop('fips', axis =1)
    df_counts = df_counts.iloc[:, [0,3,4,2,1]]
    df_counts = df_counts.reset_index()
    df_counts = df_counts.rename(columns={"index": "id"})
    df_states = creation_dataframe_states()
    df_merged = pd.merge(df_counts, df_states, left_on='state', right_on='name', how='left')
    df_merged = df_merged.drop(['state','name','fips'], axis =1)
    df_counts = df_merged.rename(columns={"id_x": "id","id_y":"id_state"})
    df_counts = df_counts.iloc[:, [0,1,2,3,5,4]]
    df_counties = creation_dataframe_counties()
    df_merged2 = pd.merge(df_counts, df_counties, left_on=['county','id_state'], right_on=['name','id_state'], how='left')
    df_merged2 = df_merged2.drop(['county','name','fips'], axis =1)
    df_counts = df_merged2.rename(columns={"id_x": "id","id_state_x":"id_state","id_y":"id_county"})
    df_counts = df_counts.dropna(subset=["id_county"])
    df_counts = df_counts.drop('id',axis=1)
    return df_counts

def creation_dataframe_mask_use():
    df = pd.read_csv('mask-use-by-county.csv')
    df_mask_use = df.reset_index()
    df_mask_use = df_mask_use.rename(columns={"index": "id"})
    df_counties = creation_dataframe_counties()
    df_merged = pd.merge(df_mask_use, df_counties, left_on='COUNTYFP', right_on='fips', how='left')
    df_merged = df_merged.drop(['COUNTYFP','name','fips','id_state'], axis =1)
    df_mask_use = df_merged.rename(columns={"id_x": "id","NEVER":"never","RARELY":"rarely","SOMETIMES":"sometimes","FREQUENTLY":"frequently","ALWAYS":"always","id_y":"id_county"})
    return df_mask_use

# Création des tables en BD
def creation_tables():
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/covid')
    metadata_obj = MetaData()
    #metadata_obj.drop_all()
    
    states = Table(
        "states",
        metadata_obj,
        Column("id", Integer, nullable=False, primary_key=True),
        Column("name", String(128)),
        Column('fips', Integer)
    )

    counties = Table(
        "counties",
        metadata_obj,
        Column("id", Integer, nullable=False, primary_key=True),
        Column("name", String(128)),
        Column('fips', Integer),
        Column('id_state', Integer, ForeignKey(states.c.id))
    )

    counts = Table(
        "counts",
        metadata_obj,
        #Column("id", Integer, nullable=False, primary_key=True),
        Column("date", Date, primary_key=True),
        Column('cases', Integer),
        Column('deaths', Integer),
        Column('id_state', Integer, ForeignKey(states.c.id), nullable=True, primary_key=True),
        Column('id_county', Integer, ForeignKey(counties.c.id), nullable=True, primary_key=True)
    )

    mask_use = Table(
        "mask_use",
        metadata_obj,
        Column("id", Integer, nullable=False, primary_key=True),
        Column("never", Float),
        Column('rarely', Float),
        Column('sometimes', Float),
        Column('frequently', Float),
        Column('always', Float),
        Column('id_county', Integer, ForeignKey(counties.c.id))
    )

    metadata_obj.create_all(engine)

    
# Peuplement des tables en BD
def peuplement_tables():
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/covid')
    
    df_states = creation_dataframe_states()
    df_states.to_sql('states', con=engine, if_exists="append", index=False)
    
    df_counties = creation_dataframe_counties()
    df_counties.to_sql('counties', con=engine, if_exists="append", index=False)
    
    print("ok pour states et counties")
    time.sleep(10)
    print("fin du sleep 10")
    
    df_counts = creation_dataframe_counts('us-counties-2020.csv')
    df_counts.to_sql('counts', con=engine, if_exists="append", index=False)
    print("ok pour counts 2020")
    df_counts = creation_dataframe_counts('us-counties-2021.csv')
    df_counts.to_sql('counts', con=engine, if_exists="append", index=False)
    print("ok pour counts 2021")
    df_counts = creation_dataframe_counts('us-counties-2022.csv')
    df_counts.to_sql('counts', con=engine, if_exists="append", index=False)
    print("ok pour counts 2022")
    df_counts = creation_dataframe_counts('us-counties-2023.csv')
    df_counts.to_sql('counts', con=engine, if_exists="append", index=False)
    print("ok pour counts 2023")
    
    df_mask_use = creation_dataframe_mask_use()
    df_mask_use.to_sql('mask_use', con=engine, if_exists="append", index=False)


# tests
creation_tables()
peuplement_tables()