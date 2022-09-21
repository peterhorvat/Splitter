import os
import pathlib
import xlwings


def split(FILE_PATH, dest=None):

    # Check if provided Excel file exists
    if not os.path.exists(FILE_PATH):
        raise FileNotFoundError(f"File {FILE_PATH} does not exist.")

    # Check/create the generated file save location
    if not dest:
        dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), pathlib.Path(FILE_PATH).stem)
    if not os.path.exists(dest):
        os.makedirs(dest)

    extension = pathlib.Path(FILE_PATH).suffix

    with xlwings.App(visible=False) as app:
        wb = xlwings.Book(FILE_PATH)
        for sheet in wb.sheets:
            wb_tmp = xlwings.Book()
            sheet.copy(after=wb_tmp.sheets[0])
            wb_tmp.save(os.path.join(dest, sheet.name + extension))
            wb_tmp.close()
        wb.close()
