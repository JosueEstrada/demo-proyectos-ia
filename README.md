# Proyectos Demo de Visión por Computadora en Python

Este repositorio contiene 6 proyectos de Python relacionados con diferentes aplicaciones de visión por computadora para el desarrollo del examen final del curso de Inteligencia Artificial. A continuación se describen brevemente cada uno de ellos:

## Índice

- [Contador de Monedas](#contador-de-monedas)
- [Detección de Rostros](#detección-de-rostros)
- [Detección de Rostros en tiempo real](#detección-de-rostros-en-tiempo-real)
- [Detección de Objetos](#detección-de-objetos)
- [Seguimiento de Ojos](#seguimiento-de-ojos)
- [Reconocimiento de Dígitos](#reconocimiento-de-dígitos)
- [Atribución](#atribución)

## Contador de Monedas

Este proyecto utiliza técnicas de procesamiento de imágenes para contar el número de monedas en una imagen. Puede ser útil en aplicaciones de contabilidad o análisis financiero.

Este script de Python, `contador_monedas.py`, utiliza la biblioteca OpenCV para contar el número de monedas en una imagen.

### Dependencias

El script requiere las siguientes bibliotecas de Python:

- numpy
- argparse
- imutils
- cv2 (OpenCV)

Puedes instalar estas con pip:

```bash
pip install numpy argparse imutils opencv-python
```

### Uso

Puedes ejecutar el script desde la línea de comandos con el siguiente comando:

```bash
python contador_monedas.py --imagen <ruta_a_tu_imagen>
```

Reemplaza `<ruta_a_tu_imagen>` con la ruta al archivo de imagen que deseas procesar.

### Cómo funciona

El script funciona de la siguiente manera:

1. Carga la imagen y la convierte a escala de grises.
2. Aplica un desenfoque gaussiano a la imagen en escala de grises.
3. Utiliza el método de detección de bordes Canny para encontrar los bordes en la imagen.
4. Encuentra los contornos en la imagen detectada por bordes. Cada contorno debería corresponder a una moneda.
5. Cuenta el número de contornos (monedas) e imprime este número.
6. Dibuja círculos verdes alrededor de las monedas en la imagen original y muestra esta imagen.
7. Para cada moneda, extrae la moneda de la imagen, la guarda como una imagen separada y la muestra. También crea una máscara para la moneda y muestra la moneda con esta máscara aplicada.

### Nota

> Este script asume que todas las monedas en la imagen están separadas y pueden ser encerradas individualmente en un contorno. Si las monedas se superponen o tocan, el script podría contarlas como una sola moneda.

## Detección de Rostros

Este proyecto utiliza algoritmos de detección de rostros para identificar y delimitar las caras en una imagen. Puede ser utilizado en aplicaciones de reconocimiento facial o análisis de emociones.

Este script, `deteccion_rostros.py`, es un programa de Python que utiliza OpenCV para detectar rostros en una imagen.

### Dependencias

El script requiere las siguientes bibliotecas de Python:

- numpy
- argparse
- imutils
- cv2 (OpenCV)

Puedes instalar estas con pip:

```bash
pip install numpy argparse imutils opencv-python
```

### Uso

Puedes ejecutar el script desde la línea de comandos con el siguiente comando:

```bash
python deteccion_rostros.py --rostro cascadas/haarcascade_frontalface_default.xml --imagen <ruta_a_tu_imagen>
```

Reemplaza `<ruta_a_tu_imagen>` con la ruta al archivo de imagen que deseas procesar.

### Cómo funciona

El script funciona de la siguiente manera:

1. Carga la imagen y la convierte a escala de grises.
2. Carga el archivo XML de Haar Cascade para la detección de rostros.
3. Aplica la detección de rostros a la imagen en escala de grises.
4. Para cada rostro detectado, dibuja un rectángulo alrededor del rostro en la imagen original.
5. Muestra la imagen original con los rostros resaltados.

### Nota

> Este script utiliza el clasificador en cascada Haar para la detección de rostros, que es un enfoque efectivo para la detección de objetos en imágenes. Sin embargo, puede no funcionar bien en todas las situaciones, especialmente si los rostros en la imagen están inclinados o parcialmente ocultos.

## Detección de Rostros en tiempo real

Este proyecto utiliza una cámara web para detectar y delimitar rostros en tiempo real. Puede ser utilizado en aplicaciones de videovigilancia o interacción humano-computadora.

Este script, `camara.py`, es un programa de Python que utiliza OpenCV para detectar rostros en tiempo real a través de la cámara de tu dispositivo. Además, se utiliza una clase `DetectorRostro` para encapsular la funcionalidad de detección de rostros.

### Clase DetectorRostro

La clase `DetectorRostro` se encarga de cargar el detector de rostros y de aplicar la detección de rostros a una imagen.

### Dependencias

El script requiere las siguientes bibliotecas de Python:

- argparse
- numpy
- cv2 (OpenCV)

Puedes instalar estas con pip:

```bash
pip install argparse numpy opencv-python
```

### Uso

Puedes ejecutar el script desde la línea de comandos con el siguiente comando:

```bash
python camara.py
```

### Cómo funciona

El script funciona de la siguiente manera:

1. Abre la cámara de tu dispositivo.
2. En un bucle, captura frames de la cámara y los convierte a escala de grises.
3. Aplica la detección de rostros a cada frame en escala de grises utilizando la clase `DetectorRostro`.
4. Para cada rostro detectado, dibuja un rectángulo alrededor del rostro en el frame original.
5. Muestra el frame original con los rostros resaltados.
6. Si se presiona la tecla 's', se termina el bucle.
7. Al final, libera la cámara y cierra cualquier ventana abierta.

### Nota

> Este script utiliza la cámara de tu dispositivo para detectar rostros en tiempo real. Asegúrate de tener los permisos necesarios para acceder a la cámara antes de ejecutar el script.

## Detección de Objetos

Este proyecto utiliza algoritmos de visión por computadora para detectar y clasificar objetos en una imagen. Puede ser utilizado en aplicaciones de reconocimiento de objetos o automatización industrial.

Este script, `seguimiento.py`, es un programa de Python que utiliza OpenCV para seguir un objeto de color específico en un video.

### Dependencias

El script requiere las siguientes bibliotecas de Python:

- imutils
- numpy
- argparse
- cv2 (OpenCV)

Puedes instalar estas con pip:

```bash
pip install imutils numpy argparse opencv-python
```

### Uso

Puedes ejecutar el script desde la línea de comandos con el siguiente comando:

```bash
python seguimiento.py --video <ruta_a_tu_video>
```

Reemplaza `<ruta_a_tu_video>` con la ruta al archivo de video que deseas procesar.

### Cómo funciona

El script funciona de la siguiente manera:

1. Carga el video.
2. En un bucle, captura frames del video.
3. Para cada frame, aplica una máscara que solo permite pasar los píxeles que están en el rango de color definido.
4. Encuentra los contornos en la imagen enmascarada.
5. Dibuja un rectángulo alrededor del contorno más grande (que debería ser el objeto de color que se está siguiendo) en el frame original.
6. Muestra el frame original con el objeto de color resaltado.

### Nota

> Este script está configurado para seguir objetos de color azul. Puedes cambiar los valores de `azulMin` y `azulMax` para seguir objetos de otro color.

## Seguimiento de Ojos

Este proyecto utiliza técnicas de seguimiento ocular para rastrear y analizar los movimientos de los ojos en una imagen o video. Puede ser utilizado en aplicaciones de investigación de la visión o interfaces de usuario basadas en la mirada.

Este script, `seguirojos.py`, es un programa de Python que utiliza OpenCV para seguir ojos en tiempo real a través de la cámara de tu dispositivo. Además, se utiliza una clase `SeguidorOjos` para encapsular la funcionalidad de detección de rostros y ojos.

### Clase SeguidorOjos

La clase `SeguidorOjos` se encarga de cargar los detectores de rostros y ojos, y de aplicar la detección a una imagen.

### Dependencias

El script requiere las siguientes bibliotecas de Python:

- argparse
- cv2 (OpenCV)
- imutils

Puedes instalar estas con pip:

```bash
pip install argparse opencv-python imutils
```

### Uso

Puedes ejecutar el script desde la línea de comandos con el siguiente comando:

```bash
python seguirojos.py --rostros cascadas/haarcascade_frontalface_default.xml --ojos cascadas/haarcascade_eye.xml
```

Utilizar un video desde una ruta

```bash
python seguirojos.py --rostros cascadas/haarcascade_frontalface_default.xml --ojos cascadas/haarcascade_eye.xml --video video/pareja.mp4
```

### Cómo funciona

El script funciona de la siguiente manera:

1. Abre la cámara de tu dispositivo.
2. En un bucle, captura frames de la cámara.
3. Para cada frame, aplica la detección de rostros y ojos utilizando la clase `SeguidorOjos`.
4. Para cada ojo detectado, aplica una máscara que delimita el ojo en el rostro
5. Encuentra los contornos en la imagen enmascarada.
6. Dibuja un rectángulo alrededor de cada contorno (que debería ser un ojo) en el frame original.
7. Muestra el frame original con los ojos resaltados.
8. Si se presiona la tecla 's', se termina el bucle.
9. Al final, libera la cámara y cierra cualquier ventana abierta.

### Nota

> Este script utiliza la cámara de tu dispositivo para detectar ojos rojos en tiempo real. Asegúrate de tener los permisos necesarios para acceder a la cámara antes de ejecutar el script.

## Reconocimiento de Dígitos

Este proyecto utiliza algoritmos de aprendizaje automático para reconocer y clasificar dígitos escritos a mano. Puede ser utilizado en aplicaciones de reconocimiento de caracteres o procesamiento de formularios.

Este script, `classify.py`, es un programa de Python que utiliza un modelo de aprendizaje automático para clasificar una imagen.

### Dependencias

El script requiere las siguientes bibliotecas de Python:

- joblib
- imutils
- argparse
- mahotas
- cv2 (OpenCV)

Puedes instalar estas con pip:

```bash
pip install joblib imutils argparse mahotas opencv-python
```

### Uso

Puedes ejecutar el script desde la línea de comandos con el siguiente comando:

```bash
python classify.py --model <ruta_al_modelo> --image <ruta_a_la_imagen>
```

Reemplaza `<ruta_al_modelo>` con la ruta al archivo del modelo de aprendizaje automático que deseas usar, y `<ruta_a_la_imagen>` con la ruta a la imagen que deseas clasificar.

### Cómo funciona

El script funciona de la siguiente manera:

1. Carga el modelo de aprendizaje automático.
2. Inicializa el descriptor HOG (Histogram of Oriented Gradients).
3. Carga la imagen y la convierte a escala de grises.
4. Desenfoca la imagen, encuentra los bordes y luego encuentra los contornos a lo largo de las regiones con bordes.
5. Ordena los contornos basándose en su posición en el eje x, asegurándose de que se lean los números de izquierda a derecha.
6. Recorre los contornos y para cada uno, calcula el cuadro delimitador para el rectángulo.
7. Si el ancho es de al menos 7 píxeles y la altura es de al menos 20 píxeles, el contorno es probablemente un dígito.
8. Recorta la ROI y luego aplica un umbral a la ROI en escala de grises para revelar el dígito.
9. Desvía la imagen y centra su extensión.
10. Describe la imagen y la clasifica.
11. Dibuja un rectángulo alrededor del dígito y muestra qué se clasificó como el dígito.
12. Muestra la imagen y espera una pulsación de tecla.

### Nota

> Este script requiere un modelo de aprendizaje automático preentrenado. Asegúrate de tener un modelo válido antes de ejecutar el script.

---

Cada proyecto se encuentra en una carpeta separada dentro de este repositorio. Por favor, consulte la documentación y los archivos de código fuente de cada proyecto para obtener más información y detalles de implementación.

## Atribución

Este código no es de mi autoría original. Fue proporcionado por mi profesor a través de videos de enseñanza. Mi contribución a este proyecto ha sido copiar el código, agregar comentarios explicativos y documentar el código para su comprensión y uso. Agradezco a mi profesor por proporcionar el material original y permitirme usarlo en este repositorio.
