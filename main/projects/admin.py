from django.contrib import admin
from .models import Category, Project

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'created_at']
    list_filter = ['category', 'is_featured', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['is_featured']
    
    fieldsets = (
        ('Informazioni Base', {
            'fields': ('title', 'description', 'category', 'is_featured')
        }),
        ('Media e Link', {
            'fields': ('image', 'url', 'github_url')
        }),
        ('Tecnologie', {
            'fields': ('technologies',)
        }),
        ('Metadati', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    ) 