from fpdf import FPDF
from PIL import Image

name = input("Name: ")
#PDF
pdf = FPDF()
#IMG
img = Image.open("shirtificate.png")

#PDF Changes

pdf.add_page()
pdf.set_font("Helvetica", "",size=48)
pdf.image("shirtificate.png",y = 0.26*pdf.eph, h=0.70*pdf.eph, w=pdf.epw,)
pdf.multi_cell(align="C",text="CS50 Shirtificate",h=53,w=0)
pdf.set_font("Helvetica", "",size=24,)
pdf.set_text_color(255,255,255)
pdf.set_x(0)
pdf.multi_cell(align="C",text=name+" took CS50",h=130,w=0)
pdf.output("shirtificate.pdf")