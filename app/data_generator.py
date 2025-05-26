import random
import asyncio
from datetime import datetime, timedelta
from fastapi import FastAPI
from faker import Faker
import nest_asyncio

nest_asyncio.apply()
fake = Faker('fr_FR')
app = FastAPI()

# ---------------------- Données statiques ----------------------

bibliotheques = []
salles = []
etudiants_data = []
livres = []

def generate_bibliotheques():
    for i in range(1, 6):
        bibliotheques.append({
            "id_bibliotheque": i,
            "nom": f"BU {fake.city()}",
            "adresse": fake.address().replace('\n', ', ')
        })

def generate_salles():
    for i in range(1, 21):
        salles.append({
            "id_salle": f"S{i:03d}",
            "nom_salle": f"Salle {i}",
            "capacite": random.choice([4, 6, 8, 10]),
            "id_bibliotheque": random.choice(bibliotheques)["id_bibliotheque"]
        })

def generate_etudiants(n=50):
    for i in range(1, n + 1):
        etudiants_data.append({
            "id": i,
            "nom": fake.last_name(),
            "prenom": fake.first_name(),
            "programme": random.choice(["Info", "Médecine", "Droit", "Économie"]),
            "date_inscription": fake.date_between(start_date='-4y', end_date='today')
        })

def generate_livres(n=200):
    for i in range(1, n + 1):
        livres.append({
            "id_livre": i,
            "titre": fake.sentence(nb_words=4),
            "isbn": fake.isbn13(),
            "disponible": random.choices([True, False], weights=[0.8, 0.2])[0]
        })
