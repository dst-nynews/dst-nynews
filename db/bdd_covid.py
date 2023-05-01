import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, insert, delete, ForeignKey, Date, Float
import time
from sqlalchemy.sql import text
from typing import Optional
import json

class Bdd_Covid:
    def __init__(self, path_csv_files: Optional[str] = None) -> None:
        """Instanciate a connection to a PostGres sql databasefetch data from an API of the NY Times.
        """
        self.path_csv_files = path_csv_files
        self.engine = create_engine('postgresql://postgres:postgres@localhost:5432/covid')


# Créations des dataframes pour chaque table à partir des csv
    def creation_dataframe_states(self):
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

    def creation_dataframe_counties(self):
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

    def creation_dataframe_counts(self, counts_csv):
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

    def creation_dataframe_mask_use(self):
        df = pd.read_csv('mask-use-by-county.csv')
        df_mask_use = df.reset_index()
        df_mask_use = df_mask_use.rename(columns={"index": "id"})
        df_counties = creation_dataframe_counties()
        df_merged = pd.merge(df_mask_use, df_counties, left_on='COUNTYFP', right_on='fips', how='left')
        df_merged = df_merged.drop(['COUNTYFP','name','fips','id_state'], axis =1)
        df_mask_use = df_merged.rename(columns={"id_x": "id","NEVER":"never","RARELY":"rarely","SOMETIMES":"sometimes","FREQUENTLY":"frequently","ALWAYS":"always","id_y":"id_county"})
        return df_mask_use

# Création des tables en BD
    def creation_tables(self):
        #engine = create_engine('postgresql://postgres:postgres@localhost:5432/covid')
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

        metadata_obj.create_all(self.engine)

    
# Peuplement des tables en BD
    def peuplement_tables(self):
        #engine = create_engine('postgresql://postgres:postgres@localhost:5432/covid')
        
        df_states = self.creation_dataframe_states()
        df_states.to_sql('states', con=self.engine, if_exists="append", index=False)
        
        df_counties = self.creation_dataframe_counties()
        df_counties.to_sql('counties', con=self.engine, if_exists="append", index=False)
        
        print("ok pour states et counties")
        time.sleep(10)
        print("fin du sleep 10")
        
        df_counts = self.creation_dataframe_counts('us-counties-2020.csv')
        df_counts.to_sql('counts', con=self.engine, if_exists="append", index=False)
        print("ok pour counts 2020")
        df_counts = self.creation_dataframe_counts('us-counties-2021.csv')
        df_counts.to_sql('counts', con=self.engine, if_exists="append", index=False)
        print("ok pour counts 2021")
        df_counts = self.creation_dataframe_counts('us-counties-2022.csv')
        df_counts.to_sql('counts', con=self.engine, if_exists="append", index=False)
        print("ok pour counts 2022")
        df_counts = self.creation_dataframe_counts('us-counties-2023.csv')
        df_counts.to_sql('counts', con=self.engine, if_exists="append", index=False)
        print("ok pour counts 2023")
        
        df_mask_use = self.creation_dataframe_mask_use()
        df_mask_use.to_sql('mask_use', con=self.engine, if_exists="append", index=False)


# requêtes sql sur la BD Covid:
# 1. Sur une période de temps définie par le user: sortir le nombre de cas covid et de deaths au total et par states
# 2. Mask use: moyenne par states des stats de mask use: never, rarely, sometimes, frequently, always
# 3. Obtenir à partir de 1 county (= 1 county name et 1 state name en input): le nbr total de cases, deaths et pour ce même
#    county, afficher les stats de mask use pour voir l'incidence.
# Bonus: ML: Faire une prédiction des cases et deaths par state/county en fonction du mask use

    def request_1(self, date_debut, date_fin):
            with self.engine.connect() as con:
                sql_request = "select s.name as \"state\" , sum(c.cases) as \"Total cases \" , sum(c.deaths) as \"Total deaths\" from counts c inner join states s on s.id = c.id_state where date >= '"+ date_debut +"' and date <= '"+ date_fin + "' group by s.name order by s.name ;"
                request = text(sql_request)

                results = con.execute(request)
            
            return results


# tests
#bdd_covid = Bdd_Covid()
#bdd_covid.creation_tables()
#bdd_covid.peuplement_tables()
#print(bdd_covid.request_1('2020-08-01','2020-08-10'))
#results = bdd_covid.request_1('2020-08-01','2020-08-10')
#print(results)

#for e in results:
#   print(e)

#print(json.dumps([dict(r) for r in results]))
