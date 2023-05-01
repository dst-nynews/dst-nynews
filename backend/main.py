from fastapi import FastAPI

# Local imports
from popular.routes import router as popular_router
from semantic.routes import routeSe as semantic_router
from covid.routes import routeSe as covid_router


# Instanciate the API controller
app = FastAPI(
    title="NyNews",
    description="API du projet New-York Times du Bootcamp DE de février 2023",
    version="1.0.1",
    openapi_tags=[
    {
        'name': 'Popular'
    },
    {
        'name': 'Article Search',
    },
    {
        'name': 'Semantic'
    },
    {
        'name': 'Covid'
    }
])

# Inject the endpoint "popular" in the scope of the controller
app.include_router(popular_router, tags=["Popular"], prefix="/popular")
# Inject the endpont "semantic"
app.include_router(semantic_router, tags=["Semantic"], prefix="/semantic")

# Inject the endpont "covid"
app.include_router(covid_router, tags=["Covid"], prefix="/covid")

# Root endpoint
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the NyNews API!"}


if __name__ == "__main__":
    # DEV MODE: start local server for testing
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
