from pydantic import BaseModel

class Ability(BaseModel):
    name: str
    url: str

class Abilities(BaseModel):
    ability: Ability
    is_hidden: bool
    slot: int