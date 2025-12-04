"""
Script pour charger les données NUID dans la base de données
Usage: python manage.py shell < load_nuid_data.py
Ou: python manage.py shell
    exec(open('load_nuid_data.py').read())
"""

from api.models.models import Category, Option, QuizQuestion, Resource

print("🗑️  Nettoyage des données existantes...")
Category.objects.all().delete()
QuizQuestion.objects.all().delete()
Resource.objects.all().delete()

print("\n📦 Création des catégories...")

# Catégories
cat1 = Category.objects.create(
    id=1,
    name="Système d'exploitation",
    description="Choisissez le système d'exploitation pour les ordinateurs.",
    order=1
)

cat2 = Category.objects.create(
    id=2,
    name="Suite bureautique",
    description="Choisissez la suite bureautique pour les PC.",
    order=2
)

cat3 = Category.objects.create(
    id=3,
    name="Stockage des données",
    description="Choisissez où stocker les données de l'école.",
    order=3
)

cat4 = Category.objects.create(
    id=4,
    name="Matériel informatique",
    description="Choisissez le matériel informatique à utiliser dans l'école.",
    order=4
)

cat5 = Category.objects.create(
    id=5,
    name="Réutilisation / Écologie",
    description="Solutions pour réduire l'impact environnemental et réutiliser les ressources.",
    order=5
)

print(f"✅ {Category.objects.count()} catégories créées")

print("\n📋 Création des options...")

# Options pour Catégorie 1: Système d'exploitation
Option.objects.create(
    id=1,
    category=cat1,
    name="Acheter 50 nouveaux PC sous Windows 11",
    description="Solution classique mais coûteuse et peu durable.",
    impact_cost=5,
    impact_ecology=-4,
    impact_autonomy=-3,
    impact_inclusion=-1
)

Option.objects.create(
    id=2,
    category=cat1,
    name="Installer Linux sur les anciens PC",
    description="Réutiliser le matériel existant.",
    impact_cost=-4,
    impact_ecology=5,
    impact_autonomy=4,
    impact_inclusion=2
)

# Options pour Catégorie 2: Suite bureautique
Option.objects.create(
    id=3,
    category=cat2,
    name="Microsoft Office (licences payantes annuelles)",
    description="Solution propriétaire et payante.",
    impact_cost=5,
    impact_ecology=-3,
    impact_autonomy=-2,
    impact_inclusion=-2
)

Option.objects.create(
    id=4,
    category=cat2,
    name="LibreOffice (logiciel libre et gratuit)",
    description="Solution libre et gratuite.",
    impact_cost=-5,
    impact_ecology=4,
    impact_autonomy=5,
    impact_inclusion=3
)

# Options pour Catégorie 3: Stockage des données
Option.objects.create(
    id=5,
    category=cat3,
    name="Cloud d'une grande entreprise (USA)",
    description="Stockage chez une grande entreprise numérique.",
    impact_cost=3,
    impact_ecology=-5,
    impact_autonomy=-4,
    impact_inclusion=-3
)

Option.objects.create(
    id=6,
    category=cat3,
    name="Hébergeur européen / solution locale",
    description="Solutions locales ou européennes respectant les données.",
    impact_cost=-3,
    impact_ecology=5,
    impact_autonomy=4,
    impact_inclusion=5
)

# Options pour Catégorie 4: Matériel informatique
Option.objects.create(
    id=7,
    category=cat4,
    name="Acheter des PC neufs avec des processeurs puissants",
    description="Des PC de haute performance pour les salles de classe.",
    impact_cost=5,
    impact_ecology=-5,
    impact_autonomy=-2,
    impact_inclusion=-3
)

Option.objects.create(
    id=8,
    category=cat4,
    name="Réutiliser des PC reconditionnés",
    description="Réutiliser des équipements anciens pour économiser de l'argent et réduire l'impact écologique.",
    impact_cost=-4,
    impact_ecology=5,
    impact_autonomy=3,
    impact_inclusion=4
)

# Options pour Catégorie 5: Réutilisation / Écologie
Option.objects.create(
    id=9,
    category=cat5,
    name="Réparer les anciens équipements",
    description="Prolonger la vie des ordinateurs existants en remplaçant les pièces défectueuses.",
    impact_cost=-3,
    impact_ecology=4,
    impact_autonomy=4,
    impact_inclusion=5
)

Option.objects.create(
    id=10,
    category=cat5,
    name="Jeter les PC obsolètes et acheter des neufs",
    description="Solution rapide mais coûteuse et peu écologique.",
    impact_cost=4,
    impact_ecology=-4,
    impact_autonomy=-3,
    impact_inclusion=-2
)

print(f"✅ {Option.objects.count()} options créées")

print("\n📝 Création des questions de quiz...")

# Questions de quiz
QuizQuestion.objects.create(
    id=1,
    question_text="Linux est un système d'exploitation libre.",
    is_true=True,
    explanation="Linux est effectivement un système d'exploitation libre et open source, ce qui signifie que son code source est accessible à tous et peut être modifié librement.",
    resource_url="https://fr.wikipedia.org/wiki/Linux"
)

