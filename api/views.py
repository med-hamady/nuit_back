from django.shortcuts import render
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from api.models.models import Category, Option, QuizQuestion, SimulationRun, Idea, Resource
from api.serializers.serializer_simulation import (
    CategorySerializer, OptionSerializer, QuizQuestionSerializer,
    SimulationRunSerializer, IdeaSerializer, IdeaUpdateSerializer, ResourceSerializer
)
from api.serializers.serializer_auth import RegisterSerializer, LoginSerializer, UserSerializer




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


# GET /api/categories/ - Configuration de la simulation
class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all().prefetch_related('options')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


# GET /api/quiz/ - Questions vrai/faux pour le quiz
class QuizListView(APIView):
    def get(self, request):
        questions = QuizQuestion.objects.all()
        serializer = QuizQuestionSerializer(questions, many=True)
        return Response(serializer.data)


# GET /api/options/ - Liste toutes les options
class OptionListView(APIView):
    def get(self, request):
        options = Option.objects.select_related('category').all()
        serializer = OptionSerializer(options, many=True)
        return Response(serializer.data)


# POST /api/simulation-runs/ et GET /api/simulation-runs/
class SimulationRunViewSet(viewsets.ModelViewSet):
    queryset = SimulationRun.objects.all()
    serializer_class = SimulationRunSerializer
    http_method_names = ['get', 'post']

    def get_queryset(self):
        queryset = SimulationRun.objects.all()
        limit = self.request.query_params.get('limit', 50)
        try:
            limit = int(limit)
        except ValueError:
            limit = 50
        return queryset[:limit]


# POST /api/ideas/ et GET /api/ideas/
class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    http_method_names = ['get', 'post', 'patch']

    def get_queryset(self):
        queryset = Idea.objects.all()
        approved_only = self.request.query_params.get('approved', None)
        if approved_only == 'true':
            queryset = queryset.filter(is_approved=True)
        return queryset

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return IdeaUpdateSerializer
        return IdeaSerializer


# GET /api/resources/ - Ressources pédagogiques
class ResourceListView(APIView):
    def get(self, request):
        resources = Resource.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data)


# GET /api/health/ - Health check
@api_view(['GET'])
def health_check(request):
    return Response({
        'status': 'ok',
        'message': 'NUIT Backend is running'
    })


# POST /api/auth/register/ - Inscription
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': UserSerializer(user).data,
                'token': token.key,
                'message': 'Inscription réussie'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# POST /api/auth/login/ - Connexion
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': UserSerializer(user).data,
                'token': token.key,
                'message': 'Connexion réussie'
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET /api/auth/me/ - Profil utilisateur (nécessite authentification)
@api_view(['GET'])
def user_profile(request):
    if request.user.is_authenticated:
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    return Response({'error': 'Non authentifié'}, status=status.HTTP_401_UNAUTHORIZED)