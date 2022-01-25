Esta es nuestra solución al reto SENASOFT 2021 Vertical 2: reto financiero. 

¿Cómo identificar documentos escaneados que están en un repositorio y enviarlos a otro automáticamente, dependiendo del tipo de documento?

Para poder ejecutar esta solución es preciso tener instalado Python 3.0 o mayor y su web framework Django.

Instalar Tesseract desde este link: https://tesseract-ocr.github.io/tessdoc/
Posteriormente añadir C:\Program Files\Tesseract-OCR al PATH del sistema. *Esta es la dirección por defecto, pero puede cambiar

Instalar Poppler desde este link: https://blog.alivate.com.au/poppler-windows/
Posteriormente añadir C:\Program Files\poppler-0.68.0\bin al PATH del sistema. *Esta es la dirección por defecto, pero puede cambiar

En una terminal CMD instalar las siguientes librerías para Python:

  $ pip install PILLOW

  $ pip install pdf2image

  $ pip install pytesseract

Ahora sí es posible ejecutar el proyecto desde una terminal CMD en la carpeta identificadorDocumento/ al ejecutar el comando:

  $ python manage.py runserver

Para ejecutar el comando del aplicativo, desde la carpeta identificadorDocumento/app/function/ ejecutar el comando:

  $python repo.py

Al hacer esto, el servidor local clona el repositorio en Github https://github.com/sergioalejandrogs/repositorio con los documentos allí alojados y procede a realizar la reorganización de los documentos, para finalmente subirlos automáticamente, y ya organizados en sus respectivas carpetas, al repositorio de los documentos.

Sergio González
