"""Root API."""
from fastapi import FastAPI

import random

from api.models import Candle


app = FastAPI(
    title="Market Candle API",
    description="API for market candle data.",
    version="0.0.1"
)


@app.get("/")
async def root():
    """Root endpoint."""
    return "API is alive and well."


@app.get("/candle")
async def candle() -> Candle:
    """Get the latest candle data. Mocked currently."""
    return Candle(
        candle_top=random.randint(4, 9),
        candle_bottom=random.randint(4, 9),
        wick_top=random.randint(4, 9),
        wick_bottom=random.randint(4, 9),
    )
