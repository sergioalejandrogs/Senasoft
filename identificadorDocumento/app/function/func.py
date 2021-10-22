from django.shortcuts import render
import os
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import shutil

# Definimos los términos clave para identificar cada tipo de texto

factura = "factura"

nota_credito1 = "credito"
nota_credito2 = "crédito"

nota_debito1 = "débito"
nota_debito2 = "debito"

epicrisis = "epicrisis"

historia_clinica1 = "clinica"
historia_clinica2 = "clínica"

copia_cedula1 = "cédula"
copia_cedula2 = "cedula"

orden_pedido = "pedido"

orden_remision1 = "remision"
orden_remision2 = "remisión"


# Establecemos los directorios a los que van a ir los archivos

creditos_rep = "notas_de_crédito/"

debitos_rep = "notas_de_débito/"

facturas_rep = "facturas/"

epicrisis_rep = "epicrisis/"

historias_clinicas_rep = "historias_clínicas/"

copias_cedulas_rep = "copias_de_cédulas/"

ordenes_pedidos_rep = "ordenes_de_pedido/"

ordenes_remisiones_rep = "ordenes_de_remisión/"

indeterminados = "indeterminados/"

# Definimos las funciones que verifican si las palabras clave se encuentran dentro del texto

def contiene_palabra(palabra, texto):
    return palabra in texto

def contiene_palabras(palabra1, palabra2, texto):
    return palabra1 or palabra2 in texto

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
    #counter = 1

    # Este ciclo nos permite dividir en diferentes imágenes, si corresponde, del archivo pdf
    for page in pages:
        myfile = outputDir + 'output' + '.jpg'
        #counter +=1
        page.save(myfile, "JPEG")
        print(myfile)

        # Este código abre las imágenes creadas y las lee por medio de OCR para devolver el contenido en texto plano
        im = Image.open(myfile)
        
        # Importante usar el PATH de Tesseract antes de invocar la función image_to_string 
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
        texto = pytesseract.image_to_string(im, lang= 'spa')
        
        # Imprimimos el texto resultante y lo cambiamos a minúsculas para evitar pérdida de información al hacer la verificación
        print(texto.lower())

        #Estas líneas de código son innecesarias, sólo están para mostrar cómo se va ejecutando el código por medio de la terminal

        if contiene_palabra(epicrisis, texto.lower()):
            print("Es una epicrisis")
        elif contiene_palabra(historia_clinica1, texto.lower()):
            print("Es una historia clínica")
        elif contiene_palabra(historia_clinica2, texto.lower()):
            print("Es una historia clínica")
        elif contiene_palabra(orden_pedido, texto.lower()):
            print("Es una orden de pedido")
        elif contiene_palabra(orden_remision1, texto.lower()):
            print("Es una orden de remisión")
        elif contiene_palabra(orden_remision2, texto.lower()):
            print("Es una orden de remisión")
        elif contiene_palabra(nota_credito1, texto.lower()):
            print("Es una nota de crédito")
        elif contiene_palabra(nota_credito2, texto.lower()):
            print("Es una nota de crédito")
        elif contiene_palabra(factura, texto.lower()):
            print("Es una factura")
        elif contiene_palabra(nota_debito1, texto.lower()):
            print("Es una nota de débito")
        elif contiene_palabra(nota_debito2, texto.lower()):
            print("Es una nota de débito")        
        elif contiene_palabra(copia_cedula1, texto.lower()):
            print("Es una copia de cédula")
        elif contiene_palabra(copia_cedula2, texto.lower()):
            print("Es una copia de cédula")
        else: print("Es indeterminado")

        if contiene_palabra(epicrisis, texto.lower()):
            if not os.path.exists(epicrisis_rep):
                os.makedirs(epicrisis_rep)
            shutil.move(pdf, epicrisis_rep)
        elif contiene_palabra(historia_clinica1, texto.lower()):
            if not os.path.exists(historias_clinicas_rep):
                os.makedirs(historias_clinicas_rep)
            shutil.move(pdf, historias_clinicas_rep)
        elif contiene_palabra(historia_clinica2, texto.lower()):
            if not os.path.exists(historias_clinicas_rep):
                os.makedirs(historias_clinicas_rep)
            shutil.move(pdf, historias_clinicas_rep)
        elif contiene_palabra(orden_pedido, texto.lower()):
            if not os.path.exists(ordenes_pedidos_rep):
                os.makedirs(ordenes_pedidos_rep)
            shutil.move(pdf, ordenes_pedidos_rep)
        elif contiene_palabra(orden_remision1, texto.lower()):
            if not os.path.exists(ordenes_remisiones_rep):
                os.makedirs(ordenes_remisiones_rep)
            shutil.move(pdf, ordenes_remisiones_rep)
        elif contiene_palabra(orden_remision2, texto.lower()):
            if not os.path.exists(ordenes_remisiones_rep):
                os.makedirs(ordenes_remisiones_rep)
            shutil.move(pdf, ordenes_remisiones_rep)
        elif contiene_palabra(nota_credito1, texto.lower()):
            if not os.path.exists(creditos_rep):
                os.makedirs(creditos_rep)
            shutil.move(pdf, creditos_rep)
        elif contiene_palabra(nota_credito2, texto.lower()):
            if not os.path.exists(creditos_rep):
                os.makedirs(creditos_rep)
            shutil.move(pdf, creditos_rep)
        elif contiene_palabra(factura, texto.lower()):
            if not os.path.exists(facturas_rep):
                os.makedirs(facturas_rep)
            shutil.move(pdf, facturas_rep)
        elif contiene_palabra(nota_debito1, texto.lower()):
            if not os.path.exists(debitos_rep):
                os.makedirs(debitos_rep)
            shutil.move(pdf, debitos_rep)  
        elif contiene_palabra(nota_debito2, texto.lower()):
            if not os.path.exists(debitos_rep):
                os.makedirs(debitos_rep)
            shutil.move(pdf, debitos_rep)        
        elif contiene_palabra(copia_cedula1, texto.lower()):
            if not os.path.exists(copias_cedulas_rep):
                os.makedirs(copias_cedulas_rep)
            shutil.move(pdf, copias_cedulas_rep)
        elif contiene_palabra(copia_cedula2, texto.lower()):
            if not os.path.exists(copias_cedulas_rep):
                os.makedirs(copias_cedulas_rep)
            shutil.move(pdf, copias_cedulas_rep)
        else: 
            if not os.path.exists(indeterminados):
                os.makedirs(indeterminados)            
            shutil.move(pdf, indeterminados)

        os.remove(myfile)

# Por último, el ciclo siguiente efectúa la función para todos los archivos que se encuentran dentro del repositorio

for pdf in os.scandir(repositorio):
    convert(pdf, outputDir)