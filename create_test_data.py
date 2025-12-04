"""
Script pour créer des données de test dans la base de données
Usage: python manage.py shell < create_test_data.py
Ou copiez-collez ce code dans: python manage.py shell
"""

from api.models.models import Category, Option, QuizQuestion, Resource

# Supprimer les données existantes (optionnel)
print("🗑️  Nettoyage des données existantes...")
Category.objects.all().delete()
QuizQuestion.objects.all().delete()
Resource.objects.all().delete()

print("📦 Création des catégories et options...")

# 1. Catégorie: Système d'exploitation
cat_os = Category.objects.create(
    name="Système d'exploitation",
    description="Choisissez le système d'exploitation pour votre établissement",
    order=1
)

Option.objects.create(
    category=cat_os,
    name="Windows 11 Pro",
    description="Système propriétaire de Microsoft",
    impact_cost=150.00,
    impact_ecology=-30.00,
    impact_autonomy=-40.00,
    impact_inclusion=90.00
)

Option.objects.create(
    category=cat_os,
    name="Linux Ubuntu",
    description="Distribution Linux populaire et gratuite",
    impact_cost=0.00,
    impact_ecology=60.00,
    impact_autonomy=80.00,
    impact_inclusion=70.00
)

Option.objects.create(
    category=cat_os,
    name="Linux Debian",
    description="Distribution Linux stable et sécurisée",
    impact_cost=0.00,
    impact_ecology=70.00,
    impact_autonomy=90.00,
    impact_inclusion=60.00
)

# 2. Catégorie: Suite bureautique
cat_suite = Category.objects.create(
    name="Suite bureautique",
    description="Choisissez vos outils de productivité",
    order=2
)

Option.objects.create(
    category=cat_suite,
    name="Microsoft Office 365",
    description="Suite bureautique propriétaire",
    impact_cost=100.00,
    impact_ecology=-20.00,
    impact_autonomy=-30.00,
    impact_inclusion=95.00
)

Option.objects.create(
    category=cat_suite,
    name="LibreOffice",
    description="Suite bureautique libre et gratuite",
    impact_cost=0.00,
    impact_ecology=50.00,
    impact_autonomy=70.00,
    impact_inclusion=80.00
)

Option.objects.create(
    category=cat_suite,
    name="Google Workspace",
    description="Suite bureautique en ligne",
    impact_cost=75.00,
    impact_ecology=-10.00,
    impact_autonomy=-20.00,
    impact_inclusion=90.00
)

# 3. Catégorie: Stockage
cat_storage = Category.objects.create(
    name="Solution de stockage",
    description="Où stocker vos données?",
    order=3
)

Option.objects.create(
    category=cat_storage,
    name="Google Drive",
    description="Stockage cloud de Google",
    impact_cost=50.00,
    impact_ecology=-15.00,
    impact_autonomy=-40.00,
    impact_inclusion=85.00
)

Option.objects.create(
    category=cat_storage,
    name="Nextcloud (auto-hébergé)",
    description="Solution de stockage cloud open source",
    impact_cost=30.00,
    impact_ecology=40.00,
    impact_autonomy=90.00,
    impact_inclusion=65.00
)

Option.objects.create(
    category=cat_storage,
    name="Serveur local",
    description="Stockage sur serveur dans l'établissement",
    impact_cost=200.00,
    impact_ecology=60.00,
    impact_autonomy=95.00,
    impact_inclusion=70.00
)

# 4. Catégorie: Matériel
cat_hardware = Category.objects.create(
    name="Matériel informatique",
    description="Quel type d'ordinateurs?",
    order=4
)

Option.objects.create(
    category=cat_hardware,
    name="Ordinateurs neufs",
    description="Ordinateurs neufs de dernière génération",
    impact_cost=800.00,
    impact_ecology=-50.00,
    impact_autonomy=50.00,
    impact_inclusion=80.00
)

Option.objects.create(
    category=cat_hardware,
    name="Ordinateurs reconditionnés",
    description="Ordinateurs de seconde main remis à neuf",
    impact_cost=400.00,
    impact_ecology=80.00,
    impact_autonomy=60.00,
    impact_inclusion=75.00
)

Option.objects.create(
    category=cat_hardware,
    name="Raspberry Pi",
    description="Mini-ordinateurs économiques et écologiques",
    impact_cost=100.00,
    impact_ecology=90.00,
    impact_autonomy=85.00,
    impact_inclusion=60.00
)

# 5. Catégorie: Connectivité
cat_network = Category.objects.create(
    name="Solution réseau",
    description="Comment connecter votre établissement?",
    order=5
)

Option.objects.create(
    category=cat_network,
    name="Fibre optique standard",
    description="Connexion internet classique",
    impact_cost=60.00,
    impact_ecology=-20.00,
    impact_autonomy=-30.00,
    impact_inclusion=85.00
)

