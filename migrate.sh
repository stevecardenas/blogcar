#!/usr/bin/env bash
# Script para aplicar migraciones en Render

echo "=== APLICANDO MIGRACIONES EN RENDER ==="

# Cambiar al directorio del proyecto
cd /opt/render/project/src/main

echo "=== 1. Verificación de Django ==="
python manage.py check

echo "=== 2. Mostrar migraciones pendientes ==="
python manage.py showmigrations

echo "=== 3. Aplicando migraciones ==="
python manage.py migrate

echo "=== 4. Verificación final ==="
python manage.py showmigrations

echo "=== 5. Verificación de base de datos ==="
python manage.py dbshell --command="SELECT name FROM sqlite_master WHERE type='table';" 2>/dev/null || echo "Error al conectar con la base de datos"

echo "=== MIGRACIONES COMPLETADAS ==="
