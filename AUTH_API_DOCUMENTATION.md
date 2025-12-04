# Documentation des APIs d'Authentification

## Nouvelles APIs ajoutées

### 1. POST /api/auth/register/ - Inscription
**Rôle:** Créer un nouveau compte utilisateur

**Body à envoyer:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "motdepasse123",
  "password_confirm": "motdepasse123",
  "first_name": "John",
  "last_name": "Doe",
  "telephone": 123456789
}
```

**Champs requis:**
- `username` (unique)
- `email` (unique)
- `password` (minimum 6 caractères)
- `password_confirm` (doit correspondre au password)
- `telephone` (unique, format numérique)

**Champs optionnels:**
- `first_name`
- `last_name`

**Réponse (201 Created):**
```json
{
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "telephone": 123456789,
    "is_staff": false,
    "is_active": true,
    "date_joined": "2025-12-04T10:30:00Z",
    "last_login": null
  },
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
  "message": "Inscription réussie"
}
```

**Erreurs possibles:**
```json
// Mots de passe différents
{
  "password": ["Les mots de passe ne correspondent pas"]
}

// Username déjà utilisé
{
  "username": ["A user with that username already exists."]
}

// Email déjà utilisé
{
  "email": ["new user with this email address already exists."]
}
```

---

### 2. POST /api/auth/login/ - Connexion
**Rôle:** Se connecter avec un compte existant

**Body à envoyer:**
```json
{
  "username": "john_doe",
  "password": "motdepasse123"
}
```

**Réponse (200 OK):**
```json
{
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "telephone": 123456789,
    "is_staff": false,
    "is_active": true,
    "date_joined": "2025-12-04T10:30:00Z",
    "last_login": "2025-12-04T11:00:00Z"
  },
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
  "message": "Connexion réussie"
}
```

**Erreurs possibles:**
```json
// Identifiants incorrects
{
  "non_field_errors": ["Nom d'utilisateur ou mot de passe incorrect"]
}

// Compte désactivé
{
  "non_field_errors": ["Ce compte est désactivé"]
}
```

---

### 3. GET /api/auth/me/ - Profil utilisateur
**Rôle:** Récupérer les informations de l'utilisateur connecté

**Headers requis:**
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Réponse (200 OK):**
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "telephone": 123456789,
  "is_staff": false,
  "is_active": true,
  "date_joined": "2025-12-04T10:30:00Z",
  "last_login": "2025-12-04T11:00:00Z"
}
```

**Erreur (401 Unauthorized):**
```json
{
  "error": "Non authentifié"
}
```

---

## Mise à jour: Quiz avec resource_url

### GET /api/quiz/ - Maintenant avec resource_url

**Nouvelle réponse:**
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
    "explanation": "Linux est aussi adapté au milieu éducatif",
    "resource_url": null
  }
]
```

Le champ `resource_url` est optionnel et peut contenir un lien vers une ressource pédagogique liée à la question.

---

## Utilisation du Token d'authentification

Une fois connecté ou inscrit, vous recevez un token. Utilisez-le dans vos requêtes pour les endpoints protégés:

### Avec curl:
```bash
curl -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" \
  http://127.0.0.1:8000/api/auth/me/
```

### Avec Postman:
1. Aller dans l'onglet "Headers"
2. Ajouter:
   - Key: `Authorization`
   - Value: `Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b`

### Avec JavaScript (fetch):
```javascript
fetch('http://127.0.0.1:8000/api/auth/me/', {
  headers: {
    'Authorization': 'Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
  }
})
.then(response => response.json())
.then(data => console.log(data));
```

---

## Tests avec Postman

### Test 1: Register
```
Method: POST
URL: http://127.0.0.1:8000/api/auth/register/
Headers:
  Content-Type: application/json
Body (raw JSON):
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "password123",
  "password_confirm": "password123",
  "first_name": "Test",
  "last_name": "User",
  "telephone": 987654321
}
```

### Test 2: Login
```
Method: POST
URL: http://127.0.0.1:8000/api/auth/login/
Headers:
  Content-Type: application/json
Body (raw JSON):
{
  "username": "testuser",
  "password": "password123"
}
```

### Test 3: Get Profile
```
Method: GET
URL: http://127.0.0.1:8000/api/auth/me/
Headers:
  Authorization: Token [VOTRE_TOKEN_ICI]
```

### Test 4: Quiz avec resource_url
```
Method: GET
URL: http://127.0.0.1:8000/api/quiz/
```

---

## Migration nécessaire

Après avoir activé l'environnement virtuel, exécutez:

```bash
python manage.py makemigrations
python manage.py migrate
```

Cela créera la nouvelle colonne `resource_url` dans la table `QUIZ_QUESTIONS`.

---

## Résumé des changements

### Nouveaux fichiers:
- `api/serializers/serializer_auth.py` - Serializers pour auth
- `AUTH_API_DOCUMENTATION.md` - Cette documentation

### Fichiers modifiés:
- `api/models/models.py` - Ajout de `resource_url` à QuizQuestion
- `api/serializers/serializer_simulation.py` - Ajout de `resource_url` dans QuizQuestionSerializer
- `api/views.py` - Ajout de RegisterView, LoginView, user_profile
- `api/urls.py` - Ajout des routes auth

### Nouvelles APIs:
1. POST /api/auth/register/ - Inscription
2. POST /api/auth/login/ - Connexion
3. GET /api/auth/me/ - Profil (nécessite authentification)

### APIs mises à jour:
1. GET /api/quiz/ - Maintenant retourne aussi `resource_url`
