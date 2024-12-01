import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()


for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)

#name of the output file and the location of new combined pdf is in outputFile

output_path = os.path.join("outputFile", "combinedDocuments.pdf")

merger.write(output_path)
merger.close()