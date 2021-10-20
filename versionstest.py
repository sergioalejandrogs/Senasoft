from PIL import Image
import pytesseract
from pdf2image import convert_from_path

pdf_file = "../factura.pdf"

# images = convert_from_path(pdf_file, 500)

# img = Image.open(images)

# pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# text = pytesseract.image_to_string(img, lang = 'spa')

# print(text)

# pages = convert_from_path(pdf_file, 500)

# for page in pages:
#     page.save('out.png', 'PNG')


# import module
from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function

poppler_path = r"C:/Program Files/poppler-0.68.0/bin" 

images = convert_from_path('../factura.pdf')
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')

"""El de abajo sí funciona, falta cambiar formato de pdf a png y debería funcionar"""

# im = Image.open("sample1.jpg")

# text = pytesseract.image_to_string(im, lang = 'eng')

# print(text)