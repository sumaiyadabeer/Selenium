import openpyxl

path = "/home/string/Desktop/selenium_ide/SDET/WriteData.xlsx"

workbook = openpyxl.load_workbook(path)

sheet = workbook.active # workbook.get_sheet_by_name("Sheet1")


for r in range(1,6):
	for c in range(1, 4):
		sheet.cell(row = r, column = c).value = r+c



workbook.save(path)
	