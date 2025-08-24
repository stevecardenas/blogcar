#!/usr/bin/env bash
# exit on error
set -o errexit

echo "=== INICIANDO BUILD EN RENDER ==="

# Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt

# Verificar que Django funciona
echo "Verificando Django..."
cd main
python manage.py check

# Mostrar migraciones pendientes
echo "Mostrando migraciones..."
python manage.py showmigrations

# Ejecutar migraciones
echo "Aplicando migraciones..."
python manage.py migrate

# Verificar migraciones aplicadas
echo "Verificando migraciones aplicadas..."
python manage.py showmigrations

# Recolectar archivos estáticos
echo "Recolectando archivos estáticos..."
python manage.py collectstatic --no-input

echo "=== BUILD COMPLETADO ==="