Option.objects.create(
    category=cat_network,
    name="Réseau mesh communautaire",
    description="Réseau partagé avec la communauté locale",
    impact_cost=20.00,
    impact_ecology=50.00,
    impact_autonomy=80.00,
    impact_inclusion=95.00
)

Option.objects.create(
    category=cat_network,
    name="Connexion satellite",
    description="Pour les zones isolées",
    impact_cost=150.00,
    impact_ecology=-40.00,
    impact_autonomy=40.00,
    impact_inclusion=70.00
)

print(f"✅ {Category.objects.count()} catégories créées")
print(f"✅ {Option.objects.count()} options créées")

# Créer des questions de quiz
print("\n📝 Création des questions de quiz...")

QuizQuestion.objects.create(
    question_text="Le logiciel libre est toujours gratuit",
    is_true=True,
    explanation="Les logiciels libres peuvent être utilisés, modifiés et distribués gratuitement. Leur code source est ouvert et accessible à tous."
)

QuizQuestion.objects.create(
    question_text="Les ordinateurs reconditionnés ont une empreinte écologique plus faible que les ordinateurs neufs",
    is_true=True,
    explanation="Réutiliser du matériel existant évite la production de nouveaux composants électroniques, ce qui réduit considérablement l'impact environnemental."
)

QuizQuestion.objects.create(
    question_text="Windows est le seul système d'exploitation utilisable en milieu éducatif",
    is_true=False,
    explanation="De nombreuses alternatives existent, notamment Linux (Ubuntu, Debian) qui sont parfaitement adaptées au milieu éducatif et offrent même des avantages en termes de coûts et de sécurité."
)

QuizQuestion.objects.create(
    question_text="Le cloud computing réduit toujours l'impact écologique",
    is_true=False,
    explanation="Le cloud nécessite d'énormes centres de données qui consomment beaucoup d'énergie. Une solution locale peut parfois être plus écologique selon l'usage."
)

QuizQuestion.objects.create(
    question_text="L'autonomie numérique signifie ne pas dépendre de grandes entreprises technologiques",
    is_true=True,
    explanation="L'autonomie numérique, c'est avoir le contrôle sur ses données et ses outils, sans dépendre exclusivement de fournisseurs propriétaires."
)

QuizQuestion.objects.create(
    question_text="Les logiciels open source sont moins sécurisés que les logiciels propriétaires",
    is_true=False,
    explanation="Les logiciels open source peuvent être audités par la communauté, ce qui permet de détecter et corriger rapidement les failles de sécurité."
)

QuizQuestion.objects.create(
    question_text="Un réseau mesh peut améliorer l'inclusion numérique d'une communauté",
    is_true=True,
    explanation="Les réseaux mesh permettent de partager la connectivité internet entre plusieurs utilisateurs, réduisant les coûts et améliorant l'accès pour tous."
)

QuizQuestion.objects.create(
    question_text="L'inclusion numérique concerne uniquement l'accès à internet",
    is_true=False,
    explanation="L'inclusion numérique englobe l'accès à internet, mais aussi les compétences numériques, l'accessibilité des outils et la capacité à utiliser la technologie de manière autonome."
)

print(f"✅ {QuizQuestion.objects.count()} questions de quiz créées")

# Créer des ressources pédagogiques
print("\n📚 Création des ressources pédagogiques...")

Resource.objects.create(
    title="Introduction au logiciel libre",
    type="video",
    url="https://www.youtube.com/watch?v=Ag1AKIl_2GM",
    description="Une excellente introduction aux concepts du logiciel libre et open source"
)

Resource.objects.create(
    title="Framasoft - Dégooglisons Internet",
    type="site",
    url="https://degooglisons-internet.org/",
    description="Collection d'alternatives libres et éthiques aux services des géants du web"
)

Resource.objects.create(
    title="Guide d'installation Ubuntu",
    type="article",
    url="https://ubuntu.com/tutorials/install-ubuntu-desktop",
    description="Guide officiel pour installer Ubuntu sur un ordinateur"
)

Resource.objects.create(
    title="Les enjeux de la souveraineté numérique",
    type="article",
    url="https://www.april.org/",
    description="Site de l'APRIL, association de promotion du logiciel libre"
)

Resource.objects.create(
    title="Introduction à Nextcloud",
    type="video",
    url="https://nextcloud.com/",
    description="Découvrez Nextcloud, l'alternative libre à Google Drive et Dropbox"
)

print(f"✅ {Resource.objects.count()} ressources créées")

print("\n✨ Toutes les données de test ont été créées avec succès!")
print("\n📊 Résumé:")
print(f"  - Catégories: {Category.objects.count()}")
print(f"  - Options: {Option.objects.count()}")
print(f"  - Questions Quiz: {QuizQuestion.objects.count()}")
print(f"  - Ressources: {Resource.objects.count()}")
