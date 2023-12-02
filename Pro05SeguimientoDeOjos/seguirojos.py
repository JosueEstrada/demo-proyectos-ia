# Uso
# python seguirojos.py --rostros cascadas/haarcascade_frontalface_default.xml --ojos cascadas/haarcascade_eye.xml --video video/pareja.mp4
# python seguirojos.py --rostros cascadas/haarcascade_frontalface_default.xml --ojos cascadas/haarcascade_eye.xml

# Importar las librerías necesarias
from seguidorDeOjos import SeguidorOjos
import imutils
import argparse
import cv2

# Construir el analizador de argumentos y analizar los argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--rostros", required=True,
                help="ruta al clasificador de rostros")
ap.add_argument("-o", "--ojos", required=True,
                help="ruta al clasificador de ojos")
ap.add_argument("-v", "--video",
                help="ruta donde se ubica el video (opcional)")
args = vars(ap.parse_args())

# Seguidor de ojos
so = SeguidorOjos(args["rostros"], args["ojos"])

# Si no se especifica el video, se utiliza la cámara
if not args.get("video", False):
    camara = cv2.VideoCapture(0)
# De lo contrario, se utiliza el video
else:
    camara = cv2.VideoCapture(args["video"])

# Iterar en los cuadros del video
while True:
    # Obtener el frame actual
    (grabbed, frame) = camara.read()

    # Si se ha alcanzado el final del video, detenerse
    if args.get("video") and not grabbed:
        break

    # Redimensionar el cuadro, convertirlo a escala de grises y aplicarle un desenfoque gaussiano
    frame = imutils.resize(frame, width=900)
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostros y ojos en la imagen
    rects = so.seguir(gris)

    # Iterar en los rectángulos delimitadores de los rostros y ojos
    for rec in rects:
        cv2.rectangle(frame, ((rec[0]), rec[1]),
                      ((rec[2]), rec[3]), (0, 255, 0), 2)

    # Mostrar los rostros y ojos seguidos
    cv2.imshow("Seguimiento", frame)

    # Si se presiona la tecla "s", deja de ejecutarse el bucle
    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

# Liberar la cámara y cerrar todas las ventanas
camara.release()
cv2.destroyAllWindows()
