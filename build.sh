#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Recolectar archivos estáticos
python main/manage.py collectstatic --no-input

# Ejecutar migraciones
python main/manage.py migrate
