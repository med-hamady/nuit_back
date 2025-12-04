# Documentation des APIs NUIT Backend

## APIs Développées

Toutes les APIs ont été développées avec Django REST Framework (DRF).

### 1. GET /api/categories/ ✅ INDISPENSABLE
**Rôle:** Envoyer la configuration complète de la simulation
- Liste de toutes les catégories (OS, suite bureautique, stockage, matériel, etc.)
- Pour chaque catégorie, toutes les options disponibles
- Pour chaque option, les impacts (cost, ecology, autonomy, inclusion)

**Réponse exemple:**
```json
[
  {
    "id": 1,
    "name": "Système d'exploitation",
    "description": "Choisissez votre OS",
    "order": 1,
    "options": [
      {
        "id": 1,
        "name": "Windows",
        "description": "OS propriétaire",
        "impact_cost": 100.00,
        "impact_ecology": -20.00,
        "impact_autonomy": -30.00,
        "impact_inclusion": 80.00
      },
      {
        "id": 2,
        "name": "Linux Ubuntu",
        "description": "OS open source",
        "impact_cost": 0.00,
        "impact_ecology": 50.00,
        "impact_autonomy": 70.00,
        "impact_inclusion": 60.00
      }
    ]
  }
]
```

---

### 2. GET /api/quiz/ ✅ INDISPENSABLE
**Rôle:** Récupérer les questions de type vrai/faux pour le quiz

**Réponse exemple:**
```json
[
  {
    "id": 1,
    "question_text": "Le logiciel libre coûte toujours moins cher",
    "is_true": true,
    "explanation": "En général, les logiciels libres n'ont pas de coût de licence"
  }
]
```

---

### 3. GET /api/options/ ⭐ BONUS
**Rôle:** Lister toutes les options, indépendamment des catégories (pour debug/admin)

**Réponse exemple:**
```json
[
  {
    "id": 1,
    "name": "Windows",
    "description": "OS propriétaire",
    "impact_cost": 100.00,
    "impact_ecology": -20.00,
    "impact_autonomy": -30.00,
    "impact_inclusion": 80.00
  }
]
```

---

### 4. POST /api/simulation-runs/ ✅ INDISPENSABLE
**Rôle:** Enregistrer les résultats d'une simulation complétée

**Body à envoyer:**
```json
{
  "score_cost": 450.50,
  "score_ecology": 75.00,
  "score_autonomy": 60.00,
  "score_inclusion": 80.00,
  "choices": {
    "os": "Linux Ubuntu",
    "suite": "LibreOffice",
    "stockage": "Cloud Open Source"
  }
}
```

**Réponse:**
```json
{
  "id": 1,
  "score_cost": 450.50,
  "score_ecology": 75.00,
  "score_autonomy": 60.00,
  "score_inclusion": 80.00,
  "choices": {...},
  "created_at": "2025-12-04T10:30:00Z"
}
```

---

### 5. GET /api/simulation-runs/ ⭐ BONUS
**Rôle:** Récupérer la liste des simulations effectuées (pour stats)

**Paramètres optionnels:**
- `?limit=50` - Limite le nombre de résultats (défaut: 50)

**Réponse:**
```json
[
  {
    "id": 1,
    "score_cost": 450.50,
    "score_ecology": 75.00,
    "score_autonomy": 60.00,
    "score_inclusion": 80.00,
    "choices": {...},
    "created_at": "2025-12-04T10:30:00Z"
  }
]
```

---

### 6. POST /api/ideas/ ✅ TRÈS UTILE
**Rôle:** Permettre aux utilisateurs de proposer des idées

**Body à envoyer:**
```json
{
  "title": "Créer un réseau mesh wifi dans l'école",
  "description": "Pour améliorer la connectivité et réduire les coûts"
}
```

**Réponse:**
```json
{
  "id": 1,
  "title": "Créer un réseau mesh wifi dans l'école",
  "description": "Pour améliorer la connectivité et réduire les coûts",
  "is_approved": false,
  "created_at": "2025-12-04T10:30:00Z",
  "updated_at": "2025-12-04T10:30:00Z"
}
```

---

### 7. GET /api/ideas/ ✅ UTILE POUR LE FRONT
**Rôle:** Récupérer les idées proposées

**Paramètres optionnels:**
- `?approved=true` - Afficher uniquement les idées approuvées

