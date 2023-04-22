from fastapi import FastAPI
from popular.routes import router as popular_router

app = FastAPI()

# Inject Popular endpoint
app.include_router(popular_router, tags=["Popular"], prefix="/popular")


# Root endpoint
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the NyNews API!"}


if __name__ == "__main__":
    # DEV mode
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
