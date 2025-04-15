import requests
import time
import threading
from flask import Flask

TOKEN = '8117106897:AAFoO65atbMgrNgzORiBt4AHOSiFOuIWco8'
CHAT_ID = '1675335472'

# URL de búsqueda
URL = "https://zelucash.com/search?show=false&query=ultra&sort=M%C3%81S%20RELEVANTES"


# Función para consultar el producto
def verificar_disponibilidad():
    try:
        response = requests.get(URL)
        if "S23 Ultra" in response.text:
            mensaje = "📱 ¡Hay un S23 Ultra disponible en Zelucash!"
        else:
            mensaje = "🔍 No hay S23 Ultra por ahora."
        requests.get(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={mensaje}"
        )
    except Exception as e:
        print("Error:", e)


# Bucle de verificación cada 1 minuto
def iniciar_bot():
    while True:
        verificar_disponibilidad()
        time.sleep(60)  # cada 1 minuto


# 🔸 Servidor Flask para mantener vivo el bot en Replit
app = Flask(__name__)


@app.route('/')
def home():
    return "✅ El bot está corriendo correctamente."


# 🔸 Iniciar el bot y el servidor Flask al mismo tiempo
if __name__ == '__main__':
    threading.Thread(target=iniciar_bot).start()
    app.run(host='0.0.0.0', port=3000)
