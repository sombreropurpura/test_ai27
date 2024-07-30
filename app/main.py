import uvicorn
from fastapi import FastAPI
from routers import abilities

app: FastAPI = FastAPI(
    title='PokeAPI Technical Test',
    description='API to obtain Pokémon abilities using data from the PokéAPI.',
    version='1.0.0'
)

app.include_router(abilities.router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=9080)