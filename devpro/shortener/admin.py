from django.contrib import admin

from devpro.shortener.models import UrlRedirect


# Register your models here.

@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('destiny', 'slug', 'created_in', 'update_in',)
