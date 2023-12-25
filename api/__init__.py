"""Root API."""
from fastapi import FastAPI


app = FastAPI(
    title="Market Candle API",
    description="API for market candle data.",
    version="0.0.1"
)


@app.get("/")
async def root():
    """Root endpoint."""
    return "API is alive and well."
