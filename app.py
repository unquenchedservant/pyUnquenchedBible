import sys
from PyQt6.QtWidgets import QApplication
from UI.main_screen import UnquenchedBible
from utilities import resource_path
from utilities import variables as v
if __name__ == "__main__":
    v.init()
    app = QApplication(sys.argv)
    if sys.platform == "linux" or sys.platform == "darwin":
        resource = "assets/style.qss"
        app.setStyle("Breeze")
    else:
        resource = "assets\\style.qss"
        app.setStyle("Fusion")
    with open(resource_path(resource), "r") as file:
        app.setStyleSheet(file.read())
    mainWin = UnquenchedBible()
    mainWin.show()
    sys.exit(app.exec())
