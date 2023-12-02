# Uso
# python camara.py --rostro cascadas/haarcascade_frontalface_default.xml
# python camara.py --rostro cascadas/haarcascade_frontalface_default.xml --video video/EntrevistaTra.avi
from detector.detector_de_rostros import DetectorRostro
import argparse
import imutils
import cv2

# Construir el analizador de argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--rostro", required=True,
                help="ruta donde se encuentra la cascada de rostros")
ap.add_argument("-v", "--video", help="ruta donde se encuentra el video")
args = vars(ap.parse_args())

# Construir el detector de rostros
dr = DetectorRostro(args["rostro"])

# En caso no exista una ruta para el video, se usa la camara
if not args.get("video", False):
    camara = cv2.VideoCapture(0)
# En caso contrario, se carga el video
else:
    camara = cv2.VideoCapture(args["video"])

while True:
    # Recuperar el frame actual
    (grabbed, frame) = camara.read()

    # En el caso se este procesando un video y ya no se grabe un frame, se alcanzó el final del video
    if args.get("video") and not grabbed:
        break

    # Redimensionar el frame, convertirlo a escala de grises
    frame = imutils.resize(frame, width=600)
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar los rostros en el frame (imagen) y clonarla para dibujar en esta
    rectRostros = dr.detectar(gris, factorEscala=1.2,
                              vecMin=5, tamMin=(30, 30))
    clonFrame = frame.copy()

    # Bucle para dibujar los rectángulos en el clon
    for (fX, fY, fW, fH) in rectRostros:
        cv2.rectangle(clonFrame, (fX, fY), (fX+fW, fY+fH), (0, 255, 0), 2)

    # Mostrar los rostros detectados
    cv2.imshow("Rostros", clonFrame)

    # if se presiona la tecla 's', se termina el bucle
    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

# Liberar la cámara y cerrar cualquier ventana abierta
camara.release()
cv2.destroyAllWindows()
