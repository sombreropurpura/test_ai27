import secrets
from fastapi import (
    status,
    Depends, 
    HTTPException
)
from fastapi.security import (
    HTTPBasic,
    HTTPBasicCredentials
)
from config import API_USERNAME, API_PASSWORD
from hashlib import sha256

def basic_auth(credentials: HTTPBasicCredentials = Depends(HTTPBasic())):
    is_username: bool = secrets.compare_digest(credentials.username, API_USERNAME)
    is_password: bool = secrets.compare_digest(
        sha256(credentials.password.encode()).hexdigest(), 
        sha256(API_PASSWORD.encode()).hexdigest())
    
    if not (is_username and is_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"www-authenticate": "Basic"}
        )
    
    return credentials.username