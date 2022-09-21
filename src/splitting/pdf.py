import os
import pathlib

from PyPDF2 import PdfFileReader, PdfFileWriter


def split(FILE_PATH, dest=None):

    # Check if file provided PDF file exists
    if not os.path.exists(FILE_PATH):
        raise FileNotFoundError(f"File {FILE_PATH} does not exist.")

    # Check/create the generated file save location
    if not dest:
        dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), pathlib.Path(FILE_PATH).stem)
    if not os.path.exists(dest):
        os.makedirs(dest)

    # Split the provided PDF into pages
    try:
        inputpdf = PdfFileReader(open(FILE_PATH, "rb"))
        numPages = inputpdf.numPages
        for i in range(numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open(os.path.join(dest, f"page{i+1}.pdf"), "wb") as outputStream:
                output.write(outputStream)
    except Exception as e:
        raise repr(e)
