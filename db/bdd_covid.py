import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, insert, delete, ForeignKey, Date, Float

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

def creation_dataframe_counts():
    df = pd.read_csv('us-counties.csv')
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
        Column("id", Integer, nullable=False, primary_key=True),
        Column("date", Date),
        Column('cases', Integer),
        Column('deaths', Integer),
        Column('id_state', Integer, ForeignKey(states.c.id)),
        Column('id_county', Integer, ForeignKey(counties.c.id))
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
    #df_counts = creation_dataframe_counts()
    #df_counts.to_sql('counts', con=engine, if_exists="append", index=False)
    df_mask_use = creation_dataframe_mask_use()
    df_mask_use.to_sql('mask_use', con=engine, if_exists="append", index=False)


# tests
creation_tables()
peuplement_tables()

"""
try:
    conn = psycopg2.connect(
          user = "postgres",
          password = "postgres",
          host = "localhost",
          port = "5432",
          database = "covid"
    )
    cur = conn.cursor()

    # Afficher la version de PostgreSQL 
    cur.execute("SELECT version();")
    version = cur.fetchone()
    print("Version : ", version,"\n")

    # Création de la table states
    cur.execute("CREATE TABLE IF NOT EXISTS states (id INTEGER NOT NULL, name VARCHAR, fips INTEGER,PRIMARY KEY (id));")
    conn.commit()

    # Création de la table counties
    cur.execute("CREATE TABLE IF NOT EXISTS counties (id INTEGER NOT NULL, name VARCHAR, fips INTEGER, id_state INTEGER, PRIMARY KEY (id), FOREIGN KEY (id_state) REFERENCES states (id));")
    conn.commit()

    # Création de la table counts
    cur.execute("CREATE TABLE IF NOT EXISTS counts (id INTEGER NOT NULL, date DATE, cases INTEGER, deaths INTEGER, id_state INTEGER, id_county INTEGER, PRIMARY KEY (id), FOREIGN KEY (id_state) REFERENCES states (id), FOREIGN KEY (id_county) REFERENCES counties (id));")
    conn.commit()

    # Création de la table mask_use
    cur.execute("CREATE TABLE IF NOT EXISTS mask_use (id INTEGER NOT NULL, never FLOAT, rarely FLOAT, sometimes FLOAT, frequently FLOAT, always FLOAT, id_county INTEGER, PRIMARY KEY (id), FOREIGN KEY (id_county) REFERENCES counties (id));")
    conn.commit()

    # Affichage des tables créées
    cur.execute("SELECT * FROM information_schema.tables where table_schema = 'public'; ")
    listTables = cur.fetchone()
    print("Liste tables : ", listTables,"\n")

    #fermeture de la connexion à la base de données
    cur.close()
    conn.close()
    print("La connexion PostgreSQL est fermée")

except (Exception, psycopg2.Error) as error :
    print ("Erreur lors de la connexion à PostgreSQL", error)


# Insertion des dataframes states, counties, counts et mask_use aux tables states, counties, counts et mask_use
engine = create_engine('postgresql://postgres:postgres@localhost:5432/covid')
#df_states = creation_table_states()
#df_states.to_sql('states', con=engine, if_exists="append", index=False)
#df_counties = creation_table_counties()
#df_counties.to_sql('counties', con=engine, if_exists="append", index=False)

metadata_obj = MetaData()

test_table = Table(
    "test_table",
    metadata_obj,
    Column("user_id", Integer, primary_key=True),
    Column("user_name", String(16), nullable=False),
)

metadata_obj.create_all(engine)

stmt = (
    insert(test_table).
    values(user_id='1', user_name='Can')
)
delete_all_rows = (
    delete(test_table)
)

with engine.connect() as conn:
    result = conn.execute(delete_all_rows)
    conn.commit()


#test_table.drop(engine)

states2 = Table(
    "states2",
    metadata_obj,
    Column("id", Integer, nullable=False, primary_key=True),
    Column("name", String(128)),
    Column('fips', Integer)
)
metadata_obj.create_all(engine)
df_states = creation_table_states()
df_states.to_sql('states2', con=engine, if_exists="append", index=False)
"""