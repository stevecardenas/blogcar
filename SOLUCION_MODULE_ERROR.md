# 🚨 Solución para "ModuleNotFoundError: No module named 'main.settings'"

## 🔍 **Diagnóstico del Problema**

El error `ModuleNotFoundError: No module named 'main.settings'` indica que Gunicorn no puede encontrar el módulo de configuración de Django.

## 🛠️ **Soluciones en Orden de Prioridad**

### **Solución 1: Script Mejorado (Recomendado)**

Usa este comando en Render:
```
Start Command: ./start.sh
```

### **Solución 2: Script Simple**

Si la primera no funciona, usa:
```
Start Command: ./start_simple.sh
```

### **Solución 3: Comando Directo**

Si los scripts no funcionan, usa:
```
Start Command: cd /opt/render/project/src/main && gunicorn main.wsgi:application --bind 0.0.0.0:$PORT
```

### **Solución 4: Comando con PYTHONPATH**

Como última opción:
```
Start Command: cd /opt/render/project/src && PYTHONPATH=/opt/render/project/src gunicorn main.main.wsgi:application --bind 0.0.0.0:$PORT
```

## 📋 **Pasos para Aplicar la Solución**

### **1. Actualizar el Start Command en Render:**

1. Ve a tu **Web Service** en Render
2. Haz clic en **"Settings"**
3. Busca la sección **"Start Command"**
4. Cambia el comando por una de las opciones arriba
5. Haz clic en **"Save Changes"**
6. Espera a que se haga un nuevo deploy

### **2. Verificar Variables de Entorno:**

Asegúrate de tener estas variables configuradas:
```
SECRET_KEY=w=16hGTv^tV5LAlSN^v&CnPMzOa1d3R8Mr8-%Qy%JZBycDL*EL
DEBUG=False
ALLOWED_HOSTS=tu-app.onrender.com
```

### **3. Verificar Build Command:**

El Build Command debe ser:
```
Build Command: ./build.sh
```

## 🔍 **Verificación de la Solución**

### **Después del deploy, verifica:**

1. **Logs de Render:**
   - Ve a **"Logs"** en tu servicio
   - Busca mensajes de éxito o error

2. **Acceso a la aplicación:**
   - Visita tu URL: `https://tu-app.onrender.com`
   - Debería cargar sin errores

3. **Admin de Django:**
   - Ve a: `https://tu-app.onrender.com/admin/`
   - Debería mostrar la página de login

## 🚨 **Si el Error Persiste**

### **Opción A: Recrear el Servicio**

1. **Elimina** el Web Service actual
2. **Crea uno nuevo** con la configuración correcta
3. **Usa la Solución 3** desde el inicio

### **Opción B: Verificar Estructura del Proyecto**

En Render Shell, ejecuta:
```bash
ls -la
ls -la main/
cat main/main/wsgi.py
```

### **Opción C: Configuración Mínima**

Usa esta configuración mínima:
```
Build Command: pip install -r requirements.txt && python main/manage.py collectstatic --no-input
Start Command: cd /opt/render/project/src/main && gunicorn main.wsgi:application --bind 0.0.0.0:$PORT
```

## 📞 **Comandos de Debug**

### **En Render Shell:**

```bash
# Verificar directorio actual
pwd

# Verificar estructura
ls -la
ls -la main/

# Verificar variables de entorno
echo $DJANGO_SETTINGS_MODULE
echo $PYTHONPATH

# Probar importación manual
python -c "import main.settings; print('OK')"
```

## 🎯 **¿Por Qué Pasa Esto?**

- **Render usa Python 3.13** que puede tener diferentes comportamientos
- **La estructura de directorios** puede confundir a Gunicorn
- **El PYTHONPATH** necesita configuración específica
- **Los scripts de inicio** resuelven estos problemas

## ✅ **Resultado Esperado**

Después de aplicar la solución correcta:
- ✅ La aplicación carga sin errores
- ✅ Los logs muestran "Starting gunicorn"
- ✅ No hay errores de importación
- ✅ El admin de Django es accesible

---

**¡Una de estas soluciones debería resolver el problema! 🚀**
