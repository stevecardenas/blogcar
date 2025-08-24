#!/usr/bin/env bash
# Script de debug para Render

echo "=== DIAGNÓSTICO DE RENDER ==="

# Cambiar al directorio del proyecto
cd /opt/render/project/src

echo "=== 1. Verificación de estructura ==="
echo "Directorio actual: $(pwd)"
ls -la

echo "=== 2. Verificación de variables de entorno ==="
echo "SECRET_KEY: ${SECRET_KEY:0:10}..."
echo "DEBUG: $DEBUG"
echo "ALLOWED_HOSTS: $ALLOWED_HOSTS"
echo "DJANGO_SETTINGS_MODULE: $DJANGO_SETTINGS_MODULE"

echo "=== 3. Verificación de Django ==="
cd main
python manage.py check --deploy

echo "=== 4. Verificación de migraciones ==="
python manage.py showmigrations

echo "=== 5. Verificación de archivos estáticos ==="
ls -la staticfiles/

echo "=== 6. Verificación de base de datos ==="
python manage.py dbshell --command="SELECT 1;" 2>/dev/null && echo "✅ Base de datos OK" || echo "❌ Error en base de datos"

echo "=== DIAGNÓSTICO COMPLETADO ==="
