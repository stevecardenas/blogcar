#!/usr/bin/env bash
# Script de inicio para Render

# Cambiar al directorio del proyecto
cd /opt/render/project/src

# Configurar variables de entorno si no están definidas
export DJANGO_SETTINGS_MODULE=main.settings

# Ejecutar Gunicorn
exec gunicorn main.main.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 120
