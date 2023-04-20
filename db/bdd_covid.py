import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import delete
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, insert, delete


def creation_table_states():
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

def creation_table_counties():
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
    df_states = creation_table_states()
    df_merged = pd.merge(df_counties, df_states, left_on='state', right_on='name', how='left')
    df_merged = df_merged.drop(['name_y','fips_y','state'], axis =1)
    df_counties = df_merged.rename(columns={"id_x": "id","name_x":"name","fips_x":"fips","id_y":"id_state"})
    return df_counties 

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

"""stmt = (
    insert(test_table).
    values(user_id='1', user_name='Can')
)"""
delete_all_rows = (
    delete(test_table)
)

with engine.connect() as conn:
    result = conn.execute(delete_all_rows)
    conn.commit()


#test_table.drop(engine)"""

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