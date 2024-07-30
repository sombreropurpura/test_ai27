from fastapi import (
    status,
    APIRouter,
    HTTPException,
    Depends
)
from fastapi.security import HTTPBasicCredentials
from httpx import HTTPStatusError
from services.abilities_service import AbilitiesService
from models.abilities import Abilities
from dependencies.auth import basic_auth

router: APIRouter = APIRouter(
    tags=["Abilities"]
)

service = AbilitiesService()


@router.get("/abilities/{pokemon_name}",
            response_model=list[Abilities],
            responses={
                status.HTTP_200_OK: {
                    "description": "Successful Response",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Abilities"
                            }
                        }
                    }
                },
                status.HTTP_404_NOT_FOUND: {
                    "description": "Not Found",
                    "content": {
                        "application/json": {
                            "example": {"detail": "Ooops! Pokémon not found!"}
                        }
                    }
                },
                status.HTTP_422_UNPROCESSABLE_ENTITY: {
                    "description": "Unprocessable Entity",
                    "content": {
                        "application/json": {
                            "example": {"detail": "Ooops! Something's wrong..."}
                        }
                    }
                },
                status.HTTP_500_INTERNAL_SERVER_ERROR: {
                    "description": "Internal Server Error",
                    "content": {
                        "application/json": {
                            "example": {"detail": "Ooops! Internal Server Error!"}
                        }
                    }
                }
            })
async def get_by_name(pokemon_name: str,
                      _: HTTPBasicCredentials = Depends(basic_auth)) -> list[Abilities]:
    try:
        return await service.get_pokemon_abilities(pokemon_name)
    except HTTPStatusError as ex:
        if ex.response.status_code == 404:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Ooops! Pokémon not found!")
        elif ex.response.status_code == 500:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ooops! Internal Server Error!")
        raise HTTPException(status_code=ex.response.status_code,
                            detail="Ooops! Something's wrong...")
