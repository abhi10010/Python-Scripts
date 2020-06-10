from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=15)

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
text = text.split(' ')

for i in range(0, len(text), 10):
    text_enter = ''
    for j in range(i, i+10):
        if j < len(text):
            text_enter = text_enter + text[j] + ' '
    pdf.cell(200, 10, txt = text_enter, ln = ln, align = 'C')

pdf.output("mypdf.pdf")
