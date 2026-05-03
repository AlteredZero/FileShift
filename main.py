import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from app import FileShiftUi

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("assets/FileShiftIcon.png"))

window = FileShiftUi()
window.show()

sys.exit(app.exec_())