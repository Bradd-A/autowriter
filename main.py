import pyautogui
import time

# Abrir el archivo con la letra de la canción
with open("data.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

# Espera unos segundos para que tengas tiempo de seleccionar la ventana de WhatsApp Web
time.sleep(5)

# Recorrer cada línea del archivo y enviarla por WhatsApp
for linea in lineas:
    pyautogui.write(linea.strip())  # Escribe la línea, .strip() elimina saltos de línea adicionales
    pyautogui.press("enter")  # Envía la línea
    time.sleep(1)  # Pausa de 1 segundo entre líneas (ajústalo si es necesario)
