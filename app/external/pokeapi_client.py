import httpx
from utils.constants import (POKEAPI_URL_BASE, POKEMON_ENDPOINT)

class PokeApiClient():

    async def get_abilites_by_name(self, pokemon_name: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(f'{POKEAPI_URL_BASE}{POKEMON_ENDPOINT}{pokemon_name}')
            response.raise_for_status()
            return response.json()
