from external.pokeapi_client import PokeApiClient
from models.abilities import Abilities


class AbilitiesService():
    def __init__(self):
        self.client: PokeApiClient = PokeApiClient()

    async def get_pokemon_abilities(self, pokemon_name: str) -> list[Abilities]:
        pokeapi_response = await self.client.get_abilites_by_name(pokemon_name)
        poke_abilities: list[Abilities] = [Abilities(
            ability=ability['ability'],
            is_hidden=ability['is_hidden'],
            slot=ability['slot']) for ability in pokeapi_response['abilities']]
        return poke_abilities
