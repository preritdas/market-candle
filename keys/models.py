"""Models for the keys."""
from pydantic import BaseModel


class GeneralModel(BaseModel):
    """
    Model for general keys.
    """
    api_auth_token: str


class Keys(BaseModel):
    """
    Model for all keys.
    """
    General: GeneralModel
