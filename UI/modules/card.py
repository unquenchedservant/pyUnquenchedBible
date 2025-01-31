from PyQt6.QtWidgets import QLabel, QVBoxLayout
class ReadingCard(QVBoxLayout):
    def __init__(self, parent=None,title="",reading=""):
        super().__init__(parent)
        self.title = QLabel(title)
        self.reading = QLabel(reading)

        self.addWidget(self.title)
        self.addWidget(self.reading)

    def setTitle(self,title):
        self.title.setText(title)

    def setReading(self,reading):
        self.reading.setText(reading)
