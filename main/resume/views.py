from django.shortcuts import render
from .models import Resume, Experience, Education, Skill

def resume_view(request):
    """Vista para mostrar el CV"""
    resume = Resume.objects.first()
    
    if not resume:
        # Crear un CV por defecto si no existe
        resume = Resume.objects.create()
    
    # Obtener experiencias, educación y habilidades ordenadas
    experiences = resume.experiences.all()
    educations = resume.educations.all()
    skills = resume.skills.all()
    
    # Agrupar habilidades por categoría
    skills_by_category = {}
    for skill in skills:
        category = skill.get_category_display()
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)
    
    context = {
        'resume': resume,
        'experiences': experiences,
        'educations': educations,
        'skills_by_category': skills_by_category,
        'title': 'CV - Steve Cardenas Ortiz'
    }
    return render(request, 'resume/resume.html', context) 