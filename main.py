from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

def images_to_pdf(image_folder, output_pdf):
    # Obtener la lista de archivos de imagen en la carpeta especificada
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]

    # Crear el lienzo de PDF
    c = canvas.Canvas(output_pdf, pagesize=letter)

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        img = Image.open(image_path)
        
        # Ajustar el tamaño de la imagen para que quepa en una página de carta
        width, height = letter
        img_width, img_height = img.size
        aspect = img_width / float(img_height)
        
        if img_width > width:
            img_width = width
            img_height = width / aspect
        
        if img_height > height:
            img_height = height
            img_width = height * aspect
        
        # Posicionar la imagen en el centro de la página
        x = (width - img_width) / 2
        y = (height - img_height) / 2
        
        c.drawImage(image_path, x, y, width=img_width, height=img_height)
        c.showPage()  # Añadir una nueva página

    c.save()
    print(f'PDF guardado como {output_pdf}')

# Ejemplo de uso
image_folder = './img'
output_pdf = 'Doc.pdf'
images_to_pdf(image_folder, output_pdf)
