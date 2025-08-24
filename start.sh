#!/usr/bin/env bash
# Script de inicio para Render

# Cambiar al directorio del proyecto
cd /opt/render/project/src

# Configurar PYTHONPATH para incluir el directorio del proyecto
export PYTHONPATH="${PYTHONPATH}:/opt/render/project/src"

# Configurar variables de entorno si no están definidas
export DJANGO_SETTINGS_MODULE=main.settings

# Verificar que estamos en el directorio correcto
echo "Directorio actual: $(pwd)"
echo "Contenido del directorio:"
ls -la

echo "Verificando estructura de main:"
ls -la main/

# Ejecutar Gunicorn con configuración específica
exec gunicorn main.main.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 2 \
    --timeout 120 \
    --preload
