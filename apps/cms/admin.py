from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Testimonial, BlogPost, BlogAuthor, InfoPage, HomeSection, ContactMessage


@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ('customer_name', 'rating', 'created_at')
    search_fields = ('customer_name', 'message')
    ordering = ('-created_at',)


@admin.register(BlogAuthor)
class BlogAuthorAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(BlogPost)
class BlogPostAdmin(ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content', 'slug')
    ordering = ('-created_at',)


@admin.register(InfoPage)
class InfoPageAdmin(ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')


@admin.register(HomeSection)
class HomeSectionAdmin(ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)


@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'submitted_at')

    
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
