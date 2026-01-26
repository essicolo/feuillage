"""
Exemple de génération de GeoJSON avec données de graphiques pour le visualiseur

Ce script montre comment enrichir vos GeoJSON avec des données
qui seront affichées sous forme de graphiques dans les popups.

Installation:
    pip install geopandas pandas shapely

Usage:
    python generate_geojson_with_charts.py
"""

import geopandas as gpd
import pandas as pd
import json
from shapely.geometry import Point, LineString, Polygon


# ============================================================================
# Exemple 1: Bassins versants avec débits mensuels
# ============================================================================

def generer_debits_mensuels_fictifs():
    """Génère des données de débits mensuels fictifs"""
    return {
        "labels": ["Jan", "Fév", "Mar", "Avr", "Mai", "Jun",
                   "Jul", "Aoû", "Sep", "Oct", "Nov", "Déc"],
        "values": [12.5, 15.3, 22.1, 45.2, 38.7, 25.4,
                   18.9, 16.2, 20.8, 28.3, 19.5, 14.2]
    }


def creer_bassins_versants_exemple():
    """Crée un GeoDataFrame de bassins versants avec données de graphiques"""

    # Créer des polygones fictifs
    bassins = gpd.GeoDataFrame({
        'nom': ['Bassin Saint-Charles', 'Bassin Montmorency', 'Bassin Beauport'],
        'superficie_ha': [545.2, 423.8, 312.5],
        'municipalite': ['Québec', 'Québec', 'Québec'],
        'annee': [2023, 2023, 2023],
        'geometry': [
            Polygon([(-71.3, 46.85), (-71.2, 46.85), (-71.2, 46.88), (-71.3, 46.88)]),
            Polygon([(-71.2, 46.88), (-71.1, 46.88), (-71.1, 46.91), (-71.2, 46.91)]),
            Polygon([(-71.15, 46.82), (-71.05, 46.82), (-71.05, 46.85), (-71.15, 46.85)])
        ]
    }, crs="EPSG:4326")

    # Ajouter des données de graphiques pour chaque bassin
    for idx, row in bassins.iterrows():
        # Convertir le dictionnaire en chaîne JSON
        bassins.at[idx, 'debits_mensuels'] = json.dumps(generer_debits_mensuels_fictifs())

    # Sauvegarder
    bassins.to_file("bassins_versants_avec_graphiques.geojson", driver="GeoJSON")
    print("✓ bassins_versants_avec_graphiques.geojson créé")


# ============================================================================
# Exemple 2: Cours d'eau avec profil d'élévation
# ============================================================================

def creer_profil_elevation(longueur_km):
    """Génère un profil d'élévation fictif pour un cours d'eau"""
    # Générer des points tous les 5 km
    distances = list(range(0, int(longueur_km) + 1, 5))
    # Élévation qui diminue avec la distance (simulation d'une rivière)
    elevations = [250 - (d * 0.8) for d in distances]

    return {
        "labels": distances,
        "values": elevations
    }


def creer_cours_eau_exemple():
    """Crée un GeoDataFrame de cours d'eau avec profils d'élévation"""

    # Créer des lignes fictives
    cours_eau = gpd.GeoDataFrame({
        'nom_cours': ['Rivière Saint-Charles', 'Rivière Montmorency', 'Rivière Beauport'],
        'longueur_km': [35.2, 28.5, 22.3],
        'ordre_strahler': [4, 3, 3],
        'municipalite': ['Québec', 'Québec', 'Québec'],
        'geometry': [
            LineString([(-71.3, 46.85), (-71.25, 46.86), (-71.2, 46.87), (-71.15, 46.88)]),
            LineString([(-71.2, 46.88), (-71.15, 46.89), (-71.1, 46.90)]),
            LineString([(-71.15, 46.82), (-71.12, 46.83), (-71.10, 46.84)])
        ]
    }, crs="EPSG:4326")

    # Ajouter des profils d'élévation
    for idx, row in cours_eau.iterrows():
        profil = creer_profil_elevation(row['longueur_km'])
        cours_eau.at[idx, 'profil_elevation'] = json.dumps(profil)

    # Sauvegarder
    cours_eau.to_file("cours_eau_avec_graphiques.geojson", driver="GeoJSON")
    print("✓ cours_eau_avec_graphiques.geojson créé")


# ============================================================================
# Exemple 3: Stations de mesure avec historique de débits
# ============================================================================

