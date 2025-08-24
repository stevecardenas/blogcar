# 🔧 Solución de Problemas - Render Deployment

## 🚨 Error: "ModuleNotFoundError: No module named 'main.settings'"

### **Problema:**
```
ModuleNotFoundError: No module named 'main.settings'
```

### **Causa:**
Gunicorn no puede encontrar el módulo de configuración de Django.

### **Solución:**

#### **Opción 1: Usar el script de inicio (Recomendado)**
```
Start Command: ./start.sh
```

#### **Opción 2: Comando directo con configuración**
```
Start Command: gunicorn main.main.wsgi:application --bind 0.0.0.0:$PORT --workers 2
```

#### **Opción 3: Comando con directorio específico**
```
Start Command: cd /opt/render/project/src && gunicorn main.main.wsgi:application --bind 0.0.0.0:$PORT
```

## 🚨 Error: "ImportError: No module named 'django'"

### **Problema:**
```
ImportError: No module named 'django'
```

### **Causa:**
Las dependencias no se instalaron correctamente.

### **Solución:**
1. Verificar que `requirements.txt` existe y contiene Django
2. Verificar que el `Build Command` es: `./build.sh`
3. Revisar los logs de build para errores de instalación

## 🚨 Error: "SECRET_KEY not set"

### **Problema:**
```
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.
```

### **Causa:**
La variable de entorno `SECRET_KEY` no está configurada.

### **Solución:**
Agregar en Environment Variables:
```
NOMBRE: SECRET_KEY
VALOR: w=16hGTv^tV5LAlSN^v&CnPMzOa1d3R8Mr8-%Qy%JZBycDL*EL
```

## 🚨 Error: "DisallowedHost at /"

### **Problema:**
```
DisallowedHost at /
Invalid HTTP_HOST header: 'tu-app.onrender.com'. You may need to add 'tu-app.onrender.com' to ALLOWED_HOSTS.
```

### **Causa:**
La variable `ALLOWED_HOSTS` no incluye tu dominio.

### **Solución:**
Agregar en Environment Variables:
```
NOMBRE: ALLOWED_HOSTS
VALOR: tu-app.onrender.com
```

## 🚨 Error: "Static files not found"

### **Problema:**
```
404 Not Found - Static files not loading
```

### **Causa:**
Los archivos estáticos no se recolectaron durante el build.

### **Solución:**
1. Verificar que `build.sh` contiene: `python main/manage.py collectstatic --no-input`
2. Verificar que `STATIC_ROOT` está configurado en `settings.py`
3. Verificar que WhiteNoise está configurado

## 🚨 Error: "Database connection failed"

### **Problema:**
```
django.db.utils.OperationalError: connection to server at "localhost" failed
```

### **Causa:**
Configuración de base de datos incorrecta.

### **Solución:**
1. **Para SQLite:** No necesitas `DATABASE_URL`
2. **Para PostgreSQL:** Verificar que `DATABASE_URL` está configurada correctamente

## 🔍 Verificación de Configuración

### **Variables de Entorno Requeridas:**
```bash
SECRET_KEY=w=16hGTv^tV5LAlSN^v&CnPMzOa1d3R8Mr8-%Qy%JZBycDL*EL
DEBUG=False
ALLOWED_HOSTS=tu-app.onrender.com
```

### **Comandos de Build y Start:**
```bash
Build Command: ./build.sh
Start Command: ./start.sh
```

### **Archivos Requeridos:**
- ✅ `requirements.txt`
- ✅ `build.sh`
- ✅ `start.sh`
- ✅ `runtime.txt`

## 🛠️ Comandos de Debug

### **Verificar estructura del proyecto:**
```bash
# En Render Shell
ls -la
ls -la main/
```

### **Verificar variables de entorno:**
```bash
# En Render Shell
echo $SECRET_KEY
echo $DEBUG
echo $ALLOWED_HOSTS
```

### **Probar Django:**
```bash
# En Render Shell
python main/manage.py check
python main/manage.py showmigrations
```

## 📞 Pasos de Emergencia

### **Si nada funciona:**

1. **Recrear el servicio:**
   - Eliminar el Web Service actual
   - Crear uno nuevo con la configuración correcta

2. **Verificar el repositorio:**
   - Asegurarse de que todos los archivos están en GitHub
   - Verificar que la rama `main` tiene los cambios

3. **Usar configuración mínima:**
   ```
   Build Command: pip install -r requirements.txt && python main/manage.py collectstatic --no-input
   Start Command: gunicorn main.main.wsgi:application --bind 0.0.0.0:$PORT
   ```

---

**¡La mayoría de errores se solucionan con la configuración correcta! 🎯**
