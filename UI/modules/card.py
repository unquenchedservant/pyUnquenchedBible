from utilities import variables as v
from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton as QButton
from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtGui import QColor
from utilities import scripture_helpers as sh
class ReadingCard(QWidget):
    def __init__(self, parent=None, title="", reading=""):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.title = title
        self.reading = reading
        self.palette().setColor(self.backgroundRole(), QColor("#383838"))
        self.setPalette(self.palette())
        self.setStyleSheet("""
                           QWidget {
                                background-color:#383838;
                                border-radius:10px;
                           }
                           QPushButton {
                                border-radius: 30px;
                                background-color: #383838;
                                padding: 5px 10px;
                           }
                           QPushButton:pressed {
                                background-color: #4A4A4A;
                           }
                           QHBoxLayout {
                                border-radius: 10px;
                           }
                           """)
        
        layout = QVBoxLayout()
        self.title = QLabel(title + " - " + reading, alignment=Qt.AlignmentFlag.AlignCenter)
        readingBar = QHBoxLayout()
        
        self.read_button = QButton("Read")
        self.read_button.clicked.connect(self.openReading)
        readingBar.addWidget(self.read_button)
        
        self.done_button = QButton("Done")
        readingBar.addWidget(self.done_button)
        
        layout.addWidget(self.title)
        layout.addLayout(readingBar)
        
        self.setLayout(layout)

    def setTitle(self, title):
        self.title.setText(title)

    def setReading(self, reading):
        self.reading.setText(reading)

    def openReading(self):
        currentReading = self.reading
        parts = currentReading.split()
        if QSettings('UnquenchedServant','Unquenched-Bible').value('prefBible','bible_gateway') == 'bible_gateway':
            sh.openBibleGateway(parts)
        else:
            sh.openLogos(parts)

