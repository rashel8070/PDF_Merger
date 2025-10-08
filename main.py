from PyPDF2 import PdfMerger
import sys
import os

merger = PdfMerger()

output_file_name = "Merged.pdf"

for filename in os.listdir(os.curdir):
    if filename.endswith(".pdf") and filename != output_file_name:
        merger.append(filename)

merger.write(output_file_name)
merger.close()
print("pdf merge completed")