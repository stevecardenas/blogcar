from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email_link', 'subject', 'created_at', 'is_read', 'message_preview']
    list_filter = ['is_read', 'created_at', 'subject']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at', 'email_link']
    list_editable = ['is_read']
    date_hierarchy = 'created_at'
    list_per_page = 25
    
    fieldsets = (
        ('Informazioni Messaggio', {
            'fields': ('name', 'email_link', 'subject', 'message')
        }),
        ('Stato', {
            'fields': ('is_read', 'created_at')
        }),
    )
    
    actions = ['mark_as_read', 'mark_as_unread', 'send_reply']
    
    def email_link(self, obj):
        """Mostra l'email come link cliccabile"""
        if obj.email:
            return format_html('<a href="mailto:{}">{}</a>', obj.email, obj.email)
        return obj.email
    email_link.short_description = 'Email'
    email_link.admin_order_field = 'email'
    
    def message_preview(self, obj):
        """Mostra un'anteprima del messaggio"""
        preview = obj.message[:100] + '...' if len(obj.message) > 100 else obj.message
        return format_html('<span title="{}">{}</span>', obj.message, preview)
    message_preview.short_description = 'Anteprima Messaggio'
    
    def mark_as_read(self, request, queryset):
        """Marca i messaggi come letti"""
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} messaggi marcati come letti.')
    mark_as_read.short_description = "Marca come letti"
    
    def mark_as_unread(self, request, queryset):
        """Marca i messaggi come non letti"""
        updated = queryset.update(is_read=False)
        self.message_user(request, f'{updated} messaggi marcati come non letti.')
    mark_as_unread.short_description = "Marca come non letti"
    
    def send_reply(self, request, queryset):
        """Azione per inviare risposta (placeholder)"""
        self.message_user(request, f'Funzionalità di risposta in sviluppo per {queryset.count()} messaggi.')
    send_reply.short_description = "Invia risposta"
    
    def get_queryset(self, request):
        """Ordina per data di creazione decrescente"""
        return super().get_queryset(request).order_by('-created_at')
    
    def has_add_permission(self, request):
        """Disabilita l'aggiunta manuale di messaggi"""
        return False 