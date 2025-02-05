from utilities import variables as v
from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton as QButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from utilities import scripture_helpers as sh
from utilities import list_helpers as lh
import datetime

# TODO: Psalms logic - once marked done, no reset option should be available. 
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
     def __init__(self, parent=None, title="", reading="", listNum=1, settings=None, list=None, psalms=False):
          super().__init__(parent)
          self.setAutoFillBackground(True)
          self.title = title
          self.iteration = 1
          self.psalms = psalms
          self.day = datetime.datetime.now().day
          if self.psalms:
               self.reading = self.getPsalmTitle()
          else:
               self.reading = reading
          self.listNum = listNum
          self.list = list
          self.settings = settings
          self.palette().setColor(self.backgroundRole(), QColor("#383838"))
          self.setPalette(self.palette())
          plan = self.settings.value('readingPlan', "PGH")
          if plan == "PGH":
               plan = "pgh"
          else:
               plan = "mcheyne"
          
          layout = QVBoxLayout()
          readingBar = QHBoxLayout()
          self.titleLabel = QLabel(self.title + " - " + self.reading, alignment=Qt.AlignmentFlag.AlignCenter)
          self.read_button = QButton("Read")
          self.read_button.clicked.connect(self.openReading)
          readingBar.addWidget(self.read_button)
          print("ITERATION: ", self.iteration)
          if self.psalms and self.iteration != 5:
               self.done_button = QButton("Next")
               self.done_button.clicked.connect(self.nextPsalm)
          else:
               self.done_button = QButton("Done")
               self.done_button.clicked.connect(self.markSingleDone)
          readingBar.addWidget(self.done_button)
          if self.settings.value('{}List{}Done'.format(plan, self.listNum), False) == "false":
               self.setStyleSheet(ACTIVE_PALETTE)
          else:
               self.setStyleSheet(UNACTIVE_PALETTE)
               if not self.psalms:
                    self.done_button.setText("Reset")
                    try:
                         self.done_button.clicked.disconnect(self.markSingleDone)
                    except:
                         print("No connection to markSingleDone")
                    self.done_button.clicked.connect(self.resetSingle)
               else:
                    self.done_button.setText("Completed")
                    self.done_button.clicked.disconnect(self.nextPsalm)
                    self.done_button.setEnabled(False)
                    self.reading = self.finalPsalm()
                    self.titleLabel.setText(self.title + " - " + self.reading)
          layout.addWidget(self.titleLabel)
          layout.addLayout(readingBar)
          
          self.setLayout(layout)

     def finalPsalm(self):
          if self.day == 31:
               return "Day Off"
          else:
               return "Psalm {}".format(self.day + (30 * 4))
     def getPsalmTitle(self):
          if self.day == 31:
               return "Day Off"
          else:
               if self.iteration == 1:
                    return "Psalm {}".format(self.day)
               else:
                    return "Psalms {}".format(self.day + (30 * (self.iteration - 1)))
          
     def nextPsalm(self):
          self.iteration = self.iteration + 1
          self.reading = self.getPsalmTitle()
          self.titleLabel.setText(self.title + " - " + self.reading)
          if self.iteration == 5:
               self.done_button.setText("Done")
               self.done_button.clicked.disconnect(self.nextPsalm)
               self.done_button.clicked.connect(self.markSingleDone)
          self.setStyleSheet(ACTIVE_PALETTE)
          self.done_button.setStyleSheet("")
          self.read_button.setStyleSheet("")

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
          listsDone = int(self.settings.value('{}listsDone'.format(plan), 0))
          self.settings.setValue("{}List{}Done".format(plan, self.listNum), "true") #mark list as done
          current = int(self.settings.value("{}List{}".format(plan, self.listNum), 1)) #get the current list index
          if current + 1 > len(self.list):
               self.settings.setValue("{}List{}".format(plan, self.listNum), "1") #reset index to 1
          self.done_button.clicked.disconnect(self.markSingleDone)
          if not self.psalms:
               self.done_button.setText("Reset")
               self.done_button.clicked.connect(self.resetSingle)
          else:
               self.done_button.isEnabled = False
          self.settings.setValue('{}listsDone'.format(plan), str(listsDone + 1))
          self.setStyleSheet(UNACTIVE_PALETTE)
          self.done_button.setStyleSheet("")
          self.read_button.setStyleSheet("")

     def resetSingle(self):
          if self.settings.value('readingPlan', "PGH") == "PGH":
               plan = "pgh"
          else:
               plan = "mcheyne"
          listsDone = int(self.settings.value('{}listsDone'.format(plan), 0))
          curIndex = int(self.settings.value("{}List{}".format(plan, self.listNum), 1))

          self.settings.setValue("{}List{}".format(plan, self.listNum), str(curIndex + 1)) # Reset List
          self.settings.setValue("{}List{}Done".format(plan, self.listNum), "false") # Uncheck List

          self.reading = self.list[int(self.settings.value("{}List{}".format(plan, self.listNum), 1))-1]
          self.titleLabel.setText(self.title + " - " + self.reading)

          self.settings.setValue('{}listsDone'.format(plan), str(listsDone - 1))

          self.done_button.setText("Done")
          self.done_button.clicked.disconnect(self.resetSingle)
          self.done_button.clicked.connect(self.markSingleDone)
          
          self.setStyleSheet(ACTIVE_PALETTE)