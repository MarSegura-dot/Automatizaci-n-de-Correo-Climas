import requests
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv


load_dotenv()

def obtener_clima(ciudad, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperatura = data['main']['temp']
            descripcion = data['weather'][0]['description']
            return (temperatura, descripcion)
        else:
            print(f"Error al obtener el clima: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None
    

def enviar_email(remitente, password, destinatario, asunto, contenido):
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(contenido, 'plain'))
    
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remitente, password)
        servidor.send_message(mensaje)
        servidor.quit()
        print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

if __name__ == "__main__":
    API_KEY = os.getenv("API_KEY")
    CIUDAD = os.getenv("CIUDAD")
    CORREO_REMITENTE = os.getenv("CORREO_REMITENTE")
    CONTRASENA = os.getenv("CONSTRASENA")
    CORREO_DESTINATARIO = os.getenv("CORREO_DESTINATARIO")

    resultado_clima = obtener_clima(CIUDAD, API_KEY)
    if resultado_clima:
        temperatura, descripcion = resultado_clima
        asunto = f"Clima en {CIUDAD}"
        contenido = f"El clima actual en {CIUDAD} es de {temperatura}°C con {descripcion}."
        enviar_email(CORREO_REMITENTE, CONTRASENA, CORREO_DESTINATARIO, asunto, contenido)