import cv2


class SeguidorOjos:
    def __init__(self, rutaCascadaRostros, rutaCascadaOjos):
        # Cargar el detector de rostros y ojos
        self.cascadaRostros = cv2.CascadeClassifier(rutaCascadaRostros)
        self.cascadaOjos = cv2.CascadeClassifier(rutaCascadaOjos)

    def seguir(self, imagen):
        # Detectar rostros en la imagen e inicializar la lista de rectángulos conteniendo los rostros y ojos
        rectsRostros = self.cascadaRostros.detectMultiScale(
            imagen, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        rects = []  # Rectángulos delimitadores

        # Iterar en los rectángulos delimitadores de los rostros
        for (rX, rY, rW, rH) in rectsRostros:
            # Extraer el rostro y actualizar la lista de rectángulos delimitadores
            rostrorect = imagen[rY:rY + rH, rX:rX + rW]
            rects.append((rX, rY, rX + rW, rY + rH))

            # Detectar ojos en el rostro
            rectsOjos = self.cascadaOjos.detectMultiScale(
                rostrorect, scaleFactor=1.1, minNeighbors=10, minSize=(20, 20), flags=cv2.CASCADE_SCALE_IMAGE)

            # Iterar en los rectángulos delimitadores de los ojos
            for (oX, oY, oW, oH) in rectsOjos:
                # Actualizar la lista de rectángulos delimitadores
                rects.append((rX + oX, rY + oY, rX + oX + oW, rY + oY + oH))
        # Devuelve los rectángulos delimitadores de los rostros y ojos
        return rects
