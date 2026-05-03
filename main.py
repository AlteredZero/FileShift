import os
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from app import FileShiftUi

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

app = QApplication(sys.argv)

icon_path = resource_path("assets/FileShiftIcon.png")
app.setWindowIcon(QIcon(icon_path))

window = FileShiftUi()
window.show()
sys.exit(app.exec_())
