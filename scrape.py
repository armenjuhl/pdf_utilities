from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import tempfile
from pdf2image import convert_from_path


# path = '12A Listen to the Mocking Bird'
# file_name = path[:-4]
import_directory = '/Users/macbookpro/Downloads/group1Pdfs'
output_filenames = dict()


def main():
    with os.scandir(import_directory) as it:
        for entry in it:
            if entry.name[-4:] == '.pdf':
                print('\n\n\nTRUE')
                new_file_name = entry.name[3:-4]

                try:
                    new_directory = f"/Users/macbookpro/Desktop/Clients/KRStringsWebsite/pdfScraper2.py/{new_file_name}".replace(' ', '')
                    os.mkdir(new_directory)
                except Exception:
                    pass
                try:
                    pdf_directory = f"/Users/macbookpro/Desktop/Clients/KRStringsWebsite/pdfScraper2.py/{new_file_name}/PDF".replace(' ', '')
                    os.mkdir(pdf_directory)
                except Exception:
                    pass
                try:
                    jpg_directory = f"/Users/macbookpro/Desktop/Clients/KRStringsWebsite/pdfScraper2.py/{new_file_name}/JPG".replace(' ', '')
                    os.mkdir(jpg_directory)
                except Exception:
                    pass

                split(entry.path, entry.name, pdf_directory)

                for i in output_filenames.values():
                    convert_pdf_to_jpg(i, jpg_directory)


def split(path, name_of_split, pdf_dir):
    pdf = PdfFileReader(path)
    first_pass = True

    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        if first_pass:
            output = f'{pdf_dir}/{name_of_split[3:-4]}_{pdf.getNumPages()}.pdf'.replace(' ', '')
            output_filenames[page] = output
        else:
            output = f'{pdf_dir}/{name_of_split[3:-4]}_{page}.pdf'.replace(' ', '')
            output_filenames[page] = output

        with open(output, 'wb+') as output_pdf:
            pdf_writer.write(output_pdf)

        first_pass = False


def convert_pdf_to_jpg(filename, jpg_dir):

    with tempfile.TemporaryDirectory() as path:
        images_from_path = convert_from_path(filename, output_folder=path, last_page=1, first_page=0)

    base_filename = os.path.splitext(os.path.basename(filename))[0] + '.jpg'

    save_dir = f'{jpg_dir}'

    for page in images_from_path:
        page.save(os.path.join(save_dir, base_filename), 'JPEG')


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        # information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        counter = 0
        pages = dict()

        while counter <= number_of_pages:
            pages[str(counter)] = pdf.getPage(counter)
            counter += 1

        for k, v in pages.items():
            pages[k] = v.extractText()

    for idx, val in enumerate(pages):
        write_path = f"./{file_name}page_{idx}.txt"
        write_file = open(write_path, 'w')
        write_file.write(val)

    txt = f"""
    {pages}
    """

    return txt


if __name__ == '__main__':
    main()
