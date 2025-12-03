from django.urls import path
from api.views import StaticViewSitemap, home, test_deployment
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt",
        content_type="text/plain"
    )),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django-sitemap'),

    path('test/', test_deployment, name='test-deployment'),

]

