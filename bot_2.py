import pdfplumber
from vk import vk
day = " "
pach = "pdf.pdf"
def raspisanie(day,group):
    nomber = 0
    array = []
    mass_pach = vk()
    with pdfplumber.open(pach) as pdf:
        page = pdf.pages[0]
        table = page.extract_table()
        for i in range(1, 50):
            if day in str(table[i][0]):
                nomber = i
        index_group = table[1].index(group)
        for j in range(1, 9):
            array.append(table[nomber + j][index_group])
        return array
