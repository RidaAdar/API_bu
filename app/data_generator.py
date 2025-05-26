import random
import asyncio
from datetime import datetime, timedelta
from faker import Faker

fake = Faker('fr_FR')

# ---------------------- Données en mémoire ----------------------

bibliotheques = []
salles = []
etudiants_data = []
livres = []

visites = []
reservations = []
prets = []

# ---------------------- Génération des données statiques ----------------------

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

# ---------------------- Génération de données dynamiques ----------------------

async def generate_dynamic_data():
    while True:
        now = datetime.now()

        # Générer des visites pour chaque BU
        for b in bibliotheques:
            visites.append({
                "id_bibliotheque": b["id_bibliotheque"],
                "date_heure": now.isoformat(),
                "nombre_personnes": random.randint(5, 80)
            })

        # Générer des réservations de salles
        for _ in range(random.randint(1, 5)):
            debut = now + timedelta(minutes=random.randint(0, 360))
            fin = debut + timedelta(minutes=random.choice([60, 90]))
            reservations.append({
                "id_salle": random.choice(salles)["id_salle"],
                "id_utilisateur": random.choice(etudiants_data)["id"],
                "date_reservation": now.date().isoformat(),
                "heure_debut": debut.time().isoformat(timespec="minutes"),
                "heure_fin": fin.time().isoformat(timespec="minutes")
            })

        # Générer des prêts de livres
        for _ in range(random.randint(2, 6)):
            livre = random.choice(livres)
            etu = random.choice(etudiants_data)
            date_pret = now - timedelta(days=random.randint(0, 10))
            rendu = random.choices([True, False], weights=[0.6, 0.4])[0]
            prets.append({
                "id_livre": livre["id_livre"],
                "id_utilisateur": etu["id"],
                "date_pret": date_pret.date().isoformat(),
                "date_retour": (date_pret + timedelta(days=7)).isoformat() if rendu else None,
                "rendu": rendu
            })

        print(f"📈 Nouveaux enregistrements générés à {now.strftime('%H:%M:%S')}")
        await asyncio.sleep(5)
