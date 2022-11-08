# importando modulos necesarios
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors


file_name = 'reporte.pdf'

title_document = 'Reporte Validacion'

title = 'Información del Comprobante'


# creando un objeto pdf.
pdf = canvas.Canvas(file_name, pagesize=letter)
width, heigth = letter

# creando texto
pdf.drawString(240, heigth - 50, 'Informacion del Comprobante')

# creamos la linea para el titulo.
pdf.line(50,735,550,735)

text1 = pdf.beginText(50, heigth - 100)

text1.textLine("Resultado:")
text1.textLine("Tipo de Comprobante:")

pdf.drawText(text1)


text2 = pdf.beginText(400, heigth - 100)
version = '4.0'
text2.textLine("Versión: "+version)
text2.textLine("Folio: ")

pdf.drawText(text2)

# pdf.drawString(70, heigth - 100, 'Resultado: ')
# pdf.drawString(130, heigth - 100, 'Comprobante Invalido')


# ajuste del titulo del documento.
pdf.setTitle(title_document)

# terminar una pagina o terminar la pagina
pdf.showPage()

# guardamos el pdf
pdf.save()