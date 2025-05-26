from fastapi import FastAPI
import asyncio
from app.data_generator import (
    bibliotheques, salles, visites, reservations, prets,
    generate_bibliotheques, generate_salles, generate_etudiants,
    generate_livres, generate_dynamic_data
)


app = FastAPI()

@app.get("/visites_bu")
def get_visites():
    return visites

@app.get("/reservations_salles")
def get_reservations():
    return reservations

@app.get("/prets")
def get_prets():
    return prets

@app.on_event("startup")
async def startup():
    generate_bibliotheques()
    generate_salles()
    generate_etudiants()
    generate_livres()
    asyncio.create_task(generate_dynamic_data())
