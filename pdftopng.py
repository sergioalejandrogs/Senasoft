import os
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

# repo_facturas = "facturas/"

# convert_from_path(pdf_path="../sample.pdf", poppler_path=r'C:/Program Files/poppler-0.68.0/bin')

# def convert(file, repo_facturas):
#     if not os.path.exists(repo_facturas):
#         os.makedirs(repo_facturas)

#     pages = convert_from_path(file, 500)
#     counter = 1

#     for page in pages:
#         myfile = repo_facturas + "output" + counter + ".jpg"
#         counter += 1
#         print(myfile)

# file = "../factura.pdf"

# convert(file, repo_facturas)

pdf = "sample.pdf"

pages = convert_from_path(pdf, poppler_path=r'C:/Program Files/poppler-0.68.0/bin')
img_file = pdf.replace(".pdf","")
count = 0

for page in pages:
    count +=1
    imagen = page.save('file-'+str(count)+'.jpg', 'JPEG')

    im = Image.open(imagen)

    text = pytesseract.image_to_string(im, lang = 'eng')

    print(text)