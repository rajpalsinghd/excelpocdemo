from xlrd import open_workbook, XLRDError

def validate_excel_sheet(filename):
    try:
        open_workbook(filename)
    except XLRDError:
        return False
    else:
        return True

def read_excel_file(filename,col,factor=10):
 try:
  wb = open_workbook(filename) 
  sheet = wb.sheet_by_index(0) 
  sheet.cell_value(0, 0) 
  number_of_rows=sheet.nrows
  number_of_columns=sheet.ncols
  
  #save in another table
  for i in range(number_of_columns): 
    print(sheet.cell_value(0, i))
    
  to_read=number_of_rows-1
  current=1
  print(to_read)
  print(type(sheet.row_values(1)))
  while to_read!=0:
     records_to_insert=[]
     if to_read>factor:
       to_read=to_read-factor
       i=current
       current+=factor
       while i<current:
        records_to_insert.append({str(1):sheet.row_values(i)})
        i=i+1
     else:
       i=current
       current+=to_read
       while i<current:
        records_to_insert.append({str(1):sheet.row_values(i)})
        i=i+1
       to_read=0
     col.insert_many(records_to_insert,ordered=True)
 except Exception as e:
  print(e)
  print("Error in read_excel_file program")
