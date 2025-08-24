from django.shortcuts import render
from django.db import connection

# Create your views here.

def get_social_media_context():
    """Función para obtener el contexto de redes sociales"""
    try:
        from .models import SocialMedia
        return {
            'social_media': SocialMedia.objects.filter(is_active=True).order_by('order')
        }
    except:
        # Retornar datos de ejemplo si no hay base de datos
        return {
            'social_media': [
                {'name': 'LinkedIn', 'url': '#', 'icon': 'bi-linkedin'},
                {'name': 'GitHub', 'url': '#', 'icon': 'bi-github'},
                {'name': 'Email', 'url': 'mailto:steve@example.com', 'icon': 'bi-envelope'},
            ]
        }

def home_view(request):
    """Vista para la página de inicio"""
    
    # Verificar si las tablas existen
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='core_homecontent'")
            table_exists = cursor.fetchone() is not None
    except:
        table_exists = False
    
    if table_exists:
        # Si las tablas existen, usar datos de la base de datos
        try:
            from projects.models import Project
            featured_projects = Project.objects.select_related('category').filter(is_featured=True)[:3]
        except:
            featured_projects = []
        
        try:
            from .models import HomeContent
            home_content = HomeContent.get_active_content()
        except:
            home_content = None
    else:
        # Si las tablas no existen, usar datos de ejemplo
        featured_projects = []
        home_content = {
            'title': 'Steve Cardenas Ortiz',
            'subtitle': 'Ingegnere Elettronico',
            'description': 'Benvenuto nel mio portfolio! Sono un ingegnere elettronico appassionato di tecnologia e innovazione.',
            'hero_image': None
        }
    
    context = {
        'featured_projects': featured_projects,
        'title': 'Steve Cardenas Ortiz - Ingegnere Elettronico',
        'home_content': home_content
    }
    # Agregar el contexto de redes sociales
    context.update(get_social_media_context())
    return render(request, 'core/home.html', context)
