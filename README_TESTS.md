# Guide de Test - NUIT Backend APIs

## 🚀 Étapes pour tester les APIs localement

### 1️⃣ Installation de l'environnement

#### Installer pip (si nécessaire)
```bash
python -m ensurepip --upgrade
```

#### Installer les dépendances
```bash
pip install -r requirements.txt
```

### 2️⃣ Configuration de la base de données

#### Créer les migrations
```bash
python manage.py makemigrations
```

#### Appliquer les migrations
```bash
python manage.py migrate
```

### 3️⃣ Créer un super utilisateur (pour accéder à l'admin)

```bash
python manage.py createsuperuser
```

Suivez les instructions pour créer votre compte admin.

### 4️⃣ Créer les données de test

Ouvrez le shell Django:
```bash
python manage.py shell
```

Puis copiez-collez le contenu du fichier `create_test_data.py` dans le shell.

Ou plus simplement:
```bash
python manage.py shell < create_test_data.py
```

Cela va créer:
- 5 catégories (OS, Suite bureautique, Stockage, Matériel, Connectivité)
- 15 options avec leurs impacts
- 8 questions de quiz
- 5 ressources pédagogiques

### 5️⃣ Lancer le serveur de développement

```bash
python manage.py runserver
```

Le serveur sera accessible sur: **http://127.0.0.1:8000/**

### 6️⃣ Accéder à l'interface d'administration

Ouvrez votre navigateur et allez sur:
**http://127.0.0.1:8000/admin/**

Connectez-vous avec le super utilisateur créé à l'étape 3.

Vous pourrez:
- Voir toutes les données créées
- Ajouter/modifier des catégories, options, questions, etc.
- Approuver les idées soumises par les utilisateurs
- Voir les statistiques des simulations

### 7️⃣ Tester les APIs

#### Option A: Script de test automatique

Dans un nouveau terminal (pendant que le serveur tourne):
```bash
python test_apis.py
```

Ce script va tester automatiquement toutes les APIs et afficher les résultats.

#### Option B: Test manuel avec curl

```bash
# Test health check
curl http://127.0.0.1:8000/api/health/

# Test categories
curl http://127.0.0.1:8000/api/categories/

# Test quiz
curl http://127.0.0.1:8000/api/quiz/

# Test options
curl http://127.0.0.1:8000/api/options/

# Test resources
curl http://127.0.0.1:8000/api/resources/

# Test POST simulation
curl -X POST http://127.0.0.1:8000/api/simulation-runs/ \
  -H "Content-Type: application/json" \
  -d '{"score_cost":450.50,"score_ecology":75.00,"score_autonomy":60.00,"score_inclusion":80.00,"choices":{"os":"Linux"}}'

# Test POST idea
curl -X POST http://127.0.0.1:8000/api/ideas/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Mon idée","description":"Description de mon idée"}'
```

#### Option C: Test avec navigateur

Ouvrez votre navigateur et testez ces URLs:
- http://127.0.0.1:8000/api/health/
- http://127.0.0.1:8000/api/categories/
- http://127.0.0.1:8000/api/quiz/
- http://127.0.0.1:8000/api/options/
- http://127.0.0.1:8000/api/resources/
- http://127.0.0.1:8000/api/simulation-runs/
- http://127.0.0.1:8000/api/ideas/

## 📋 Liste des APIs disponibles

| Méthode | Endpoint | Description | Priorité |
|---------|----------|-------------|----------|
| GET | /api/health/ | Health check | ⭐ BONUS |
| GET | /api/categories/ | Configuration simulation | ✅ INDISPENSABLE |
| GET | /api/quiz/ | Questions quiz | ✅ INDISPENSABLE |
| GET | /api/options/ | Liste toutes les options | ⭐ BONUS |
| GET | /api/resources/ | Ressources pédagogiques | ⭐ BONUS |
| POST | /api/simulation-runs/ | Enregistrer résultat | ✅ INDISPENSABLE |
| GET | /api/simulation-runs/ | Liste des simulations | ⭐ BONUS |
| POST | /api/ideas/ | Proposer une idée | ✅ TRÈS UTILE |
| GET | /api/ideas/ | Liste des idées | ✅ UTILE |
| PATCH | /api/ideas/:id/ | Valider une idée (admin) | ⭐ BONUS |

## ✅ Checklist de validation

Avant de valider et pousser vers GitHub, vérifiez:

- [ ] Le serveur Django démarre sans erreur
- [ ] L'interface admin est accessible
- [ ] Les données de test sont créées
- [ ] GET /api/health/ retourne {"status": "ok"}
- [ ] GET /api/categories/ retourne les catégories avec leurs options
- [ ] GET /api/quiz/ retourne les questions
- [ ] POST /api/simulation-runs/ enregistre correctement
- [ ] POST /api/ideas/ crée une nouvelle idée
- [ ] GET /api/ideas/ liste les idées
- [ ] PATCH /api/ideas/:id/ permet de modifier/approuver
- [ ] Toutes les APIs retournent du JSON valide
- [ ] Pas d'erreurs dans la console du serveur

## 🐛 Résolution de problèmes

### Erreur: No module named 'django'
```bash
pip install -r requirements.txt
```

### Erreur: mysqlclient connection
Vérifiez que MySQL est accessible et que les credentials dans `settings.py` sont corrects.

### Erreur: migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Port 8000 déjà utilisé
```bash
python manage.py runserver 8080
```

## 📝 Notes importantes

1. **Base de données**: Le projet est configuré pour utiliser MySQL. Les credentials sont dans `project/settings.py`.

2. **CORS**: Le CORS est configuré pour accepter toutes les origines (`CORS_ORIGIN_ALLOW_ALL = True`). En production, vous devrez le restreindre.

3. **Debug mode**: `DEBUG = True` dans settings.py. À désactiver en production.

4. **Données de test**: Les données créées par `create_test_data.py` peuvent être supprimées et recréées à tout moment.

## 📚 Documentation complète

Consultez [API_DOCUMENTATION.md](API_DOCUMENTATION.md) pour la documentation complète de toutes les APIs avec des exemples détaillés.

## 🎉 Prêt pour le déploiement

Une fois tous les tests validés, vous pourrez:
1. Créer un commit avec toutes les modifications
2. Pousser vers GitHub
3. Déployer sur votre serveur de production
