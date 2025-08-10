from django.contrib import admin
from .models import SocialMedia, HomeContent, SiteSettings, Navigation

# Register your models here.

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'icon', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'url']
    ordering = ['order', 'name']

@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'is_active', 'header_title', 'about_title')
    list_filter = ('is_active', 'created_at')
    search_fields = ('header_title', 'about_title')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Configuración', {
            'fields': ('is_active',)
        }),
        ('Sección Header', {
            'fields': ('header_badge', 'header_subtitle', 'header_title')
        }),
        ('Sección About', {
            'fields': ('about_title', 'about_subtitle', 'about_description')
        }),
        ('Botones', {
            'fields': ('resume_button_text', 'projects_button_text')
        }),
        ('Información del sistema', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    def save_model(self, request, obj, form, change):
        # Si se está activando este contenido, desactivar los demás
        if obj.is_active:
            HomeContent.objects.exclude(pk=obj.pk).update(is_active=False)
        super().save_model(request, obj, form, change)

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'profession', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('site_name', 'profession')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Configuración', {
            'fields': ('is_active',)
        }),
        ('Información del sitio', {
            'fields': ('site_name', 'site_title', 'site_description', 'profession')
        }),
        ('Copyright', {
            'fields': ('copyright_text',)
        }),
        ('Información del sistema', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    def save_model(self, request, obj, form, change):
        # Si se está activando esta configuración, desactivar las demás
        if obj.is_active:
            SiteSettings.objects.exclude(pk=obj.pk).update(is_active=False)
        super().save_model(request, obj, form, change)

@admin.register(Navigation)
class NavigationAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'name', 'url_name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'display_name', 'url_name')
    ordering = ('order', 'name')
    
    fieldsets = (
        ('Configuración', {
            'fields': ('is_active', 'order')
        }),
        ('Información del enlace', {
            'fields': ('name', 'display_name', 'url_name')
        }),
        ('Información del sistema', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
