ASISTENTE VIRTUAL DE INVERSIONES - MVP (Python Flask + SQLite + Frontend)
========================================================================

Estructura del proyecto:
- app.py        -> Backend (Flask), sirve frontend y API
- db.py         -> Script para crear tablas SQLite
- seed.py       -> Inserta productos de ejemplo
- requirements.txt -> Dependencias
- /frontend/
    - index.html
    - styles.css
    - app.js
- /database/
    - asistente.db (generada tras correr db.py)

Cómo ejecutar en local (Linux / macOS / Windows con WSL / Windows con Python instalado):

1. Clonar o descargar el proyecto y navegar a la carpeta asistente_project:
   cd /path/to/asistente_project

2. Crear un entorno virtual (opcional pero recomendado):
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate    # Windows

3. Instalar dependencias:
   pip install -r requirements.txt

4. Crear la base de datos y tablas:
   python db.py

5. Cargar productos de ejemplo:
   python seed.py

6. Ejecutar el servidor:
   python app.py

7. Abrir en el navegador:
   http://localhost:5000

Notas:
- El frontend está servido por Flask (app.py). Si deseas servirlo separadamente, puedes abrir frontend/index.html pero algunas llamadas fetch a /api/ no funcionarán debido a CORS/file protocol.
- Puedes desplegar en servicios como Render, Railway o Vercel (backend debe estar en Render/Railway).