import os
import sqlite3
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from groq import Groq

# Cargar variables desde properties.env
load_dotenv("properties.env")

print("GROQ KEY cargada:", os.getenv("GROQ_API_KEY") is not None)

# Cliente Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Flask
app = Flask(__name__)
CORS(app)

# ============================
#  SERVIR UI DESDE FRONTEND/
# ============================
@app.route("/")
def serve_ui():
    return send_from_directory("frontend", "index.html")

@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory("frontend", path)

# ============================
#        API /chat
# ============================
@app.post("/chat")
def chat():
    try:
        data = request.json
        mensaje = data.get("mensaje", "")

        # Leer base de datos
        conn = sqlite3.connect("database/asistente.db")
        cur = conn.cursor()
        cur.execute("SELECT nombre, entidad, tipo, tasa, minimo, descripcion FROM productos")
        productos = cur.fetchall()
        conn.close()

        # Convertir productos a texto
        productos_texto = "\n".join([
            f"- {p[0]} ({p[1]}): tipo {p[2]}, tasa {p[3]}%, mínimo RD${p[4]}, desc: {p[5]}"
            for p in productos
        ])

        # Llamar modelo Groq
        respuesta = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": f"""
Eres un asesor financiero llamado Beniz de República Dominicana.
Usa SOLO los productos listados a continuación.
NO inventes información.
Si te piden algo fuera del ámbito financiero, responde:
"Solo puedo ayudarte con temas financieros."
Sé claro, amable y conciso.

Productos disponibles:
{productos_texto}
"""
                },
                {"role": "user", "content": mensaje}
            ],
            max_tokens=200,
            temperature=0.4
        )

        texto = respuesta.choices[0].message.content
        return jsonify({"respuesta": texto})

    except Exception as e:
        print("Error en /chat:", e)
        return jsonify({"error": "Error al procesar la solicitud"}), 500


if __name__ == "__main__":
    app.run(debug=True)
