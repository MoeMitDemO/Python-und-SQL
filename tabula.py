from win32com import client
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
import sys,win32api

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()                  # Rufe die Klasse auf
        uic.loadUi('yo.ui', self)        # Lade die UI Datei
        self.show()             



def selectSource():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(window, "QFileDialog.getOpenFileName()", "","All Files (*);;Excel-Dateien (*.xls*)", options=options)
    if fileName:
        print(fileName)
        window.quelleLineEdit.setText(fileName)

def convert():
    print("convert")
    

app = QtWidgets.QApplication(sys.argv)              # Erzeuge eine Instanz von QtWidgets.QApplication
window = Ui()                                       # Erzeuge eine Instanz unserer Klasse (Ui)

window.quelleButton.clicked.connect(selectSource)      # Legt fest, dass bei Knopfdruck auf "umrechnen" die Funktion "umrechnen()" ausgeführt wird
window.zielButton.clicked.connect(selectDestination)        # Legt fest, dass bei Knopfdruck auf "Info" die Funktion "zeigeInfo" ausgeführt wird
window.convertButton.clicked.connect(convert) 
app.exec_()                                         # Starte die Anwendung
