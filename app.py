import sys
from PyQt6.QtWidgets import QApplication
from UI.main_screen import MainWindow
from utilities import resource_path
if __name__ == "__main__":
    app = QApplication(sys.argv)
    if sys.platform == "linux" or sys.platform == "darwin":
        resource = "asset/style.qss"
        app.setStyle("Breeze")
    else:
        resource = "asset\\style.qss"
        app.setStyle("Fusion")
    with open(resource_path(resource), "r") as file:
        app.setStyleSheet(file.read())
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
