import argparse
import os.path

from PyPDF2 import PdfFileWriter, PdfFileReader


def pdfProcess(FILE_PATH, dest=None):
    if not os.path.exists(FILE_PATH):
        print(f"File {FILE_PATH} does not exist")
        return
    inputpdf = PdfFileReader(open(FILE_PATH, "rb"))
    if dest and not os.path.exists(dest):
        os.makedirs(dest)
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open(os.path.join(dest, f"page{i}.pdf"), "wb") as outputStream:
            output.write(outputStream)
    print(f"Files have been saved to {os.path.dirname(FILE_PATH) if not dest else dest}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="PDFsplitter generates separate PDF files for each page",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("src", help="PDF file location")
    parser.add_argument("--dest", help="Destination to save the generated files")

    args = parser.parse_args()
    pdfProcess(args.src, dest=args.dest)
