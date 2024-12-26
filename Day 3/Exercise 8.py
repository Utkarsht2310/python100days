# Merging pdf files
from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["dummy2.pdf", "sample1.pdf", "sample-pdf3.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()