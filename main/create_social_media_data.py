#!/usr/bin/env python
"""
Script para crear datos de ejemplo de redes sociales
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from core.models import SocialMedia

def create_social_media_data():
    """Crear datos de ejemplo para redes sociales"""
    
    # Datos de ejemplo de redes sociales
    social_media_data = [
        {
            'name': 'LinkedIn',
            'url': 'https://www.linkedin.com/in/steve-cardenas-ortiz',
            'icon': 'linkedin',
            'order': 1,
        },
        {
            'name': 'GitHub',
            'url': 'https://github.com/stevecardenas',
            'icon': 'github',
            'order': 2,
        },
        {
            'name': 'Twitter',
            'url': 'https://twitter.com/stevecardenas',
            'icon': 'twitter-x',
            'order': 3,
        },
        {
            'name': 'Instagram',
            'url': 'https://www.instagram.com/stevecardenas',
            'icon': 'instagram',
            'order': 4,
        },
        {
            'name': 'YouTube',
            'url': 'https://www.youtube.com/@stevecardenas',
            'icon': 'youtube',
            'order': 5,
        },
    ]
    
    # Crear las redes sociales
    for data in social_media_data:
        social_media, created = SocialMedia.objects.get_or_create(
            name=data['name'],
            defaults=data
        )
        if created:
            print(f"✅ Creada red social: {data['name']}")
        else:
            print(f"⚠️  Red social ya existe: {data['name']}")
    
    print("\n🎉 Datos de redes sociales creados exitosamente!")
    print("Puedes gestionar las redes sociales desde el admin de Django.")

if __name__ == '__main__':
    create_social_media_data() 