from django.shortcuts import render
from projects.models import Project
from .models import SocialMedia, HomeContent

# Create your views here.

def get_social_media_context():
    """Función para obtener el contexto de redes sociales"""
    return {
        'social_media': SocialMedia.objects.filter(is_active=True).order_by('order')
    }

def home_view(request):
    """Vista para la página de inicio"""
    featured_projects = Project.objects.select_related('category').filter(is_featured=True)[:3]
    
    # Obtener el contenido dinámico de la página de inicio
    home_content = HomeContent.get_active_content()
    
    context = {
        'featured_projects': featured_projects,
        'title': 'Steve Cardenas Ortiz - Ingegnere Elettronico',
        'home_content': home_content
    }
    # Agregar el contexto de redes sociales
    context.update(get_social_media_context())
    return render(request, 'core/home.html', context)
