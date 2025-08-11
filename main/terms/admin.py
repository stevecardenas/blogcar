from django.contrib import admin
from .models import Terms, Privacy, Cookies

@admin.register(Terms)
class TermsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_active',)
    ordering = ('-updated_at',)

@admin.register(Privacy)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_active',)
    ordering = ('-updated_at',)

@admin.register(Cookies)
class CookiesAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_active',)
    ordering = ('-updated_at',)
