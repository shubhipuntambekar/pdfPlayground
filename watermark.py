import PyPDF2


def add_watermark(input_file):
    template = PyPDF2.PdfFileReader(open(input_file, 'rb'))
    watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

    output = PyPDF2.PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open('watermark_output.pdf', 'wb') as file:
            output.write(file)


add_watermark('super.pdf')
