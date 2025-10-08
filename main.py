from PyPDF2 import PdfMerger
import sys
import os

merger = PdfMerger()


for filename in os.listdir(os.curdir):
    if filename.endswith(".pdf"):
        merger.append(filename)

merger.write("Combined.pdf")
merger.close()
print("pdf merge completed")