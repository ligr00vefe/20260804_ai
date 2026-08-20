from shutil import which

import xlrd
import xlwt
#  pip install xlwt

in_workbook = xlrd.open_workbook('../source/singer.xls')
out_workbook = xlwt.Workbook()

# 해당 엑셀 파일을 읽어서 새로운 엑셀파일에 저장.
wsheetList = in_workbook.sheets()
for worksheet in wsheetList :
  outsheet = out_workbook.add_sheet(worksheet.name)
  for row in range(worksheet.nrows):
    for col in range(worksheet.ncols):
      outsheet.write(row, col, worksheet.cell_value(row, col))
out_workbook.save('../source/singer_out.xls')


wsheetList = in_workbook.sheets()
worksheet = wsheetList[0]
# 출력하고자 하는 시트의 제목만 입력하는 부분
outSheet = out_workbook.add_sheet("singer")
for col in range(worksheet.ncols):
  outSheet.write(0, col, worksheet.cell_value(0, col))

totalRow = 0
for worksheet in wsheetList:
  for row in range(1, worksheet.nrows):
    if int(worksheet.cell_value(row, 4)) >= 165:
      totalRow += 1
      for col in range(worksheet.ncols):
        outSheet.write(totalRow, col, worksheet.cell_value(row, col))

out_workbook.save('../source/singer_out_165.xls')
print("Save. OK~")