def generer_historique_debit():
    """Génère un historique de débit fictif sur 12 mois"""
    return {
        "labels": ["Jan 23", "Fév 23", "Mar 23", "Avr 23", "Mai 23", "Jun 23",
                   "Jul 23", "Aoû 23", "Sep 23", "Oct 23", "Nov 23", "Déc 23"],
        "values": [15.2, 18.5, 25.3, 48.2, 42.1, 28.5,
                   20.3, 17.8, 22.5, 30.2, 21.8, 16.5]
    }


def creer_stations_exemple():
    """Crée un GeoDataFrame de stations de mesure avec historiques"""

    # Créer des points fictifs
    stations = gpd.GeoDataFrame({
        'code': ['ST-001', 'ST-002', 'ST-003'],
        'nom': ['Station Saint-Charles Amont', 'Station Montmorency', 'Station Beauport'],
        'type': ['Débitmètre', 'Débitmètre', 'Pluviomètre'],
        'installation': ['2020-03-15', '2019-11-02', '2021-06-20'],
        'actif': [True, True, False],
        'geometry': [
            Point(-71.25, 46.86),
            Point(-71.15, 46.89),
            Point(-71.12, 46.83)
        ]
    }, crs="EPSG:4326")

    # Ajouter des historiques de débit
    for idx, row in stations.iterrows():
        if row['type'] == 'Débitmètre':
            stations.at[idx, 'historique_debit'] = json.dumps(generer_historique_debit())

    # Sauvegarder
    stations.to_file("stations_avec_graphiques.geojson", driver="GeoJSON")
    print("✓ stations_avec_graphiques.geojson créé")


# ============================================================================
# Exemple 4: Utiliser des données réelles depuis un DataFrame
# ============================================================================

def creer_avec_donnees_reelles():
    """
    Exemple avec des données réelles depuis un DataFrame pandas
    """

    # Simuler un DataFrame de mesures de débit
    mesures = pd.DataFrame({
        'bassin_id': [1, 1, 1, 1, 2, 2, 2, 2],
        'mois': ['Jan', 'Fév', 'Mar', 'Avr', 'Jan', 'Fév', 'Mar', 'Avr'],
        'debit': [12.5, 15.3, 22.1, 45.2, 18.2, 20.5, 28.9, 52.1]
    })

    # Créer un GeoDataFrame de bassins
    bassins = gpd.GeoDataFrame({
        'id': [1, 2],
        'nom': ['Bassin A', 'Bassin B'],
        'geometry': [
            Polygon([(-71.3, 46.85), (-71.2, 46.85), (-71.2, 46.88), (-71.3, 46.88)]),
            Polygon([(-71.2, 46.88), (-71.1, 46.88), (-71.1, 46.91), (-71.2, 46.91)])
        ]
    }, crs="EPSG:4326")

    # Fonction pour créer les données de graphique depuis les mesures
    def creer_donnees_graphique_reelles(bassin_id):
        donnees = mesures[mesures['bassin_id'] == bassin_id]
        return {
            "labels": donnees['mois'].tolist(),
            "values": donnees['debit'].tolist()
        }

    # Ajouter les graphiques basés sur les vraies données
    for idx, row in bassins.iterrows():
        graphique_data = creer_donnees_graphique_reelles(row['id'])
        bassins.at[idx, 'debits_mensuels'] = json.dumps(graphique_data)

    # Sauvegarder
    bassins.to_file("bassins_donnees_reelles.geojson", driver="GeoJSON")
    print("✓ bassins_donnees_reelles.geojson créé")


# ============================================================================
# Fonction principale
# ============================================================================

def main():
    """Génère tous les exemples de GeoJSON"""
    print("Génération des fichiers GeoJSON avec données de graphiques...\n")

    creer_bassins_versants_exemple()
    creer_cours_eau_exemple()
    creer_stations_exemple()
    creer_avec_donnees_reelles()

    print("\n✓ Tous les fichiers ont été générés avec succès!")
    print("\nPour les utiliser:")
    print("1. Chargez les fichiers .geojson dans le visualiseur")
    print("2. Ou créez un fichier view-config.json pour une vue complète")
    print("\nFormat des données de graphique dans le GeoJSON:")
    print('  "debits_mensuels": "{\\"labels\\": [...], \\"values\\": [...]}"')


if __name__ == "__main__":
    main()
