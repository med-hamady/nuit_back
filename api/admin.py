from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from api.models.models import *

import requests



@admin.register(APILog)
class APILogAdmin(admin.ModelAdmin):
    
    list_display = ['formatted_request_date','country', 'city','user_email' ,'path', 'response_status']

    
    list_filter = ['response_status','country', 'city']
    search_fields = ['body', 'user_email','ip_address']
    def formatted_request_date(self, obj):
        return obj.request_date.strftime("%Y-%m-%d %H:%M:%S") if obj.request_date else "-"
    formatted_request_date.short_description = 'Request Date'



# admin.site.register(UserMetaData)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    ordering = ['order']


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'impact_cost', 'impact_ecology', 'impact_autonomy', 'impact_inclusion']
    list_filter = ['category']
    search_fields = ['name', 'description']
    list_select_related = ['category']


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text_short', 'is_true', 'created_at']
    list_filter = ['is_true', 'created_at']
    search_fields = ['question_text', 'explanation']

    def question_text_short(self, obj):
        return obj.question_text[:50] + '...' if len(obj.question_text) > 50 else obj.question_text
    question_text_short.short_description = 'Question'


@admin.register(SimulationRun)
class SimulationRunAdmin(admin.ModelAdmin):
    list_display = ['id', 'score_cost', 'score_ecology', 'score_autonomy', 'score_inclusion', 'created_at']
    list_filter = ['created_at']
    search_fields = ['choices']
    readonly_fields = ['created_at']
    ordering = ['-created_at']


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_approved', 'created_at', 'updated_at']
    list_filter = ['is_approved', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_approved']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'url', 'created_at']
    list_filter = ['type', 'created_at']
    search_fields = ['title', 'description', 'url']
    ordering = ['-created_at']