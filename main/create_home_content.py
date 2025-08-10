#!/usr/bin/env python
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from core.models import HomeContent

def create_default_home_content():
    """Crear contenido por defecto para la página de inicio"""
    
    # Verificar si ya existe contenido
    if HomeContent.objects.filter(is_active=True).exists():
        print("Ya existe contenido activo. No se creará contenido duplicado.")
        return
    
    # Crear contenido por defecto
    home_content = HomeContent.objects.create(
        header_badge="Sistemi Embedded · Automazione · IoT",
        header_subtitle="Posso aiutare la tua azienda a",
        header_title="Crescere e innovare",
        about_title="Chi Sono",
        about_subtitle="Mi chiamo Steve Cardenas Ortiz e aiuto le aziende a crescere.",
        about_description="Ingegnere elettronico specializzato in sistemi embedded, automazione industriale e IoT. Con oltre 8 anni di esperienza nello sviluppo di soluzioni elettroniche innovative per diverse industrie.",
        resume_button_text="Resume",
        projects_button_text="Projects",
        is_active=True
    )
    
    print(f"✅ Contenido por defecto creado exitosamente!")
    print(f"📝 ID: {home_content.id}")
    print(f"🔄 Última actualización: {home_content.updated_at}")
    print("\n🎯 Ahora puedes:")
    print("1. Ir a http://127.0.0.1:8000/admin/")
    print("2. Iniciar sesión con tu superusuario")
    print("3. Editar el contenido en 'Contenidos de la página de inicio'")

if __name__ == "__main__":
    create_default_home_content()
