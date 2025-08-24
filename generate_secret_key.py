#!/usr/bin/env python3
"""
Script para generar una SECRET_KEY segura para Django
"""

import secrets
import string

def generate_secret_key(length=50):
    """Genera una SECRET_KEY segura para Django"""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*(-_=+)"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print("🔑 SECRET_KEY generada para Django:")
    print(f"SECRET_KEY={secret_key}")
    print("\n📋 Copia esta línea y agrégala a tus variables de entorno en Render")
    print("⚠️  IMPORTANTE: Nunca compartas esta clave públicamente")
