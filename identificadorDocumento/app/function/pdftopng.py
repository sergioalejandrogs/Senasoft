import os
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import shutil

# Definimos los términos clave para identificar cada tipo de texto

factura = "factura"

nota_credito = "credito"

nota_debito = "débito"

epicrisis = "epicrisis"

historia_clinica = "clinica"

copia_cedula = "cédula"

orden_pedido = "pedido"

orden_remision = "remision"

# Definimos las funciones que verifican si la palabra clave se encuentra dentro del texto

def contiene_palabra(palabra, texto):
    return palabra in texto

pdf = "repositorio/remison8.pdf"

repositorio = "repositorio/"

# Repositorio temporal en el que estarán las imágenes que serán leídas por tesseract-OCR
outputDir = "tempfiles/"

# Esta función nos permite convertir los archivos pdf a imágenes jpg para poder ser leídas mediante OCR y obtener el contenido en texto 

def convert(pdf, outputDir):

    # Verificamos la existencia del repositorio temporal
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    # Poppler PATH para poder utilizar la herramienta y convertir a imágenes
    pages = convert_from_path(pdf, poppler_path=r'C:/Program Files/poppler-0.68.0/bin')
    counter = 1

    # Este ciclo nos permite dividir en diferentes imágenes si corresponde en el archivo pdf
    for page in pages:
        myfile = outputDir + 'output' + str(counter) + '.jpg'
        counter +=1
        page.save(myfile, "JPEG")
        print(myfile)

        # Este código abre las imágenes creadas y las lee por medio de OCR para devolver el contenido en texto plano
        im = Image.open(myfile)
        
        # Importante usar el PATH de Tesseract antes de invocar la función image_to_string
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
        texto = pytesseract.image_to_string(im, lang= 'spa')
        
        # Imprimimos el texto resultante y lo cambiamos a minúsculas para evitar pérdida de información al hacer la verificación
        print(texto.lower())

        if contiene_palabra(nota_credito, texto.lower()):
            print("Es una nota de crédito")
        if contiene_palabra(nota_debito, texto.lower()):
            print("Es una nota de débito")
        if contiene_palabra(factura, texto.lower()):
            print("Es una factura")
        if contiene_palabra(copia_cedula, texto.lower()):
            print("Es una copia de cédula")
        if contiene_palabra(historia_clinica, texto.lower()):
            print("Es una historia clínica")
        if contiene_palabra(epicrisis, texto.lower()):
            print("Es una epicrisis")
        if contiene_palabra(orden_pedido, texto.lower()):
            print("Es una orden de pedido")
        if contiene_palabra(orden_remision, texto.lower()):
            print("Es una orden de remisión")

        if contiene_palabra(nota_credito, texto.lower()):
            shutil.move(pdf, "notas_de_credito/")
        elif contiene_palabra(nota_debito, texto.lower()):
            shutil.move(pdf, "notas_de_débito/")
        elif contiene_palabra(factura, texto.lower()):
            shutil.move(pdf, "facturas/")
        elif contiene_palabra(nota_credito, texto.lower()):
            shutil.move(pdf, "notas_de_crédito/")
        elif contiene_palabra(nota_debito, texto.lower()):
            shutil.move(pdf, "notas_de_débito/")
        elif contiene_palabra(copia_cedula, texto.lower()):
            shutil.move(pdf, "copias_de_cédulas/")
        elif contiene_palabra(historia_clinica, texto.lower()):
            shutil.move(pdf, "historias_clínicas/")
        elif contiene_palabra(epicrisis, texto.lower()):
            shutil.move(pdf, "epicrisis/")
        elif contiene_palabra(orden_pedido, texto.lower()):
            shutil.move(pdf, "ordenes_de_pedido/")
        elif contiene_palabra(orden_remision, texto.lower()):
            shutil.move(pdf, "ordenes_de_remisión/")
        else: 
            shutil.move(pdf, "indeterminado/")

        os.remove(myfile)

#for pdf in os.listdir(repositorio):
#    convert(pdf, outputDir)

convert(pdf, outputDir)