"""
Configuración centralizada del proyecto.
- En local: lee las variables desde un archivo .env (requiere python-dotenv).
- En Replit: los secrets ya están inyectados como variables de entorno; dotenv es opcional.
"""

import os

try:
    from dotenv import load_dotenv
    load_dotenv()  # no hace nada si no hay .env — no lanza error
except ImportError:
    pass  # python-dotenv no instalado (Replit); las vars ya están en el entorno

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError(
        "La variable GROQ_API_KEY no está definida. "
        "En local: crea un archivo .env con GROQ_API_KEY=tu_clave. "
        "En Replit: añádela como Secret en la configuración del proyecto."
    )
