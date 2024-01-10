import xlrd

def readlocators(file_path,sheet_name ):
    workbook = xlrd.open_workbook(file_path)
    worksheet = workbook.sheet_by_name(sheet_name)
    rows = worksheet.get_rows()
    header = next(rows)
    data = {[row.value[0]] : (row.value[1],row.value[2]) for row in  rows}
    return data

