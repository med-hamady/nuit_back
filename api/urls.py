from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    StaticViewSitemap, home, test_deployment,
    CategoryListView, QuizListView, OptionListView,
    SimulationRunViewSet, IdeaViewSet, ResourceListView, health_check,
    RegisterView, LoginView, user_profile
)
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'static': StaticViewSitemap,
}

router = DefaultRouter()
router.register(r'simulation-runs', SimulationRunViewSet, basename='simulation-run')
router.register(r'ideas', IdeaViewSet, basename='idea')

urlpatterns = [
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt",
        content_type="text/plain"
    )),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django-sitemap'),

    path('test/', test_deployment, name='test-deployment'),

    # API Endpoints
    path('api/categories/', CategoryListView.as_view(), name='category-list'),
    path('api/quiz/', QuizListView.as_view(), name='quiz-list'),
    path('api/options/', OptionListView.as_view(), name='option-list'),
    path('api/resources/', ResourceListView.as_view(), name='resource-list'),
    path('api/health/', health_check, name='health-check'),

    # Authentication Endpoints
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/me/', user_profile, name='user-profile'),

    # ViewSets routes
    path('api/', include(router.urls)),

]

