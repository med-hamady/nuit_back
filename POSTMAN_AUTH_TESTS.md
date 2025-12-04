# Tests Postman - APIs d'Authentification

## 🚀 Guide de test complet avec Postman

### Prérequis
1. Le serveur doit être lancé: `python manage.py runserver`
2. Les migrations doivent être faites: `python manage.py makemigrations && python manage.py migrate`

---

## Test 1: Register (Inscription) ✅ INDISPENSABLE

### Configuration Postman:
```
Method: POST
URL: http://127.0.0.1:8000/api/auth/register/
```

### Headers:
```
Content-Type: application/json
```

### Body (raw JSON):
```json
{
  "username": "testuser2024",
  "email": "test2024@example.com",
  "password": "password123",
  "password_confirm": "password123",
  "first_name": "Jean",
  "last_name": "Dupont",
  "telephone": 612345678
}
```

### Résultat attendu (201 Created):
```json
{
  "user": {
    "id": 2,
    "username": "testuser2024",
    "email": "test2024@example.com",
    "first_name": "Jean",
    "last_name": "Dupont",
    "telephone": 612345678,
    "is_staff": false,
    "is_active": true,
    "date_joined": "2025-12-04T...",
    "last_login": null
  },
  "token": "abc123def456...",
  "message": "Inscription réussie"
}
```

**⚠️ IMPORTANT:** Copiez le token reçu, vous en aurez besoin pour Test 3!

---

## Test 2: Login (Connexion) ✅ INDISPENSABLE

### Configuration Postman:
```
Method: POST
URL: http://127.0.0.1:8000/api/auth/login/
```

### Headers:
```
Content-Type: application/json
```

### Body (raw JSON):
```json
{
  "username": "testuser2024",
  "password": "password123"
}
```

### Résultat attendu (200 OK):
```json
{
  "user": {
    "id": 2,
    "username": "testuser2024",
    "email": "test2024@example.com",
    "first_name": "Jean",
    "last_name": "Dupont",
    "telephone": 612345678,
    "is_staff": false,
    "is_active": true,
    "date_joined": "2025-12-04T...",
    "last_login": "2025-12-04T..."
  },
  "token": "abc123def456...",
  "message": "Connexion réussie"
}
```

**⚠️ IMPORTANT:** Copiez le token reçu!

---

## Test 3: Get User Profile (Profil utilisateur) ⭐ BONUS

### Configuration Postman:
```
Method: GET
URL: http://127.0.0.1:8000/api/auth/me/
```

### Headers:
```
Authorization: Token abc123def456...
```

**IMPORTANT:** Remplacez `abc123def456...` par le token reçu aux Tests 1 ou 2.

### Résultat attendu (200 OK):
```json
{
  "id": 2,
  "username": "testuser2024",
  "email": "test2024@example.com",
  "first_name": "Jean",
  "last_name": "Dupont",
  "telephone": 612345678,
  "is_staff": false,
  "is_active": true,
  "date_joined": "2025-12-04T...",
  "last_login": "2025-12-04T..."
}
```

### Test sans token (devrait échouer - 401):
Essayez la même requête SANS le header Authorization:
```json
{
  "error": "Non authentifié"
}
```

---

## Test 4: Quiz avec resource_url ✅ MISE À JOUR

### Configuration Postman:
```
Method: GET
URL: http://127.0.0.1:8000/api/quiz/
```

### Résultat attendu (200 OK):
```json
[
  {
    "id": 1,
    "question_text": "Le logiciel libre est toujours gratuit",
    "is_true": true,
    "explanation": "Les logiciels libres peuvent être utilisés gratuitement",
    "resource_url": "https://www.gnu.org/philosophy/free-sw.html"
  },
  {
    "id": 2,
    "question_text": "Windows est le seul OS pour l'éducation",
    "is_true": false,
    "explanation": "Linux est aussi adapté",
    "resource_url": null
  }
]
```

**Nouveau champ:** `resource_url` - URL optionnelle vers une ressource pédagogique

---

## Tests d'erreurs (pour validation)

### Test 5: Register avec mots de passe différents
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "password123",
  "password_confirm": "differentpassword",
  "telephone": 123456789
}
```

**Résultat (400 Bad Request):**
```json
{
  "password": ["Les mots de passe ne correspondent pas"]
}
```

---

### Test 6: Register avec username déjà existant
```json
{
  "username": "testuser2024",
  "email": "autre@example.com",
  "password": "password123",
  "password_confirm": "password123",
  "telephone": 987654321
}
```

**Résultat (400 Bad Request):**
```json
{
  "username": ["A user with that username already exists."]
}
```

---

### Test 7: Login avec mauvais credentials
```json
{
  "username": "wronguser",
  "password": "wrongpassword"
}
```

**Résultat (400 Bad Request):**
```json
{
  "non_field_errors": ["Nom d'utilisateur ou mot de passe incorrect"]
}
```

---

## 📋 Checklist de validation

- [ ] Register fonctionne avec données valides (201)
- [ ] Register retourne un token
- [ ] Register échoue avec mots de passe différents (400)
- [ ] Register échoue avec username existant (400)
- [ ] Login fonctionne avec credentials valides (200)
- [ ] Login retourne un token
- [ ] Login échoue avec mauvais credentials (400)
- [ ] Profile fonctionne avec token (200)
- [ ] Profile échoue sans token (401)
- [ ] Quiz retourne le champ resource_url

---

## 💡 Conseils Postman

### 1. Créer une variable d'environnement pour le token
1. Aller dans "Environments"
2. Créer un nouvel environnement "NUIT Backend"
3. Ajouter une variable `token`
4. Dans les tests du register/login, ajouter ce script:
```javascript
pm.environment.set("token", pm.response.json().token);
```
5. Dans les headers, utiliser: `Authorization: Token {{token}}`

### 2. Créer une collection Postman
Organisez vos requêtes dans une collection:
```
NUIT Backend APIs
├── Authentication
│   ├── Register
│   ├── Login
│   └── Get Profile
├── Simulation
│   ├── Get Categories
│   ├── Get Quiz
│   ├── Post Simulation Run
│   └── ...
└── Ideas
    ├── Get Ideas
    ├── Post Ideas
    └── ...
```

---

## 🔄 Workflow complet avec Postman

1. **Register** → Copier le token
2. **Login** → Vérifier que le token fonctionne
3. **Get Profile** → Utiliser le token dans le header
4. **Tester les autres APIs** (categories, quiz, etc.)
5. **Poster une simulation** avec les données du joueur
6. **Poster une idée**

---

## 🎯 Résumé des endpoints Auth

| Méthode | Endpoint | Auth requise | Description |
|---------|----------|--------------|-------------|
| POST | /api/auth/register/ | Non | Créer un compte |
| POST | /api/auth/login/ | Non | Se connecter |
| GET | /api/auth/me/ | Oui (Token) | Voir son profil |

---

## 🚀 Script de test automatique

Si vous préférez tester automatiquement:

```bash
python test_auth_apis.py
```

Ce script teste automatiquement toutes les APIs d'authentification.
