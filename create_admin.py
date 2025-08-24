#!/usr/bin/env python3
"""
Script para crear superusuario en Django
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def create_superuser():
    """Crear superusuario si no existe"""
    
    # Credenciales del superusuario
    username = 'admin'
    email = 'admin@example.com'
    password = 'admin123456'
    
    try:
        # Verificar si ya existe
        if User.objects.filter(username=username).exists():
            print(f"✅ Superusuario '{username}' ya existe")
            return
        
        # Crear superusuario
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        
        print(f"✅ Superusuario creado exitosamente!")
        print(f"   Usuario: {username}")
        print(f"   Email: {email}")
        print(f"   Contraseña: {password}")
        print(f"   ID: {user.id}")
        
    except Exception as e:
        print(f"❌ Error creando superusuario: {e}")

def list_superusers():
    """Listar todos los superusuarios"""
    superusers = User.objects.filter(is_superuser=True)
    print(f"📋 Superusuarios existentes ({superusers.count()}):")
    for user in superusers:
        print(f"   - {user.username} ({user.email}) - ID: {user.id}")

if __name__ == "__main__":
    print("=== CREACIÓN DE SUPERUSUARIO ===")
    create_superuser()
    print("\n=== LISTADO DE SUPERUSUARIOS ===")
    list_superusers()
    print("\n=== INSTRUCCIONES ===")
    print("1. Ve a: https://tu-app.onrender.com/admin/")
    print("2. Usuario: admin")
    print("3. Contraseña: admin123456")