**Réponse:**
```json
[
  {
    "id": 1,
    "title": "Créer un réseau mesh wifi dans l'école",
    "description": "Pour améliorer la connectivité et réduire les coûts",
    "is_approved": true,
    "created_at": "2025-12-04T10:30:00Z",
    "updated_at": "2025-12-04T10:30:00Z"
  }
]
```

---

### 8. PATCH /api/ideas/<id>/ ⭐ BONUS ADMIN
**Rôle:** Modifier/valider une idée (pour admin)

**Body à envoyer:**
```json
{
  "is_approved": true
}
```

Ou pour modifier complètement:
```json
{
  "title": "Nouveau titre",
  "description": "Nouvelle description",
  "is_approved": true
}
```

---

### 9. GET /api/resources/ ⭐ BONUS
**Rôle:** Récupérer les ressources pédagogiques

**Réponse:**
```json
[
  {
    "id": 1,
    "title": "Introduction au logiciel libre",
    "type": "video",
    "url": "https://youtube.com/watch?v=xxx",
    "description": "Une excellente introduction au logiciel libre",
    "created_at": "2025-12-04T10:30:00Z"
  }
]
```

Types disponibles: `video`, `article`, `site`

---

### 10. GET /api/health/ ⭐ BONUS SIMPLISSIME
**Rôle:** Vérifier que le backend fonctionne

**Réponse:**
```json
{
  "status": "ok",
  "message": "NUIT Backend is running"
}
```

---

## Instructions pour déployer et tester

### 1. Installation des dépendances

Vous devez d'abord installer pip si ce n'est pas déjà fait, puis installer les dépendances:

```bash
# Si vous n'avez pas pip
python -m ensurepip --upgrade

# Installer les dépendances
pip install -r requirements.txt
```

### 2. Créer les migrations

```bash
python manage.py makemigrations
```

### 3. Appliquer les migrations

```bash
python manage.py migrate
```

### 4. Créer un super utilisateur (optionnel pour l'admin)

```bash
python manage.py createsuperuser
```

### 5. Lancer le serveur de développement

```bash
python manage.py runserver
```

Le serveur sera accessible sur: `http://127.0.0.1:8000/`

---

## Tests des APIs

### Test avec curl

```bash
# Test health check
curl http://127.0.0.1:8000/api/health/

# Test GET categories
curl http://127.0.0.1:8000/api/categories/

# Test GET quiz
curl http://127.0.0.1:8000/api/quiz/

# Test POST simulation-runs
curl -X POST http://127.0.0.1:8000/api/simulation-runs/ \
  -H "Content-Type: application/json" \
  -d '{"score_cost": 450.50, "score_ecology": 75.00, "score_autonomy": 60.00, "score_inclusion": 80.00, "choices": {"os": "Linux"}}'

# Test POST ideas
curl -X POST http://127.0.0.1:8000/api/ideas/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Mon idée", "description": "Description de mon idée"}'

# Test GET ideas (seulement approuvées)
curl http://127.0.0.1:8000/api/ideas/?approved=true
```

### Test avec Python requests

```python
import requests

# Test health check
response = requests.get('http://127.0.0.1:8000/api/health/')
print(response.json())

# Test POST simulation
data = {
    "score_cost": 450.50,
    "score_ecology": 75.00,
    "score_autonomy": 60.00,
    "score_inclusion": 80.00,
    "choices": {"os": "Linux", "suite": "LibreOffice"}
}
response = requests.post('http://127.0.0.1:8000/api/simulation-runs/', json=data)
print(response.json())
```

---

## Fichiers créés/modifiés

1. **api/models/models.py** - Ajout de 6 nouveaux modèles:
   - Category
   - Option
   - QuizQuestion
   - SimulationRun
   - Idea
   - Resource

2. **api/serializers/serializer_simulation.py** - Nouveau fichier avec tous les serializers

3. **api/views.py** - Ajout de toutes les vues:
   - CategoryListView
   - QuizListView
   - OptionListView
   - SimulationRunViewSet
   - IdeaViewSet
   - ResourceListView
   - health_check

4. **api/urls.py** - Configuration de toutes les routes API

---

## Prochaines étapes

1. Installer pip et les dépendances
2. Créer et appliquer les migrations
3. Créer des données de test dans l'admin Django
4. Tester toutes les APIs localement
5. Valider les résultats des tests
6. Pousser vers GitHub après validation
