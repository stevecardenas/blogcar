from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    list_editable = ['is_read']
    
    fieldsets = (
        ('Informazioni Messaggio', {
            'fields': ('name', 'email', 'subject', 'message')
        }),
        ('Stato', {
            'fields': ('is_read', 'created_at')
        }),
    ) 