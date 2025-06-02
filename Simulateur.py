import random
import pandas as pd
from datetime import datetime, timedelta

# 📅 Point de départ : 8h du matin
heure_courante = datetime(2025, 6, 1, 8, 0, 0)

# 🧾 Liste pour stocker les logs simulés
logs = []

# 🔁 Générer 200 événements simulés
for _ in range(100):
    # Temps entre deux voitures (5 à 60 min)
    temps_attente = timedelta(minutes=random.randint(5, 60))
    heure_arrivee = heure_courante + temps_attente

    # Durée de stationnement (30 min à 3h)
    duree = timedelta(minutes=random.randint(30, 180))
    heure_depart = heure_arrivee + duree

    # Place choisie au hasard (1 à 10)
    place = random.randint(1, 10)

    # ✍️ Ajouter l'arrivée
    logs.append({
        "action": "arrival",
        "spot": place,
        "timestamp": heure_arrivee.strftime("%Y-%m-%d %H:%M:%S")
    })

    # ✍️ Ajouter le départ
    logs.append({
        "action": "departure",
        "spot": place,
        "timestamp": heure_depart.strftime("%Y-%m-%d %H:%M:%S")
    })

    # Préparer la prochaine arrivée
    heure_courante = heure_arrivee

# 🧾 Créer le DataFrame
df = pd.DataFrame(logs)

# 💾 Sauvegarder dans un fichier CSV
df.to_csv("logs_simules.csv", index=False)

print("✅ Fichier logs_simules.csv généré avec succès.")
