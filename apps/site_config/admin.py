from django.contrib import admin
from .models import SiteFeature, SocialLink
from unfold.admin import ModelAdmin

# SiteFeature Admin
@admin.register(SiteFeature)
class SiteFeatureAdmin(ModelAdmin):
    list_display = ('id', 'title', 'description', 'icon_class', 'sort_order')
    search_fields = ('title', 'description')
    ordering = ('sort_order',)
    list_editable = ('sort_order',) 

# SocialLink Admin
@admin.register(SocialLink)
class SocialLinkAdmin(ModelAdmin):
    list_display = ('id', 'platform', 'url', 'icon_class')
    search_fields = ('platform', 'url')
    ordering = ('id',)
