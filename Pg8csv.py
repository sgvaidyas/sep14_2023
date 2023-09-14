import xlrd

workbook = xlrd.open_workbook('C:/Users/Administrator/Desktop/myfile.xls')

sheet = workbook.sheet_by_name("jan")

for i in range(4):
    for j in range(3):
        print(sheet.cell_value(i,j),end="\t")
    print()