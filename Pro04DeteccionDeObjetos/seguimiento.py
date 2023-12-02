# Uso
# python seguimiento.py --video video/soldados.mp4

# Importar las librerías necesarios
import imutils
import numpy as np
import argparse
import time
import cv2

# Construir el analizador de argumentos y analizar los argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="ruta al archivo de video")
args = vars(ap.parse_args())

# Define el límite superior e inferior para que el color sea considerado "azul"
azulMin = np.array([100, 67, 0], dtype="uint8")
azulMax = np.array([255, 128, 50], dtype="uint8")

# Cargar el video
# camara = cv2.VideoCapture(0) # Para usar la cámara web
camara = cv2.VideoCapture(args["video"])

# Bucle
while True:
    # Tomar el fotograma actual
    (grabbed, fotograma) = camara.read()

    # Revisar si se alcanzó el final del video
    if not grabbed:
        break

    # Determinar los pixeles que caen dentro de los límites y luego difuminar la imagen binaria
    azul = cv2.inRange(fotograma, azulMin, azulMax)
    azul = cv2.GaussianBlur(azul, (3, 3), 0)

    # Encontrar contornos en la imagen binaria
    cnts = cv2.findContours(
        azul.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # Revisar si se encontró algún contorno
    if len(cnts) > 0:
        # Ordena los contornos y encuentra el más grande
        # Asumiremos que este contorno corresponde al área del objeto ázul
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

        # Calcular el cuadro delimitador (girado) alrededor del contorno y luego dibujarlo
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        cv2.drawContours(fotograma, [rect], -1, (0, 255, 0), 2)

    # Muestra el fotograma y la imagen binaria
    cv2.imshow("Fotograma", fotograma)
    cv2.imshow("Binaria", azul)

    # Si su máquina es rápida, puede mostrar los fotogramas en lo que parece ser un "avance rápido", ya que se muestran más de 32 fotogramas por segundo; un truco simple es simplemente dormir un poquito entre fotogramas; sin embargo, si su computadora es lenta, probablemente sería conveniente comentar esta línea.
    time.sleep(0.025)

    # Si se presiona la tecla "s", se rompe el bucle
    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

# Liberar la cámara y cerrar las ventanas abiertas
camara.release()
cv2.destroyAllWindows()
