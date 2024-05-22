from glob import glob
from datetime import datetime
from PyPDF2 import PdfWriter, PdfReader

def merge_files():
    merger = PdfWriter()

    for filename in glob("files/merge/*.pdf", recursive=True):
        merger.append(filename)

    dt = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    file_merged = f'files/merge/merged_{dt}.pdf'
    
    merger.write(file_merged)
    merger.close()

    return file_merged

def split_files(start_page: int, end_page):
    for filename in glob("files/split/*.pdf", recursive=True):
        pdf = PdfReader(filename)

    merger = PdfWriter()

    for page in range(start_page - 1, end_page):
        current_page = pdf._get_page(page)
        merger.add_page(current_page)

    dt = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    file_splitted = f"files/split/splitted-{start_page}-{end_page}_{dt}.pdf"

    with open(file_splitted, "wb") as out:
        merger.write(out)

    return file_splitted