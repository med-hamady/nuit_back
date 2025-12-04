from rest_framework import serializers
from api.models.models import Category, Option, QuizQuestion, SimulationRun, Idea, Resource


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'name', 'description', 'impact_cost', 'impact_ecology',
                  'impact_autonomy', 'impact_inclusion']


class CategorySerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'order', 'options']


class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ['id', 'question_text', 'is_true', 'explanation', 'resource_url']


class SimulationRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimulationRun
        fields = ['id', 'score_cost', 'score_ecology', 'score_autonomy',
                  'score_inclusion', 'choices', 'created_at']
        read_only_fields = ['id', 'created_at']


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ['id', 'title', 'description', 'is_approved', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class IdeaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ['title', 'description', 'is_approved']


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'title', 'type', 'url', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']
