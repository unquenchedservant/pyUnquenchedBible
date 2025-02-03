from utilities import variables as v
from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton as QButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from utilities import scripture_helpers as sh


ACTIVE_PALETTE = """
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
                           """
UNACTIVE_PALETTE = """
                           QWidget {
                                border-radius:10px;
                           }
                           QPushButton {
                                border-radius: 30px;
                                padding: 5px 10px;
                           }
                           QPushButton:pressed {
                                background-color: #4A4A4A;
                           }
                           QHBoxLayout {
                                border-radius: 10px;
                           }
                           """
class ReadingCard(QWidget):
     def __init__(self, parent=None, title="", reading="", listNum=1, settings=None):
          super().__init__(parent)
          self.setAutoFillBackground(True)
          self.title = title
          self.reading = reading
          self.listNum = listNum
          self.settings = settings
          self.palette().setColor(self.backgroundRole(), QColor("#383838"))
          self.setPalette(self.palette())
          plan = self.settings.value('readingPlan', "PGH")
          if plan == "PGH":
               plan = "pgh"
          else:
               plan = "mcheyne"
          
          layout = QVBoxLayout()
          self.titleLabel = QLabel(title + " - " + reading, alignment=Qt.AlignmentFlag.AlignCenter)
          readingBar = QHBoxLayout()
          
          self.read_button = QButton("Read")
          self.read_button.clicked.connect(self.openReading)
          readingBar.addWidget(self.read_button)
          
          self.done_button = QButton("Done")
          self.done_button.clicked.connect(self.markSingleDone)
          readingBar.addWidget(self.done_button)
          if self.settings.value('{}List{}Done'.format(plan, self.listNum), False) == False:
               self.setStyleSheet(ACTIVE_PALETTE)
          else:
               self.setStyleSheet(UNACTIVE_PALETTE)
               self.done_button.setText("Reset")
               self.done_button.clicked.disconnect(self.markSingleDone)
               self.done_button.clicked.connect(self.resetSingle)
          layout.addWidget(self.titleLabel)
          layout.addLayout(readingBar)
          
          self.setLayout(layout)

     def setTitle(self, title):
          self.title = title

     def setReading(self, reading):
          self.reading = reading

     def openReading(self):
          currentReading = self.reading
          parts = currentReading.split()
          if self.settings.value('prefBible','bible_gateway') == 'bible_gateway':
               sh.openBibleGateway(parts)
          else:
               sh.openLogos(parts)

     def markSingleDone(self):
          if self.settings.value('readingPlan', "PGH") == "PGH":
               plan = "pgh"
          else:
               plan = "mcheyne"
          self.settings.setValue("{}List{}Done".format(plan, self.listNum), True) #mark list as done
          current = int(self.settings.value("{}List{}".format(plan, self.listNum), 1)) #get the current list index
          self.settings.setValue("{}List{}".format(plan, self.listNum), current + 1) #increase index by 1
          self.done_button.setText("Reset")
          self.done_button.clicked.disconnect(self.markSingleDone)
          self.done_button.clicked.connect(self.resetSingle)
          self.setStyleSheet("""
                              QWidget {
                                   border-radius:10px;
                              }
                              QPushButton {
                                   border-radius: 30px;
                                   padding: 5px 10px;
                              }
                              QPushButton:pressed {
                                   background-color: #4A4A4A;
                              }
                              QHBoxLayout {
                                   border-radius: 10px;
                              }
                              """)
          self.done_button.setStyleSheet("")
          self.read_button.setStyleSheet("")

     def resetSingle(self):
          if self.settings.value('readingPlan', "PGH") == "PGH":
               plan = "pgh"
          else:
               plan = "mcheyne"
          self.settings.setValue("{}List{}Done".format(plan, self.listNum), False) # Uncheck List
          self.done_button.setText("Done")
          self.done_button.clicked.disconnect(self.resetSingle)
          self.done_button.clicked.connect(self.markSingleDone)
          self.setStyleSheet(ACTIVE_PALETTE)