"""Models for the API response."""
from pydantic import BaseModel, Field


class Candle(BaseModel):
    """Candle model."""
    candle_top: float = Field(
        ..., 
        description="Geopoisition of the top of the candle.",
        example=1.0, 
        gte=-10.0, 
        lte=10.0
    )
    candle_bottom: float = Field(
        ..., 
        description="Geopoisition of the bottom of the candle.",
        example=1.0, 
        gte=-10.0, 
        lte=10.0
    )
    wick_top: float = Field(
        ..., 
        description="Geopoisition of the top of the wick.",
        example=1.0, 
        gte=-10.0, 
        lte=10.0
    )
    wick_bottom: float = Field(
        ..., 
        description="Geopoisition of the bottom of the wick.",
        example=1.0, 
        gte=-10.0, 
        lte=10.0
    )
