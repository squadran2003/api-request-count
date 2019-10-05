from django.contrib import admin
from .models import ApiRequest


class ApiRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'view_name', "created_at")
    search_fields = ('user__username',)

admin.site.register(ApiRequest, ApiRequestAdmin)

