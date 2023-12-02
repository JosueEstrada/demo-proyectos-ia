import cv2


class DetectorRostro:
    def __init__(self, rutaCascadaRostros):
        # Cargar el detector de rostros
        self.cascadaRostro = cv2.CascadeClassifier(rutaCascadaRostros)

    def detectar(self, imagen, factorEscala=1.1, vecMin=5, tamMin=(30, 30)):
        # Detectar los rostros de la imagen
        rects = self.cascadaRostro.detectMultiScale(
            imagen, scaleFactor=factorEscala, minNeighbors=vecMin, minSize=tamMin, flags=cv2.CASCADE_SCALE_IMAGE)
        # Devolver los rectangulos representado los cuadros en los que se enmarcan la imagen
        return rects
