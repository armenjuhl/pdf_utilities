import glob
from PyPDF2 import PdfFileWriter, PdfFileReader
from collections import OrderedDict
from math import floor


def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)


if __name__ == '__main__':
    paths = glob.glob('/Users/macbookpro/Desktop/Clients/KRStringsWebsite/pdfScraper2.py/ChristmasCarols/PDF/*ChristmasCarols.pdf')
    new_list = dict()
    for i in range(1, len(paths)): new_list[str(i)] = ''

    for i, v in enumerate(paths):
        int_checker = ''
        for j in v[86:88]:
            try:
                int(j)
                int_checker = int_checker + j
            except Exception:
                pass

        new_list[str(int_checker)] = v
        print('match found')
    final_list = OrderedDict(new_list.items())

    list_1 = list()
    list_2 = list()
    list_3 = list()
    list_4 = list()
    list_5 = list()
    final_dict_len = len(final_list)

    complete_list = {1: list_1, 2: list_2, 3: list_3, 4: list_4, 5: list_5}

    counter_a = 0
    counter_b = 1
    for i in final_list.items():
        if counter_a <= floor(final_dict_len / 5):
            complete_list[counter_b].append(i[1])
        else:
            counter_a = 0
            counter_b += 1
            complete_list[counter_b].append(i[1])

        counter_a += 1

    merger('christmas_carols_1.pdf', complete_list[1])
    merger('christmas_carols_2.pdf', complete_list[2])
    merger('christmas_carols_3.pdf', complete_list[3])
    merger('christmas_carols_4.pdf', complete_list[4])
    merger('christmas_carols_5.pdf', complete_list[5])

