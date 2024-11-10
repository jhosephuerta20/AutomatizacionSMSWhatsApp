import pywhatkit as pwk
import time
import re

# Lee el archivo de números y mensajes
with open("contactos.txt", "r") as file:
    numeros = [line.strip() for line in file]

# Mensaje a enviar
mensaje = "Hola, este es un mensaje de prueba enviado automáticamente.  \n No responder   \n ¡Gracias por su atención! "

# Tiempo de espera entre mensajes para evitar bloqueo (en segundos)
intervalo_segundos = 15

# Expresión regular para verificar el formato de los números (ej. +521234567890)
formato_numero = re.compile(r'^\+?\d{10,15}$')

# Función para validar si el número es correcto
def es_numero_valido(numero):
    return bool(formato_numero.match(numero))

# Función para enviar mensajes
def enviar_mensajes():
    for numero in numeros:
        if not es_numero_valido(numero):
            print(f"El número {numero} no tiene un formato válido. Saltando...")
            continue

        try:
            # Aseguramos que WhatsApp Web esté completamente cargado
            print(f"Enviando mensaje a {numero}...")
            pwk.sendwhatmsg_instantly(numero, mensaje, wait_time=20, tab_close=False, close_time=3)
            print(f"Mensaje enviado a {numero}")

            # Agregar a un archivo de log para llevar un control
            with open("log_envios.txt", "a") as log_file:
                log_file.write(f"Mensaje enviado a {numero} - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

            # Espera entre mensajes
            time.sleep(intervalo_segundos)

        except Exception as e:
            print(f"Error al enviar mensaje a {numero}: {e}")
            # Agregar el error al log
            with open("log_envios.txt", "a") as log_file:
                log_file.write(f"Error al enviar mensaje a {numero} - {e} - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            continue

# Ejecuta el envío de mensajes
enviar_mensajes()
