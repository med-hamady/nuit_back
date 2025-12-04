"""
Script de test pour toutes les APIs NUIT Backend
Usage: python test_apis.py
"""

import requests
import json

BASE_URL = 'http://127.0.0.1:8000'

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


def test_health():
    """Test GET /api/health/"""
    print("\n\n🔍 TEST 1: Health Check")
    response = requests.get(f'{BASE_URL}/api/health/')
    print_response("GET /api/health/", response)
    return response.status_code == 200


def test_categories():
    """Test GET /api/categories/"""
    print("\n\n🔍 TEST 2: Get Categories")
    response = requests.get(f'{BASE_URL}/api/categories/')
    print_response("GET /api/categories/", response)
    return response.status_code == 200


def test_quiz():
    """Test GET /api/quiz/"""
    print("\n\n🔍 TEST 3: Get Quiz Questions")
    response = requests.get(f'{BASE_URL}/api/quiz/')
    print_response("GET /api/quiz/", response)
    return response.status_code == 200


def test_options():
    """Test GET /api/options/"""
    print("\n\n🔍 TEST 4: Get Options")
    response = requests.get(f'{BASE_URL}/api/options/')
    print_response("GET /api/options/", response)
    return response.status_code == 200


def test_resources():
    """Test GET /api/resources/"""
    print("\n\n🔍 TEST 5: Get Resources")
    response = requests.get(f'{BASE_URL}/api/resources/')
    print_response("GET /api/resources/", response)
    return response.status_code == 200


def test_simulation_runs_get():
    """Test GET /api/simulation-runs/"""
    print("\n\n🔍 TEST 6: Get Simulation Runs")
    response = requests.get(f'{BASE_URL}/api/simulation-runs/')
    print_response("GET /api/simulation-runs/", response)
    return response.status_code == 200


def test_simulation_runs_post():
    """Test POST /api/simulation-runs/"""
    print("\n\n🔍 TEST 7: Create Simulation Run")
    data = {
        "score_cost": 450.50,
        "score_ecology": 75.00,
        "score_autonomy": 60.00,
        "score_inclusion": 80.00,
        "choices": {
            "os": "Linux Ubuntu",
            "suite": "LibreOffice",
            "stockage": "Cloud Open Source",
            "materiel": "Ordinateur reconditionné"
        }
    }
    response = requests.post(f'{BASE_URL}/api/simulation-runs/', json=data)
    print_response("POST /api/simulation-runs/", response)
    return response.status_code == 201


def test_ideas_get():
    """Test GET /api/ideas/"""
    print("\n\n🔍 TEST 8: Get Ideas")
    response = requests.get(f'{BASE_URL}/api/ideas/')
    print_response("GET /api/ideas/", response)

    print("\n🔍 TEST 8b: Get Approved Ideas Only")
    response2 = requests.get(f'{BASE_URL}/api/ideas/?approved=true')
    print_response("GET /api/ideas/?approved=true", response2)

    return response.status_code == 200


def test_ideas_post():
    """Test POST /api/ideas/"""
    print("\n\n🔍 TEST 9: Create Idea")
    data = {
        "title": "Créer un réseau mesh wifi dans l'établissement",
        "description": "Mettre en place un réseau mesh pour améliorer la connectivité et réduire les coûts d'infrastructure"
    }
    response = requests.post(f'{BASE_URL}/api/ideas/', json=data)
    print_response("POST /api/ideas/", response)

    # Retourner l'ID de l'idée créée pour le test PATCH
    if response.status_code == 201:
        return response.json().get('id')
    return None


def test_ideas_patch(idea_id):
    """Test PATCH /api/ideas/<id>/"""
    if idea_id is None:
        print("\n⚠️  TEST 10: Skipped (no idea ID)")
        return False

    print("\n\n🔍 TEST 10: Update Idea (Approve)")
    data = {
        "is_approved": True
    }
    response = requests.patch(f'{BASE_URL}/api/ideas/{idea_id}/', json=data)
    print_response(f"PATCH /api/ideas/{idea_id}/", response)
    return response.status_code == 200


def run_all_tests():
    """Exécuter tous les tests"""
    print("\n" + "="*60)
    print("🚀 DÉMARRAGE DES TESTS - NUIT Backend APIs")
    print("="*60)

    results = {}

    # Tests GET simples
    results['Health Check'] = test_health()
    results['Categories'] = test_categories()
    results['Quiz'] = test_quiz()
    results['Options'] = test_options()
    results['Resources'] = test_resources()
    results['Simulation Runs GET'] = test_simulation_runs_get()
    results['Ideas GET'] = test_ideas_get()

    # Tests POST
    results['Simulation Runs POST'] = test_simulation_runs_post()
    idea_id = test_ideas_post()
    results['Ideas POST'] = idea_id is not None

    # Test PATCH
    results['Ideas PATCH'] = test_ideas_patch(idea_id)

    # Résumé
    print("\n\n" + "="*60)
    print("📊 RÉSUMÉ DES TESTS")
    print("="*60)

    passed = 0
    failed = 0

    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name:.<40} {status}")
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


if __name__ == "__main__":
    try:
        run_all_tests()
    except requests.exceptions.ConnectionError:
        print("\n❌ ERREUR: Impossible de se connecter au serveur")
        print("Assurez-vous que le serveur Django est lancé:")
        print("  python manage.py runserver")
    except Exception as e:
        print(f"\n❌ ERREUR: {str(e)}")
