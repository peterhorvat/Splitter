import argparse
import os.path

from PyPDF2 import PdfFileWriter, PdfFileReader


def pdfProcess(FILE_PATH, dest=None):

    # Check if file provided PDF file exists
    if not os.path.exists(FILE_PATH):
        print(f"File {FILE_PATH} does not exist.")
        return

    # Check/create the generated file save location
    if not dest:
        dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"split_pdf")
    if not os.path.exists(dest):
        os.makedirs(dest)

    # Split the provided PDF into pages
    try:
        inputpdf = PdfFileReader(open(FILE_PATH, "rb"))
        numPages = inputpdf.numPages
        for i in range(numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open(os.path.join(dest, f"page{i}.pdf"), "wb") as outputStream:
                output.write(outputStream)
        print(f"{numPages} files have been saved to {dest}.")
    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="PDFsplitter generates separate PDF files for each page",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("src", help="PDF file location")
    parser.add_argument("--dest", help="Destination to save the generated files")

    args = parser.parse_args()
    pdfProcess(args.src, dest=args.dest)
