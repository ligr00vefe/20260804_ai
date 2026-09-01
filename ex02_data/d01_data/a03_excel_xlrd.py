import xlrd
#  terminal에서 pip install xlrd

workbook = xlrd.open_workbook('../source/singer.xls')
print('워크시트는 %d개 입니다' % (workbook.nsheets))
rowCount = 0
groupTot = 0

for worksheet in workbook.sheets() :
    print('** 워크시트의 이름 : %s' % (worksheet.name) )
    print(" 행 수는 %d, 열 개수는 %d 입니다." % (worksheet.nrows, worksheet.ncols))
    rowCount += worksheet.nrows-1
    for row in range(worksheet.nrows):
      if worksheet.cell_value(row, 2) != "인원":
        groupTot += int(worksheet.cell_value(row, 2))
      for col in range(worksheet.ncols):
        print("%s" % worksheet.cell_value(row, col), end='\t')
      print()
    print()

print("전체 그룹 수: ", rowCount)
print("전체 인원 수: ", groupTot)
print("전체 그룹 평균 인원수: ", groupTot / rowCount)