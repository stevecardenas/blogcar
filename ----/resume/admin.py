from django.contrib import admin
from django.utils.html import format_html
from .models import Resume, Experience, Education, Skill

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'title', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'email', 'title', 'summary']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Informazioni Personali', {
            'fields': ('name', 'email', 'phone', 'title', 'summary')
        }),
        ('Metadati', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        """Mostrar solo el primer CV (singleton pattern)"""
        return super().get_queryset(request)
    
    def has_add_permission(self, request):
        """Permitir agregar solo si no existe ningún CV"""
        return Resume.objects.count() == 0
    
    def has_delete_permission(self, request, obj=None):
        """No permitir eliminar el CV principal"""
        return False

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'location', 'get_period', 'order']
    list_filter = ['current', 'start_date', 'end_date']
    search_fields = ['position', 'company', 'location', 'description']
    list_editable = ['order']
    
    fieldsets = (
        ('Informazioni Azienda', {
            'fields': ('resume', 'company', 'position', 'location')
        }),
        ('Periodo', {
            'fields': ('start_date', 'end_date', 'current')
        }),
        ('Descrizione', {
            'fields': ('description',)
        }),
        ('Ordinamento', {
            'fields': ('order',),
            'classes': ('collapse',)
        }),
    )
    
    def get_period(self, obj):
        return obj.get_period()
    get_period.short_description = 'Periodo'

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'location', 'get_period', 'order']
    list_filter = ['current', 'start_date', 'end_date']
    search_fields = ['degree', 'institution', 'location', 'description']
    list_editable = ['order']
    
    fieldsets = (
        ('Informazioni Istituzione', {
            'fields': ('resume', 'institution', 'degree', 'location')
        }),
        ('Periodo', {
            'fields': ('start_date', 'end_date', 'current')
        }),
        ('Descrizione', {
            'fields': ('description',)
        }),
        ('Ordinamento', {
            'fields': ('order',),
            'classes': ('collapse',)
        }),
    )
    
    def get_period(self, obj):
        return obj.get_period()
    get_period.short_description = 'Periodo'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'get_proficiency_display', 'order']
    list_filter = ['category', 'proficiency']
    search_fields = ['name', 'description']
    list_editable = ['order', 'proficiency']
    
    fieldsets = (
        ('Informazioni Competenza', {
            'fields': ('resume', 'name', 'category')
        }),
        ('Livello', {
            'fields': ('proficiency', 'description')
        }),
        ('Ordinamento', {
            'fields': ('order',),
            'classes': ('collapse',)
        }),
    )
    
    def get_proficiency_display(self, obj):
        return obj.get_proficiency_display()
    get_proficiency_display.short_description = 'Livello' 