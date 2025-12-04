# Changelog - NUIT Backend

## Version 2.0 - 2025-12-04

### ✨ Nouvelles fonctionnalités

#### APIs d'Authentification
- ✅ **POST /api/auth/register/** - Inscription de nouveaux utilisateurs
  - Création de compte avec username, email, password
  - Génération automatique de token d'authentification
  - Validation des mots de passe (doivent correspondre)
  - Vérification de l'unicité (username, email, téléphone)

- ✅ **POST /api/auth/login/** - Connexion des utilisateurs
  - Authentification par username et password
  - Retour du token d'authentification
  - Gestion des erreurs (credentials incorrects, compte désactivé)

- ✅ **GET /api/auth/me/** - Profil utilisateur (protégé)
  - Récupération des informations de l'utilisateur connecté
  - Nécessite un token d'authentification dans le header
  - Retourne toutes les infos du profil

#### Amélioration du Quiz
- ✅ Ajout du champ **`resource_url`** au modèle QuizQuestion
  - Permet d'associer une ressource pédagogique à chaque question
  - Champ optionnel (peut être null)
  - Type: URLField pour validation automatique
  - Visible dans l'API GET /api/quiz/

---

### 📁 Fichiers créés

1. **api/serializers/serializer_auth.py**
   - RegisterSerializer - Validation et création de compte
   - LoginSerializer - Validation des credentials
   - UserSerializer - Sérialisation des données utilisateur

2. **AUTH_API_DOCUMENTATION.md**
   - Documentation complète des APIs d'authentification
   - Exemples de requêtes et réponses
   - Gestion des erreurs
   - Utilisation du token

3. **test_auth_apis.py**
   - Script Python pour tester automatiquement les APIs auth
   - 7 tests automatisés
   - Génération de rapports de tests

4. **POSTMAN_AUTH_TESTS.md**
   - Guide complet pour tester avec Postman
   - Exemples de requêtes
   - Checklist de validation
   - Tests d'erreurs

5. **CHANGELOG.md**
   - Ce fichier - historique des modifications

---

### 🔧 Fichiers modifiés

1. **api/models/models.py**
   - Ajout du champ `resource_url` à la classe QuizQuestion
   ```python
   resource_url = models.URLField(blank=True, null=True,
                                  help_text="URL vers une ressource pédagogique")
   ```

2. **api/serializers/serializer_simulation.py**
   - Ajout de `resource_url` dans QuizQuestionSerializer
   ```python
   fields = ['id', 'question_text', 'is_true', 'explanation', 'resource_url']
   ```

3. **api/views.py**
   - Import de Token et authentification Django
   - Ajout de RegisterView (APIView)
   - Ajout de LoginView (APIView)
   - Ajout de user_profile (function-based view)

4. **api/urls.py**
   - Ajout des routes d'authentification:
     - `api/auth/register/`
     - `api/auth/login/`
     - `api/auth/me/`

---

### 🗄️ Changements de base de données

#### Table QUIZ_QUESTIONS
```sql
ALTER TABLE QUIZ_QUESTIONS ADD COLUMN resource_url VARCHAR(200) NULL;
```

**Migration requise:**
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 📊 Statistiques

**Lignes de code ajoutées:** ~400
**Nouveaux fichiers:** 5
**Fichiers modifiés:** 4
**Nouvelles APIs:** 3
**APIs modifiées:** 1 (quiz)

---

### 🎯 Fonctionnalités complètes du backend

#### Authentification
- ✅ Inscription (register)
- ✅ Connexion (login)
- ✅ Profil utilisateur (me)
- ✅ Token-based authentication

#### Simulation
- ✅ GET /api/categories/ - Configuration complète
- ✅ GET /api/options/ - Toutes les options
- ✅ POST /api/simulation-runs/ - Enregistrer résultats
- ✅ GET /api/simulation-runs/ - Liste des simulations

#### Quiz
- ✅ GET /api/quiz/ - Questions avec resource_url
- ✅ Support vrai/faux
- ✅ Explications
- ✅ Liens vers ressources pédagogiques

#### Idées
- ✅ POST /api/ideas/ - Proposer une idée
- ✅ GET /api/ideas/ - Liste des idées
- ✅ PATCH /api/ideas/:id/ - Valider/modifier (admin)
- ✅ Filtrage par statut d'approbation

#### Ressources
- ✅ GET /api/resources/ - Ressources pédagogiques
- ✅ Support video, article, site

#### Système
- ✅ GET /api/health/ - Health check
- ✅ Interface admin complète
- ✅ Logging des requêtes API

---

### 🔐 Sécurité

**Token Authentication:**
- Utilisation de Django REST Framework Token Authentication
- Tokens générés automatiquement à l'inscription/connexion
- Stockage sécurisé dans la table `authtoken_token`
- Validation automatique sur les endpoints protégés

**Validation des données:**
- Mots de passe minimum 6 caractères
- Vérification de correspondance des mots de passe
- Validation des emails
- Unicité garantie (username, email, téléphone)

**Endpoints protégés:**
- GET /api/auth/me/ nécessite un token
- Autres endpoints publics (pour l'instant)

---

### 📝 Documentation

**Guides disponibles:**
1. API_DOCUMENTATION.md - Documentation des APIs de simulation
2. AUTH_API_DOCUMENTATION.md - Documentation des APIs d'authentification
3. README_TESTS.md - Guide de test complet
4. POSTMAN_AUTH_TESTS.md - Tests spécifiques Postman
5. IMPLEMENTATION_SUMMARY.md - Résumé de l'implémentation
6. QUICK_START.txt - Démarrage rapide
7. CHANGELOG.md - Historique des modifications

**Scripts de test:**
1. test_apis.py - Tests automatiques généraux
2. test_auth_apis.py - Tests automatiques auth
3. create_test_data.py - Création de données de test

---

### 🚀 Prochaines étapes

Pour déployer ces changements:

1. **Activer l'environnement virtuel**
   ```bash
   venv\Scripts\Activate.ps1
   ```

2. **Créer et appliquer les migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Tester les nouvelles APIs**
   ```bash
   python test_auth_apis.py
   ```

4. **Valider avec Postman**
   - Suivre le guide POSTMAN_AUTH_TESTS.md

5. **Commit et push vers GitHub**
   - Une fois tous les tests validés

---

### ⚠️ Breaking Changes

Aucun breaking change. Toutes les APIs existantes restent compatibles.

**Note:** Le champ `resource_url` est optionnel dans QuizQuestion, donc les données existantes ne seront pas affectées.

---

### 🐛 Corrections de bugs

Aucune correction de bug dans cette version (nouvelles fonctionnalités uniquement).

---

### 📞 Support

Pour toute question ou problème:
1. Consulter la documentation appropriée
2. Vérifier les logs du serveur Django
3. Tester avec les scripts automatisés
4. Utiliser Postman pour déboguer les requêtes

---

**Version précédente:** 1.0 (10 APIs de simulation)
**Version actuelle:** 2.0 (13 APIs + authentification complète)
