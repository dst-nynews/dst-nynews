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

# Retourne le résultat de la request1 de la bd covid 
@routeSe.get('/request1', name='Nombre de cases et deaths au total et par states', tags=['Covid'])
async def resquest1_covid(date_debut, date_fin):
    answer = bdd_covid.request_1(date_debut, date_fin)
    #first = answer.first()
    #return first
    return json.dumps([dict(r) for r in answer])
    #return "request1 OK"