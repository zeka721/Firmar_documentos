import fitz  # PyMuPDF
import os

# Carpetas de trabajo
pdf_folder = r"C:\Users\Zeka\PycharmProjects\Firmar_documento\documentos"
image_path = r"C:\Users\Zeka\PycharmProjects\Firmar_documento\firma\firmas.jpg"
output_folder = r"C:\Users\Zeka\PycharmProjects\Firmar_documento\documentos_firmados"

# Crear la carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Función para obtener la posición de la firma
def get_image_rect(pdf_path):
    """Obtiene el tamaño de la primera página del PDF y define la región de inserción."""
    doc = fitz.open(pdf_path)
    page = doc[0]  # Primera página
    width, height = page.rect.width, page.rect.height  # Tamaño de la página
    rect = fitz.Rect(width - 450, height - 100, width - 150, height - 0)
    doc.close()
    return rect

# Procesar todos los PDFs en la carpeta
for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        doc = fitz.open(pdf_path)

        # Insertar la imagen en cada página
        rect = get_image_rect(pdf_path)
        for page in doc:
            page.insert_image(rect, filename=image_path)

        # Guardar en la carpeta "documentos_firmados"
        output_path = os.path.join(output_folder, f"mod_{filename}")
        doc.save(output_path)
        doc.close()

print("✅ Proceso completado. PDFs firmados guardados en:", output_folder)
