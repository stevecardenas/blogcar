#!/bin/bash

# Script para aceptar todos los cambios en Git
# Uso: ./accept-all-changes.sh [mensaje_commit]

# Obtener mensaje de commit (opcional)
COMMIT_MESSAGE=${1:-"Auto commit - $(date '+%Y-%m-%d %H:%M:%S')"}

echo "🔄 Aceptando todos los cambios..."

# Agregar todos los archivos modificados
git add .

# Verificar si hay cambios para commitear
if git diff --cached --quiet; then
    echo "✅ No hay cambios para commitear"
    exit 0
fi

# Hacer commit con el mensaje
git commit -m "$COMMIT_MESSAGE"

# Mostrar estado final
echo "✅ Cambios aceptados exitosamente!"
echo "📝 Commit: $COMMIT_MESSAGE"
echo ""
echo "📊 Estado actual:"
git status --short
