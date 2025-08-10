from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Project, Category

def projects_view(request):
    """Vista para mostrar todos los proyectos con paginación"""
    projects = Project.objects.select_related('category').all()
    categories = Category.objects.all()
    
    # Filtrar por categoría si se especifica
    category_id = request.GET.get('category')
    if category_id:
        projects = projects.filter(category_id=category_id)
    
    # Búsqueda por texto
    search_query = request.GET.get('search')
    if search_query:
        projects = projects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(technologies__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )
    
    # Ordenamiento
    sort_by = request.GET.get('sort', 'created_at')
    if sort_by == 'title':
        projects = projects.order_by('title')
    elif sort_by == 'category':
        projects = projects.order_by('category__name', 'title')
    elif sort_by == 'featured':
        projects = projects.order_by('-is_featured', '-created_at')
    else:
        projects = projects.order_by('-created_at')
    
    # Paginación
    paginator = Paginator(projects, 12)  # 12 proyectos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Estadísticas
    total_projects = Project.objects.count()
    featured_projects = Project.objects.filter(is_featured=True).count()
    categories_count = Category.objects.count()
    
    context = {
        'projects': page_obj.object_list,
        'page_obj': page_obj,
        'categories': categories,
        'title': 'Progetti',
        'search_query': search_query,
        'sort_by': sort_by,
        'stats': {
            'total_projects': total_projects,
            'featured_projects': featured_projects,
            'categories_count': categories_count,
        }
    }
    return render(request, 'projects/projects.html', context)

def project_detail_view(request, slug):
    """Vista para mostrar detalles de un proyecto específico usando slug"""
    project = get_object_or_404(Project.objects.select_related('category'), slug=slug)
    
    # Proyectos relacionados de la misma categoría
    related_projects = Project.objects.select_related('category').filter(
        category=project.category
    ).exclude(id=project.id).order_by('-is_featured', '-created_at')[:3]
    
    # Proyectos destacados de otras categorías
    other_featured = Project.objects.select_related('category').filter(
        is_featured=True
    ).exclude(category=project.category).order_by('-created_at')[:2]
    
    context = {
        'project': project,
        'related_projects': related_projects,
        'other_featured': other_featured,
        'title': f'Progetto - {project.title}'
    }
    return render(request, 'projects/project_detail.html', context) 