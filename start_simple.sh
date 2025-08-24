#!/usr/bin/env bash
# Script de inicio simple para Render

# Cambiar al directorio del proyecto
cd /opt/render/project/src

# Configurar el entorno de Django
export DJANGO_SETTINGS_MODULE=main.settings

# Ejecutar Gunicorn desde el directorio main
cd main
exec gunicorn main.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 2 \
    --timeout 120
