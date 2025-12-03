from django.shortcuts import render
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django_rest_framework.response import Response
from django.http import JsonResponse




def home(request):
    return render(request, "index.html", {"test": "tests"})




    

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        # Include anchors as separate items
        return [
            'home'
        ]

    def location(self, item):
        # Split to handle anchors correctly
        if '#' in item:
            base, anchor = item.split('#')
            return reverse(base) + f'#{anchor}'
        return reverse(item)






def test_deployment(request):
    return JsonResponse({"status": "Layers backend is deployed successfully!"})