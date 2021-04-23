from win32com import client
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
import sys,win32api

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()                  # Rufe die Klasse auf
        uic.loadUi('you.ui', self)        # Lade die UI Datei
        self.show()             



def selectSource():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(window, "QFileDialog.getOpenFileName()", "","All Files (*);;Excel-Dateien (*.xls*)", options=options)
    if fileName:
        print(fileName)
        window.quelleLineEdit.setText(fileName)
        
def selectDestination():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getSaveFileName(window,"QFileDialog.getSaveFileName()","","All Files (*);;PDF (*.pdf)", options=options)
    if fileName:
        print(fileName)
        window.zielLineEdit.setText(fileName)

def convert():
    print(window.zielLineEdit.text())
    input_file =  window.quelleLineEdit.text()
    #give your file name with valid path 
    # output_file = window.zielLineEdit.text()
    output_file = window.zielLineEdit.text()
    #give valid output file name and path
    app1 = client.DispatchEx("Excel.Application")
    app1.Interactive = False
    app1.Visible = False
    Workbook = app1.Workbooks.Open(input_file)
    try:
        Workbook.ActiveSheet.ExportAsFixedFormat(0, output_file)
    except Exception as e:
        print("Failed to convert in PDF format.Please confirm environment meets all the requirements  and try again")
        print(str(e))
    finally:
        Workbook.Close(True)


app = QtWidgets.QApplication(sys.argv)              # Erzeuge eine Instanz von QtWidgets.QApplication
window = Ui()                                       # Erzeuge eine Instanz unserer Klasse (Ui)

window.quelleButton.clicked.connect(selectSource)      # Legt fest, dass bei Knopfdruck auf "umrechnen" die Funktion "umrechnen()" ausgeführt wird
window.zielButton.clicked.connect(selectDestination)        # Legt fest, dass bei Knopfdruck auf "Info" die Funktion "zeigeInfo" ausgeführt wird
window.convertButton.clicked.connect(convert) 
app.exec_()                                         # Starte die Anwendung







