import os
import sys
sys.path.insert(0,".")
from fastapi import APIRouter
from db.bdd_covid import Bdd_Covid
import json
import sys
sys.setrecursionlimit(50000)

# Instanciate a router for this endpoint
routeSe = APIRouter()

# Import Bdd Covid to request local covid postgres sql bdd
bdd_covid = Bdd_Covid()

# requêtes sql sur la BD Covid:
# 1. Sur une période de temps définie par le user: sortir le nombre de cas covid et de deaths au total et par states
# 2. Mask use: moyenne par states des stats de mask use: never, rarely, sometimes, frequently, always
# 3. Obtenir à partir de 1 county (= 1 county name et 1 state name en input): le nbr total de cases, deaths et pour ce même
#    county, afficher les stats de mask use pour voir l'incidence.

# Retourne le résultat de la requete cases_deaths_by_date_by_state de la bd covid 
@routeSe.get('/cases_deaths_by_date_by_state', name='Nombre de cases et deaths au total et par states', tags=['Covid'])
async def cases_deaths_by_date_by_state(date_debut, date_fin):
    answer = bdd_covid.cases_deaths_by_date_by_state(date_debut, date_fin)
    return json.dumps([dict(r) for r in answer])


# Retourne le résultat de la requete total_cases_by_date de la bd covid 
@routeSe.get('/total_cases_by_date', name='Nombre de cases au total', tags=['Covid'])
async def total_cases_by_date(date_debut, date_fin):
    answer = bdd_covid.total_cases_by_date(date_debut, date_fin)
    return json.dumps([dict(r) for r in answer])


# Retourne le résultat de la requete total_deaths_by_date de la bd covid 
@routeSe.get('/total_deaths_by_date', name='Nombre de deaths au total', tags=['Covid'])
async def total_deaths_by_date(date_debut, date_fin):
    answer = bdd_covid.total_deaths_by_date(date_debut, date_fin)
    return json.dumps([dict(r) for r in answer])


# Retourne le résultat de la requete avg_mask_use_by_state de la bd covid 
@routeSe.get('/avg_mask_use_by_state', name='Moyenne utilisation du mask pour un state', tags=['Covid'])
async def avg_mask_use_by_state(state):
    answer = bdd_covid.avg_mask_use_by_state(state)
    return json.dumps([dict(r) for r in answer])