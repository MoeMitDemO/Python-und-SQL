from win32com import client
import win32api
input_file = r'C:\Users\thequickblog\Desktop\Python session 2\tqb_sample.xlsx'
#give your file name with valid path 
output_file = r'C:\Users\thequickblog\Desktop\Python session 2\tqb_sample_output.pdf'
#give valid output file name and path
app = client.DispatchEx("Excel.Application")
app.Interactive = False
app.Visible = False
Workbook = app.Workbooks.Open(input_file)
try:
    Workbook.ActiveSheet.ExportAsFixedFormat(0, output_file)
except Exception as e:
    print("Failed to convert in PDF format.Please confirm environment meets all the requirements  and try again")
    print(str(e))
finally:
    Workbook.Close()
    app.Exit()