"""
Script de test pour les APIs d'authentification
Usage: python test_auth_apis.py
"""

import requests
import json
import random

BASE_URL = 'http://127.0.0.1:8000'

# Variable globale pour stocker le token
TOKEN = None


def print_response(title, response):
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    except:
        print(f"Response: {response.text}")
    print()


def test_register():
    """Test POST /api/auth/register/"""
    global TOKEN
    print("\n\n🔍 TEST 1: Register (Inscription)")

    # Générer un username unique
    random_num = random.randint(1000, 9999)

    data = {
        "username": f"testuser_{random_num}",
        "email": f"test{random_num}@example.com",
        "password": "password123",
        "password_confirm": "password123",
        "first_name": "Test",
        "last_name": "User",
        "telephone": random.randint(100000000, 999999999)
    }

    response = requests.post(f'{BASE_URL}/api/auth/register/', json=data)
    print_response("POST /api/auth/register/", response)

    if response.status_code == 201:
        TOKEN = response.json().get('token')
        print(f"✅ Token reçu: {TOKEN[:20]}...")
        return True, data['username']
    return False, None


def test_login(username):
    """Test POST /api/auth/login/"""
    global TOKEN
    print("\n\n🔍 TEST 2: Login (Connexion)")

    data = {
        "username": username,
        "password": "password123"
    }

    response = requests.post(f'{BASE_URL}/api/auth/login/', json=data)
    print_response("POST /api/auth/login/", response)

    if response.status_code == 200:
        TOKEN = response.json().get('token')
        print(f"✅ Token reçu: {TOKEN[:20]}...")
        return True
    return False


def test_user_profile():
    """Test GET /api/auth/me/"""
    print("\n\n🔍 TEST 3: User Profile (avec token)")

    if not TOKEN:
        print("❌ Pas de token disponible")
        return False

    headers = {
        'Authorization': f'Token {TOKEN}'
    }

    response = requests.get(f'{BASE_URL}/api/auth/me/', headers=headers)
    print_response("GET /api/auth/me/ (authenticated)", response)

    return response.status_code == 200


def test_user_profile_without_token():
    """Test GET /api/auth/me/ sans token"""
    print("\n\n🔍 TEST 4: User Profile (sans token - devrait échouer)")

    response = requests.get(f'{BASE_URL}/api/auth/me/')
    print_response("GET /api/auth/me/ (unauthenticated)", response)

    return response.status_code == 401


def test_login_wrong_credentials():
    """Test login avec mauvais credentials"""
    print("\n\n🔍 TEST 5: Login avec mauvais mot de passe (devrait échouer)")

    data = {
        "username": "wronguser",
        "password": "wrongpassword"
    }

    response = requests.post(f'{BASE_URL}/api/auth/login/', json=data)
    print_response("POST /api/auth/login/ (wrong credentials)", response)

    return response.status_code == 400


def test_register_duplicate():
    """Test register avec username existant"""
    print("\n\n🔍 TEST 6: Register avec username existant (devrait échouer)")

    data = {
        "username": "admin",
        "email": "admin@example.com",
        "password": "password123",
        "password_confirm": "password123",
        "first_name": "Admin",
        "last_name": "User",
        "telephone": 111111111
    }

    response = requests.post(f'{BASE_URL}/api/auth/register/', json=data)
    print_response("POST /api/auth/register/ (duplicate username)", response)

    return response.status_code == 400


def test_quiz_with_resource_url():
    """Test GET /api/quiz/ pour vérifier le champ resource_url"""
    print("\n\n🔍 TEST 7: Quiz avec resource_url")

    response = requests.get(f'{BASE_URL}/api/quiz/')
    print_response("GET /api/quiz/ (avec resource_url)", response)

    if response.status_code == 200:
        data = response.json()
        if len(data) > 0:
            # Vérifier que resource_url existe dans la réponse
            has_resource_url = 'resource_url' in data[0]
            print(f"✅ Champ 'resource_url' présent: {has_resource_url}")
            return has_resource_url
        else:
            print("⚠️  Aucune question de quiz dans la base")
            return True
    return False


def run_all_tests():
    """Exécuter tous les tests"""
    print("\n" + "="*60)
    print("🚀 DÉMARRAGE DES TESTS - APIs d'Authentification")
    print("="*60)

    results = {}

    # Test d'inscription
    success, username = test_register()
    results['Register'] = success

    # Test de login (avec le username créé)
    if username:
        results['Login'] = test_login(username)
    else:
        results['Login'] = False

    # Test profil avec token
    results['Profile (with token)'] = test_user_profile()

    # Test profil sans token
    results['Profile (without token)'] = test_user_profile_without_token()

    # Tests d'erreurs
    results['Login (wrong credentials)'] = test_login_wrong_credentials()
    results['Register (duplicate)'] = test_register_duplicate()

    # Test quiz avec resource_url
    results['Quiz with resource_url'] = test_quiz_with_resource_url()

    # Résumé
    print("\n\n" + "="*60)
    print("📊 RÉSUMÉ DES TESTS D'AUTHENTIFICATION")
    print("="*60)

    passed = 0
    failed = 0

    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name:.<45} {status}")
        if result:
            passed += 1
        else:
            failed += 1

    print("\n" + "="*60)
    print(f"Total: {passed + failed} tests")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print("="*60)

    if failed == 0:
        print("\n🎉 Tous les tests sont passés avec succès!")
    else:
        print(f"\n⚠️  {failed} test(s) ont échoué. Vérifiez les détails ci-dessus.")

    if TOKEN:
        print(f"\n🔑 Token final: {TOKEN}")
        print("Vous pouvez utiliser ce token pour tester les endpoints protégés dans Postman:")
        print(f"  Header: Authorization: Token {TOKEN}")


if __name__ == "__main__":
    try:
        run_all_tests()
    except requests.exceptions.ConnectionError:
        print("\n❌ ERREUR: Impossible de se connecter au serveur")
        print("Assurez-vous que le serveur Django est lancé:")
        print("  python manage.py runserver")
    except Exception as e:
        print(f"\n❌ ERREUR: {str(e)}")
