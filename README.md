# 🐙 OctopusIcons - Generador de Assets Web

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?logo=flask)
![Docker](https://img.shields.io/badge/Docker-✔-blue?logo=docker)

Aplicación para generar favicons, logos y archivos de configuración para PWAs a partir de un PNG.

## 🚀 Características
- 🖼️ Convierte PNG a favicon.ico y múltiples tamaños
- 📦 Genera `manifest.json` y plantilla HTML automáticamente
- ⚡ Progressive Web App (PWA) lista para instalar
- 🐳 Despliegue con Docker optimizado

## 🛠️ Variables de Entorno

| Variable              | Valor por Defecto       | Descripción                              |
|-----------------------|-------------------------|------------------------------------------|
| **`PORT`**            | `5001`                  | Puerto del servidor                      |
| **`HOST`**           | `0.0.0.0`               | Host de escucha                          |
| **`DEBUG`**          | `False`                 | Modo debug (no usar en producción)       |
| **`FLASK_ENV`**      | `production`            | Entorno: `production` o `development`    |
| **`APP_NAME`**       | `OctopusIcons`          | Nombre de la aplicación                  |
| **`SECRET_KEY`**     | `dev-key-insecure-...`  | Clave secreta para sesiones              |
| **`MAX_CONTENT_LENGTH`**| `16` (MB)            | Tamaño máximo de archivos subidos        |

## 🐳 Despliegue con Docker

### 1. Construir la imagen
```bash
docker-compose build
```

### 2. Iniciar los servicios
```bash
docker-compose up -d
```

### Estructura de archivos clave
```
├── Dockerfile              # Configuración multi-etapa para producción
├── docker-compose.yml      # Orquestación con healthchecks
├── .env                    # Variables de entorno (NO versionar)
└── nginx/                  # Configuración opcional para proxy inverso
```

### Configuración de producción
1. Crea un archivo `.env.prod`:
   ```ini
   FLASK_ENV=production
   SECRET_KEY=tu_clave_secreta_aqui
   PORT=8000
   ```
2. Usa compose para producción:
   ```bash
   docker-compose -f docker-compose.yml --env-file .env.prod up -d
   ```

## 🏗️ Estructura del Proyecto
```
assets_generator/
├── core/                   # Lógica principal de generación
├── server/                 # Rutas y configuración Flask
├── static/                 # Assets PWA (icons, CSS, JS)
├── templates/              # Plantillas Jinja2
└── tests/                  # Pruebas unitarias
```

## 🌐 Uso como PWA
1. Accede a la app desde un dispositivo móvil
2. Haz clic en "Añadir a la pantalla de inicio" (Android/Chrome)
3. Funciona offline gracias al Service Worker

## 💻 Desarrollo
```bash
# Instalar dependencias
pip install -r requirements.txt

# Iniciar servidor de desarrollo
flask run --port 5001
```

## 📄 Licencia
MIT © [Gabriel Baute](https://github.com/gabrielbaute)
```

---