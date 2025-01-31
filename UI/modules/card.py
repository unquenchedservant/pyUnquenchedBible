from utilities import variables as v
from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
class ReadingCard(QWidget):
    def __init__(self, parent=None,title="",reading=""):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.palette().setColor(self.backgroundRole(), v.COLOR_PRIMARY)
        layout = QVBoxLayout()
        self.title = QLabel(title)
        self.reading = QLabel(reading)

        layout.addWidget(self.title)
        layout.addWidget(self.reading)
        
        self.setLayout(layout)

    def setTitle(self,title):
        self.title.setText(title)

    def setReading(self,reading):
        self.reading.setText(reading)
