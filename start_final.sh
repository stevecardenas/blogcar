#!/usr/bin/env bash
# Script final para Render - Solución definitiva

# Cambiar al directorio del proyecto
cd /opt/render/project/src

# Verificar que estamos en el lugar correcto
echo "=== Verificación de estructura ==="
echo "Directorio actual: $(pwd)"
echo "Contenido:"
ls -la

echo "=== Verificación de main ==="
ls -la main/

echo "=== Verificación de main/main ==="
ls -la main/main/

# Configurar el entorno
export DJANGO_SETTINGS_MODULE=main.settings
export PYTHONPATH="/opt/render/project/src"

# Ejecutar Gunicorn desde el directorio main
cd main
echo "=== Ejecutando Gunicorn desde main ==="
exec gunicorn main.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 2 \
    --timeout 120 \
    --preload
