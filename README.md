# 🗺️ Visualiseur GeoJSON - Québec

Application web 100% statique pour visualiser et gérer plusieurs fichiers GeoJSON sur une carte interactive Leaflet.

## 📋 Fonctionnalités

### Chargement de données
- ✅ **Chargement par URL** : Collez l'URL d'un fichier GeoJSON distant
- ✅ **Téléversement de fichier** : Chargez des fichiers `.geojson` ou `.json` depuis votre ordinateur
- ✅ **Exemple intégré** : Bouton pour charger automatiquement les bassins versants de la Ville de Québec
- ✅ **Gestion des gros fichiers** : Avertissement automatique pour les fichiers > 5 MB

### Gestion des couches
- ✅ **Panneau de gestion** : Interface latérale listant toutes les couches chargées
- ✅ **Contrôle Leaflet** : Widget standard pour activer/désactiver chaque couche
- ✅ **Renommage flexible** :
  - Lors du chargement via dialogue
  - Après chargement via le panneau de gestion
- ✅ **Suppression individuelle** : Retirez des couches spécifiques
- ✅ **Effacer tout** : Supprimez toutes les couches en un clic

### Visualisation
- ✅ **Popups automatiques** : Affichage de toutes les propriétés pour chaque feature
- ✅ **Zoom automatique** : Centrage sur les données chargées
- ✅ **Palette accessible** : Couleurs distinctes respectant les principes WCAG
- ✅ **Support multi-géométries** : Point, LineString, Polygon, MultiPoint, etc.
- ✅ **Style adaptatif** : Styles différenciés selon le type de géométrie

### Accessibilité
- ✅ **Palette de couleurs accessible** : Compatible avec le daltonisme
- ✅ **Messages d'erreur clairs** : Retours visuels pour chaque action
- ✅ **Interface responsive** : Adaptation mobile et desktop
- ✅ **Pas de dépendances** : Fonctionne sans backend ni frameworks JS

## 🚀 Déploiement

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

## 📖 Guide d'utilisation

### 1. Charger un GeoJSON par URL

1. Collez l'URL du fichier dans le champ de texte
2. Cliquez sur **"Ajouter URL"** ou appuyez sur `Entrée`
3. Entrez un nom pour la couche dans la boîte de dialogue
4. La couche s'affiche automatiquement sur la carte

**Exemple d'URL** :
```
https://www.donneesquebec.ca/recherche/dataset/.../vdq-hydrobassinversant.geojson
```

### 2. Charger un fichier local

1. Cliquez sur **"📁 Choisir un fichier"**
2. Sélectionnez un fichier `.geojson` ou `.json`
3. Entrez un nom pour la couche
4. La couche s'affiche automatiquement

### 3. Charger l'exemple

Cliquez sur **"✨ Exemple"** pour charger automatiquement le GeoJSON des bassins versants de la Ville de Québec.

### 4. Gérer les couches

**Panneau latéral** :
- Affiche toutes les couches chargées avec leur couleur
- **Renommer** : Cliquez sur "✏️ Renommer" pour changer le nom
- **Supprimer** : Cliquez sur "🗑️" pour retirer une couche
- **Masquer/Afficher** : Cliquez sur "◀" pour replier le panneau

**Contrôle Leaflet** (coin supérieur droit) :
- Cochez/décochez pour activer/désactiver une couche
- Utile pour comparer plusieurs jeux de données

### 5. Explorer les données

- **Cliquez** sur n'importe quelle feature pour voir ses propriétés dans un popup
- **Zoomez/Déplacez** la carte pour naviguer
- Le zoom s'ajuste automatiquement lors du chargement

### 6. Effacer les données

Cliquez sur **"🗑️ Effacer tout"** pour supprimer toutes les couches et recommencer.

## 🎨 Palette de couleurs

L'application utilise une palette de 10 couleurs accessibles, optimisée pour :
- ✅ Contraste élevé sur fond de carte
- ✅ Distinction pour les personnes daltoniennes
- ✅ Conformité WCAG 2.1

**Couleurs** : Bleu (#0072B2), Orange (#D55E00), Vert sarcelle (#009E73), Rose (#CC79A7), Jaune (#F0E442), Bleu ciel (#56B4E9), Orange doré (#E69F00), Magenta foncé (#882255), Vert cyan (#44AA99), Beige (#DDCC77).

## 🧪 Test avec le fichier d'exemple

Un fichier `test-example.geojson` est inclus pour tester localement :

```bash
# Ouvrez index.html dans votre navigateur
# Puis chargez test-example.geojson via le bouton "Choisir un fichier"
```

**Contenu du test** :
- 2 LineString (Tronçons A et B)
- 1 Point (Station de mesure)
- 1 Polygon (Zone protégée)

## 🔧 Personnalisation

### Modifier la vue par défaut

Ligne 272 dans `index.html` :
```javascript
const map = L.map('map').setView([46.8, -71.2], 6);
```
- `[46.8, -71.2]` : Latitude, Longitude (Québec)
- `6` : Niveau de zoom (1 = monde entier, 18 = rue)

### Modifier la limite de fichier

Ligne 300 dans `index.html` :
```javascript
const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5 MB
```

### Changer le fond de carte

Ligne 275 dans `index.html` :
```javascript
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors',
    maxZoom: 19
}).addTo(map);
```

**Alternatives** :
- OpenTopoMap : `https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png`
- CartoDB Positron : `https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png`
- Stamen Terrain : `https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg`

### Modifier les couleurs de l'interface

Ligne 28-32 dans `index.html` (couleur principale du header) :
```css
header {
    background-color: #095797; /* Bleu Québec */
    color: white;
}
```

## 📐 Structure du projet

```
feuillage/
├── index.html              # Application complète (autonome)
├── test-example.geojson    # Fichier de test
└── README.md               # Ce fichier
```

## 🔒 Sécurité et vie privée

- ✅ **100% côté client** : Aucune donnée n'est envoyée à un serveur
- ✅ **Pas de tracking** : Aucun cookie ni analytics
- ✅ **Fichiers locaux** : Vos données restent sur votre machine
- ✅ **Pas de dépendances externes** : Seul Leaflet est chargé depuis CDN (unpkg.com)

## 🐛 Dépannage

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

## 🛠️ Technologies utilisées

- **Leaflet 1.9.4** : Bibliothèque de cartographie interactive
- **OpenStreetMap** : Fond de carte par défaut
- **HTML5/CSS3** : Interface utilisateur
- **JavaScript ES6+** : Logique de l'application

## 📝 Licence

Ce projet est libre d'utilisation et de modification. Aucune restriction.

## 🤝 Contribution

Pour signaler un bug ou suggérer une amélioration :
1. Créez un fichier avec votre suggestion
2. Partagez-le avec l'auteur du projet

## 🌐 Ressources

- [Documentation Leaflet](https://leafletjs.com/reference.html)
- [Données Québec](https://www.donneesquebec.ca/)
- [Spécification GeoJSON](https://geojson.org/)
- [Guide de design du Québec](https://design.quebec.ca/)
- [Validateur GeoJSON](https://geojson.io/)

---

**Version** : 1.0.0
**Dernière mise à jour** : Janvier 2026
**Développé pour** : Visualisation de données géospatiales du Québec
