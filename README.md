# Visualiseur GeoJSON

Application web 100% statique pour visualiser et gérer plusieurs fichiers GeoJSON sur une carte interactive Leaflet.

## Fonctionnalités

### Chargement de données
- **Chargement par URL** : Collez l'URL d'un fichier GeoJSON distant
- **Téléversement de fichier** : Chargez des fichiers `.geojson` ou `.json` depuis votre ordinateur
- **Exemple intégré** : Bouton pour charger automatiquement les bassins versants de la Ville de Québec
- **Gestion des gros fichiers** : Avertissement automatique pour les fichiers > 5 MB

### Gestion des couches
- **Panneau de gestion** : Interface latérale gauche listant toutes les couches chargées
- **Visibilité** : Cases à cocher pour activer/désactiver chaque couche
- **Renommage flexible** :
  - Lors du chargement via dialogue
  - Après chargement via le bouton "Renommer" dans le panneau
- **Suppression individuelle** : Retirez des couches spécifiques
- **Effacer tout** : Supprimez toutes les couches en un clic
- **Bouton de collapse** : Masquer/afficher le panneau (bas gauche de l'écran)

### Interface utilisateur
- **Menu hamburger** : Accès à toutes les fonctions via le menu en haut à droite
- **Export de configuration** : Sauvegardez votre vue actuelle en fichier `config.json`
- **Interface épurée** : Carte plein écran avec contrôles discrets
- **Design responsive** : Adaptation mobile et desktop

### Visualisation
- **Popups automatiques** : Affichage de toutes les propriétés pour chaque feature
- **Popups avec graphiques** : Support de Chart.js pour afficher des graphiques dans les popups
- **Templates de popups** : Système de templates configurables pour personnaliser l'affichage
- **Zoom automatique** : Centrage sur les données chargées
- **Palette accessible** : Couleurs distinctes respectant les principes WCAG
- **Support multi-géométries** : Point, LineString, Polygon, MultiPoint, etc.
- **Style adaptatif** : Styles différenciés selon le type de géométrie
- **Fonds de carte** : OpenStreetMap, OpenTopoMap, CartoDB Positron

### Vues configurables
- **Fichiers de configuration** : Chargement de vues pré-configurées (JSON)
- **Distribution publique** : Partagez des vues complètes avec couches et popups
- **Templates personnalisés** : Définissez l'affichage des popups par type de donnée
- **Graphiques intégrés** : Bar charts, line charts pour visualiser vos données
- **Export** : Exportez votre configuration actuelle pour la réutiliser

### Accessibilité
- **Palette de couleurs accessible** : Compatible avec le daltonisme
- **Messages d'erreur clairs** : Retours visuels pour chaque action
- **Interface responsive** : Adaptation mobile et desktop
- **Pas de dépendances** : Fonctionne sans backend ni frameworks JS

## Déploiement

### GitHub Pages

1. **Créez un nouveau dépôt sur GitHub**
2. **Poussez le fichier `index.html`**
   ```bash
   git init
   git add index.html
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/VOTRE_USERNAME/VOTRE_REPO.git
   git push -u origin main
   ```
3. **Activez GitHub Pages**
   - Allez dans `Settings > Pages`
   - Source : `Deploy from a branch`
   - Branch : `main` / `root`
   - Cliquez sur `Save`
4. **Accédez à votre site** : `https://VOTRE_USERNAME.github.io/VOTRE_REPO/`

### Cloudflare Pages

1. **Connectez votre dépôt GitHub à Cloudflare Pages**
2. **Configuration du build** :
   - Build command : (laisser vide)
   - Build output directory : `/`
3. **Déployez** : Le site sera accessible sur `VOTRE_PROJET.pages.dev`

### Utilisation locale

Ouvrez simplement `index.html` dans votre navigateur. Aucun serveur web requis !

> **Note** : Pour charger des fichiers depuis des URLs externes, votre navigateur doit autoriser les requêtes CORS. Les fichiers locaux et les URLs publiques comme données.québec.ca fonctionnent sans problème.

## Guide d'utilisation

### 1. Ouvrir le menu

Cliquez sur le bouton **menu hamburger** (icône ≡) en haut à droite pour accéder à toutes les fonctions.

### 2. Charger un GeoJSON par URL

1. Dans le menu, collez l'URL du fichier dans le champ de texte
2. Cliquez sur **"Ajouter"** ou appuyez sur `Entrée`
3. Entrez un nom pour la couche dans la boîte de dialogue
4. La couche s'affiche automatiquement sur la carte

**Exemple d'URL** :
```
https://www.donneesquebec.ca/recherche/dataset/.../vdq-hydrobassinversant.geojson
```

### 3. Charger un fichier local

1. Dans le menu, cliquez sur **"Choisir un fichier GeoJSON"**
2. Sélectionnez un fichier `.geojson` ou `.json`
3. Entrez un nom pour la couche
4. La couche s'affiche automatiquement

### 4. Charger une configuration

1. Dans le menu, section "Configuration", cliquez sur **"Charger une configuration"**
2. Sélectionnez votre fichier `config.json`
3. Toutes les couches et templates se chargent automatiquement

### 5. Exporter votre configuration

1. Chargez vos couches et configurez votre vue (position, zoom, visibilité)
2. Ouvrez le menu et cliquez sur **"Exporter la configuration"**
3. Entrez un nom pour votre configuration
4. Le fichier `config.json` est téléchargé automatiquement

**Utilisations** :
- Sauvegarder votre travail pour le reprendre plus tard
- Créer plusieurs configurations pour différents bassins/zones
- Partager votre configuration avec des collègues

**Note importante** : Si vos couches ont été chargées depuis des fichiers locaux, les URLs dans le fichier exporté seront génériques (`./votre-fichier.geojson`). Vous devrez les modifier manuellement pour pointer vers les bons fichiers.

### 6. Gérer les couches

**Panneau latéral gauche** :
- Affiche toutes les couches chargées avec leur couleur
- **Cases à cocher** : Cochez/décochez pour afficher/masquer une couche
- **Renommer** : Cliquez sur "Renommer" pour changer le nom
- **Supprimer** : Cliquez sur l'icône poubelle pour retirer une couche

**Bouton de collapse (bas gauche)** :
- Cliquez pour masquer/afficher le panneau latéral
- Pratique pour avoir une vue dégagée de la carte

### 7. Explorer les données

- **Cliquez** sur n'importe quelle feature pour voir ses propriétés dans un popup
- **Zoomez/Déplacez** la carte pour naviguer
- Le zoom s'ajuste automatiquement lors du chargement
- **Changez le fond de carte** dans le panneau latéral (OpenStreetMap, OpenTopoMap, CartoDB)

### 8. Charger l'exemple

Dans le menu, cliquez sur **"Charger l'exemple"** pour charger automatiquement le GeoJSON des bassins versants de la Ville de Québec.

### 9. Effacer les données

Dans le menu, cliquez sur **"Effacer tout"** pour supprimer toutes les couches et recommencer.

## Créer une configuration personnalisée

Les configurations permettent de distribuer publiquement des cartes pré-configurées avec plusieurs couches, des popups personnalisés et des graphiques.

### Workflow recommandé

**Option 1 : Export depuis l'interface**
1. Chargez vos couches manuellement dans l'application
2. Ajustez la position de la carte, le zoom, la visibilité des couches
3. Exportez la configuration via le menu
4. Éditez le fichier `config.json` pour :
   - Corriger les URLs (si fichiers locaux)
   - Ajouter des templates de popups
   - Ajouter des graphiques

**Option 2 : Création manuelle**
1. Créez votre fichier `config.json` directement (voir structure ci-dessous)
2. Testez en le chargeant via le menu "Charger une configuration"
3. Ajustez jusqu'à satisfaction

### Distribution d'une configuration pré-chargée

Pour distribuer une configuration qui se charge automatiquement au démarrage :

1. **Créez votre dossier de distribution** :
   ```
   mon-projet/
   ├── index.html
   ├── config.json              ← Nom important !
   ├── bassins.geojson
   └── stations.geojson
   ```

2. **Configurez `config.json`** avec des URLs relatives :
   ```json
   {
     "view": { "name": "Ma vue", "center": [46.8, -71.2], "zoom": 11 },
     "layers": [
       { "name": "Bassins", "url": "./bassins.geojson", "popup_template": "bassin" }
     ],
     "popup_templates": { ... }
   }
   ```

3. **Déployez le dossier** : GitHub Pages, serveur web, ou partagez le ZIP

4. **Résultat** : Quand l'utilisateur ouvre `index.html`, la configuration se charge automatiquement avec toutes les couches et graphiques configurés.

### Scénario : 15 bassins différents

Si vous avez 15 bassins versants avec des configurations différentes :

**Option A : 15 dossiers séparés**
```
bassin-01/
├── index.html
├── config.json           ← Configuration pour bassin 1
└── bassin-01.geojson

bassin-02/
├── index.html
├── config.json           ← Configuration pour bassin 2
└── bassin-02.geojson
...
```

Avantage : Chaque bassin a son propre site web autonome

**Option B : Un seul dossier, plusieurs configurations**
```
tous-bassins/
├── index.html
├── config-bassin-01.json
├── config-bassin-02.json
├── ...
├── config-bassin-15.json
├── bassin-01.geojson
├── bassin-02.geojson
└── ...
```

Utilisateur charge manuellement le config souhaité via le menu.

**Option C : Un fichier config.json avec tous les bassins**
```json
{
  "view": { "name": "Tous les bassins", "center": [46.8, -71.2], "zoom": 9 },
  "layers": [
    { "name": "Bassin 1", "url": "./bassin-01.geojson", "visible": true },
    { "name": "Bassin 2", "url": "./bassin-02.geojson", "visible": false },
    ...
  ]
}
```

Tous les bassins chargés, visibilité contrôlée par cases à cocher.

### Structure du fichier de configuration

Créez un fichier `config.json` :

```json
{
  "view": {
    "name": "Nom de votre vue",
    "description": "Description optionnelle",
    "center": [46.8, -71.2],
    "zoom": 11,
    "basemap": "osm"
  },
  "layers": [
    {
      "name": "Nom de la couche",
      "url": "https://example.com/data.geojson",
      "visible": true,
      "color": "#0072B2",
      "popup_template": "nom_du_template"
    }
  ],
  "popup_templates": {
    "nom_du_template": {
      "title": "{properties.nom}",
      "sections": [
        {
          "type": "properties",
          "fields": ["champ1", "champ2", "champ3"]
        },
        {
          "type": "chart",
          "chart_type": "bar",
          "data_field": "nom_propriete_avec_donnees",
          "options": {
            "title": "Titre du graphique",
            "xlabel": "Axe X",
            "ylabel": "Axe Y"
          }
        }
      ]
    }
  }
}
```

**Paramètres disponibles** :

- **view.basemap** : `"osm"`, `"topo"`, ou `"positron"`
- **layers[].visible** : `true` ou `false` (visibilité initiale)
- **layers[].color** : Code couleur hexadécimal (optionnel, palette auto sinon)
- **popup_templates** : Objet définissant les templates de popups (optionnel)

### Types de graphiques supportés

- **bar** : Graphique à barres
- **line** : Graphique linéaire
- **pie** : Graphique circulaire (expérimental)

### Préparer vos GeoJSON avec données de graphiques

Utilisez GeoPandas pour ajouter des données de graphiques à vos GeoJSON :

```python
import geopandas as gpd
import json

# Charger votre GeoDataFrame
gdf = gpd.read_file("bassins.geojson")

# Ajouter des données de graphique
for idx, row in gdf.iterrows():
    graphique_data = {
        "labels": ["Jan", "Fév", "Mar", "Avr", "Mai", "Jun"],
        "values": [12.5, 15.3, 22.1, 45.2, 38.7, 25.4]
    }
    gdf.at[idx, 'debits_mensuels'] = json.dumps(graphique_data)

# Sauvegarder
gdf.to_file("bassins_enrichis.geojson", driver="GeoJSON")
```

Un script Python complet d'exemple est disponible : `generate_geojson_with_charts.py`

### Exemple complet

Voir le fichier `config-example.json` pour un exemple complet de configuration avec multiples templates et graphiques.

## Palette de couleurs

L'application utilise une palette de 10 couleurs accessibles, optimisée pour :
- Contraste élevé sur fond de carte
- Distinction pour les personnes daltoniennes
- Conformité WCAG 2.1

**Couleurs** : Bleu (#0072B2), Orange (#D55E00), Vert sarcelle (#009E73), Rose (#CC79A7), Jaune (#F0E442), Bleu ciel (#56B4E9), Orange doré (#E69F00), Magenta foncé (#882255), Vert cyan (#44AA99), Beige (#DDCC77).

## Personnalisation

### Modifier la vue par défaut

Dans `index.html`, recherchez :
```javascript
const map = L.map('map').setView([46.8, -71.2], 6);
```
- `[46.8, -71.2]` : Latitude, Longitude (Québec)
- `6` : Niveau de zoom (1 = monde entier, 18 = rue)

### Modifier la limite de fichier

Dans `index.html`, recherchez :
```javascript
const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5 MB
```

## Structure du projet

```
feuillage/
├── index.html                              # Application complète (autonome)
├── config.json                             # Configuration de vue (chargement automatique)
├── config-example.json                     # Exemple de configuration avancée
├── bassins_versants_avec_graphiques.geojson # Exemple avec données de graphiques
├── generate_geojson_with_charts.py         # Script Python pour générer des GeoJSON avec graphiques
└── README.md                               # Ce fichier
```

**Note** : Si `config.json` existe dans le même dossier que `index.html`, il sera chargé automatiquement au démarrage.

## Sécurité et vie privée

- **100% côté client** : Aucune donnée n'est envoyée à un serveur
- **Pas de tracking** : Aucun cookie ni analytics
- **Fichiers locaux** : Vos données restent sur votre machine
- **CDN externes** : Seuls Leaflet, Chart.js, Iconify et Tailwind CSS sont chargés depuis CDN

## Dépannage

### "Erreur HTTP: 403" lors du chargement d'une URL

- Le serveur distant bloque les requêtes CORS
- **Solution** : Téléchargez le fichier et chargez-le localement

### La carte ne s'affiche pas

- Vérifiez votre connexion Internet (Leaflet est chargé depuis CDN)
- Ouvrez la console du navigateur (F12) pour voir les erreurs

### "Format GeoJSON invalide"

- Vérifiez que le fichier est un JSON valide
- Le fichier doit avoir `"type": "FeatureCollection"` ou `"type": "Feature"`
- Validez votre GeoJSON sur [geojson.io](https://geojson.io)

### Le fichier est trop volumineux

- Essayez de simplifier les géométries (ex: [mapshaper.org](https://mapshaper.org))
- Divisez le fichier en plusieurs fichiers plus petits
- Acceptez l'avertissement si votre ordinateur est assez puissant

### Les graphiques ne s'affichent pas

- Vérifiez que le champ `data_field` existe dans les propriétés de votre GeoJSON
- Les données doivent être au format JSON : `{"labels": [...], "values": [...]}`
- Ouvrez la console (F12) pour voir les erreurs détaillées

## Technologies utilisées

- **Leaflet 1.9.4** : Bibliothèque de cartographie interactive
- **Chart.js 4.4.1** : Bibliothèque de graphiques interactifs
- **Iconify 3.1.0** : Icônes vectorielles
- **Tailwind CSS** : Framework CSS utilitaire
- **OpenStreetMap** : Fond de carte par défaut
- **HTML5/CSS3** : Interface utilisateur
- **JavaScript ES6+** : Logique de l'application

## Licence

Ce projet est libre d'utilisation et de modification. Aucune restriction.

## Contribution

Pour signaler un bug ou suggérer une amélioration :
1. Créez un fichier avec votre suggestion
2. Partagez-le avec l'auteur du projet

## Ressources

- [Documentation Leaflet](https://leafletjs.com/reference.html)
- [Documentation Chart.js](https://www.chartjs.org/docs/latest/)
- [Données Québec](https://www.donneesquebec.ca/)
- [Spécification GeoJSON](https://geojson.org/)
- [Validateur GeoJSON](https://geojson.io/)
- [Iconify Icons](https://icon-sets.iconify.design/)
- [Tailwind CSS](https://tailwindcss.com/)

