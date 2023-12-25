"""Check security of inbound requests."""
from fastapi import Header, HTTPException

from keys import KEYS


async def check_authorized_requester(api_auth_token: str = Header(...)):
    """Check if the requester is authorized to use the API."""
    if api_auth_token != KEYS.General.api_auth_token:
        raise HTTPException(status_code=401, detail="Unauthorized")