QuizQuestion.objects.create(
    id=2,
    question_text="Les logiciels Microsoft Office sont gratuits.",
    is_true=False,
    explanation="Microsoft Office est un logiciel propriétaire payant qui nécessite l'achat d'une licence pour être utilisé légalement.",
    resource_url="https://www.microsoft.com/fr-fr/microsoft-365/buy/compare-all-microsoft-365-products"
)

QuizQuestion.objects.create(
    id=3,
    question_text="Réutiliser les ordinateurs est bon pour l'environnement.",
    is_true=True,
    explanation="La réutilisation des ordinateurs réduit les déchets électroniques et diminue la demande de production de nouveaux équipements, ce qui est bénéfique pour l'environnement.",
    resource_url="https://www.ademe.fr/particuliers-eco-citoyens/dechets/bien-jeter/faire-appareils-electriques-electroniques"
)

QuizQuestion.objects.create(
    id=4,
    question_text="Les données dans le cloud sont toujours sécurisées.",
    is_true=False,
    explanation="Bien que les services cloud offrent généralement une bonne sécurité, aucun système n'est totalement sûr. La sécurité dépend de nombreux facteurs comme le fournisseur, la configuration et les pratiques de l'utilisateur.",
    resource_url="https://www.cnil.fr/fr/le-cloud-computing"
)

QuizQuestion.objects.create(
    id=5,
    question_text="Les logiciels libres permettent aux utilisateurs de modifier leur code source.",
    is_true=True,
    explanation="C'est l'une des libertés fondamentales des logiciels libres : la liberté d'étudier le fonctionnement du programme et de le modifier pour qu'il fasse ce que vous souhaitez.",
    resource_url="https://www.gnu.org/philosophy/free-sw.fr.html"
)

QuizQuestion.objects.create(
    id=6,
    question_text="Tous les systèmes d'exploitation Linux sont gratuits.",
    is_true=True,
    explanation="Les distributions Linux sont généralement gratuites à télécharger et à utiliser. Même si certaines entreprises proposent des versions commerciales avec support, le système d'exploitation lui-même reste libre.",
    resource_url="https://doc.ubuntu-fr.org/linux"
)

QuizQuestion.objects.create(
    id=7,
    question_text="Il est impossible de réutiliser un PC de plus de 5 ans.",
    is_true=False,
    explanation="Un PC de plus de 5 ans peut tout à fait être réutilisé, notamment en installant un système d'exploitation léger comme Linux, en ajoutant de la RAM ou en remplaçant le disque dur par un SSD.",
    resource_url="https://emmabuntus.org/"
)

QuizQuestion.objects.create(
    id=8,
    question_text="Le stockage en ligne est plus sécurisé que le stockage local.",
    is_true=False,
    explanation="La sécurité dépend de nombreux facteurs. Le stockage local peut être plus sécurisé si bien géré, car les données restent sous votre contrôle direct. Le stockage en ligne présente des risques comme les piratages de serveurs ou les accès non autorisés.",
    resource_url="https://www.cnil.fr/fr/securite-informatique-les-precautions-elementaires"
)

print(f"✅ {QuizQuestion.objects.count()} questions créées")

print("\n📚 Création des ressources...")

# Ressources pédagogiques
Resource.objects.create(
    id=1,
    title="Présentation de NIRD",
    type="site",
    url="https://nird.forge.apps.education.fr",
    description="Site officiel du projet NIRD pour les établissements scolaires."
)

Resource.objects.create(
    id=2,
    title="Pourquoi Linux à l'école ?",
    type="video",
    url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    description="Vidéo d'élèves qui expliquent pourquoi Linux est adapté aux écoles."
)

Resource.objects.create(
    id=3,
    title="Logiciels libres et leur impact",
    type="article",
    url="https://april.org/logiciels-libres-education",
    description="Un article sur les avantages des logiciels libres dans les écoles."
)

Resource.objects.create(
    id=4,
    title="Le mouvement des logiciels libres",
    type="article",
    url="https://framablog.org/education/",
    description="Un article expliquant l'importance des logiciels libres dans l'éducation."
)

Resource.objects.create(
    id=5,
    title="Réutilisation et recyclage informatique",
    type="video",
    url="https://www.youtube.com/watch?v=xyz123",
    description="Vidéo expliquant comment réutiliser les anciens PC et les transformer en outils pédagogiques."
)

Resource.objects.create(
    id=6,
    title="Les alternatives open-source à Microsoft Office",
    type="site",
    url="https://fr.libreoffice.org/",
    description="Présentation de LibreOffice, une alternative libre et gratuite à Microsoft Office."
)

print(f"✅ {Resource.objects.count()} ressources créées")

print("\n✨ Toutes les données NUID ont été chargées avec succès!")
print("\n📊 Résumé:")
print(f"  - Catégories: {Category.objects.count()}")
print(f"  - Options: {Option.objects.count()}")
print(f"  - Questions Quiz: {QuizQuestion.objects.count()}")
print(f"  - Ressources: {Resource.objects.count()}")

print("\n🎯 Les APIs sont prêtes à être testées:")
print("  - GET /api/categories/")
print("  - GET /api/quiz/")
print("  - GET /api/options/")
print("  - GET /api/resources/")
