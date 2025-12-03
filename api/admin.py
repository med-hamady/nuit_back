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