from PySide2.QtWidgets import QApplication
from mainWindow import MainWIndow
import sys

app=QApplication()

window=MainWIndow()
window.show()
sys.exit(app.exec_())
 

