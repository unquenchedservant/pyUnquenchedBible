from utilities import variables as v
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QGridLayout, QPushButton
from PyQt6.QtCore import QSettings
from datetime import datetime as dt
from .modules import card
from utilities import list_helpers as lh
class UnquenchedBible(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(v.APP_NAME)
        self.setGeometry(100, 100, 800, 300)

        self.settings = QSettings('UnquenchedServant','Unquenched-Bible')
        """
        self.settings.setValue('pghList1',1)
        self.settings.setValue('pghList2',1)
        self.settings.setValue('pghList3',1)
        self.settings.setValue('pghList4',1)
        self.settings.setValue('pghList5',1)
        self.settings.setValue('pghList6',1)
        self.settings.setValue('pghList7',1)
        self.settings.setValue('pghList8',1)
        self.settings.setValue('pghList9',1)
        self.settings.setValue('pghList10',1)
        """
        #self.executor = concurrent.futures.ThreadPoolExecutor()
        self.is_complete = False
        if self.settings.value('readingPlan','PGH') == 'PGH': # PGH, Mcheyne
            self.initPGH()
        else:
            self.initMcheyne()
    
    def initPGH(self):
        self.setWindowTitle(dt.now().strftime('%m-%d'))
        main_layout = QVBoxLayout()
        
        reading_card_layout = QGridLayout()
        self.card1 = card.ReadingCard(self, 'Gospels', lh.pgh_1[int(self.settings.value("pghList1", 1))-1], listNum=1, settings=self.settings, list=lh.pgh_1)
        self.card2 = card.ReadingCard(self, 'Pentateuch', lh.pgh_2[int(self.settings.value("pghList2", 1))-1], listNum=2, settings=self.settings, list=lh.pgh_2)
        self.card3 = card.ReadingCard(self, 'Epistles I', lh.pgh_3[int(self.settings.value("pghList3", 1))-1], listNum=3, settings=self.settings, list=lh.pgh_3)
        self.card4 = card.ReadingCard(self, 'Epistles II', lh.pgh_4[int(self.settings.value("pghList4", 1))-1], listNum=4, settings=self.settings, list=lh.pgh_4)
        self.card5 = card.ReadingCard(self, 'Poetry', lh.pgh_5[int(self.settings.value("pghList5", 1))-1], listNum=5, settings=self.settings, list=lh.pgh_5)
        self.card6 = card.ReadingCard(self, 'Psalms', lh.pgh_6[int(self.settings.value("pghList6", 1))-1], listNum=6, settings=self.settings, list=lh.pgh_6)
        self.card7 = card.ReadingCard(self, 'Proverbs', lh.pgh_7[int(self.settings.value("pghList7", 1))-1], listNum=7, settings=self.settings, list=lh.pgh_7)
        self.card8 = card.ReadingCard(self, 'History', lh.pgh_8[int(self.settings.value("pghList8", 1))-1], listNum=8, settings=self.settings, list=lh.pgh_8)
        self.card9 = card.ReadingCard(self, 'Prophets', lh.pgh_9[int(self.settings.value("pghList9", 1))-1], listNum=9, settings=self.settings, list=lh.pgh_9)
        self.card10 = card.ReadingCard(self, 'Acts', lh.pgh_10[int(self.settings.value("pghList10", 1))-1], listNum=10, settings=self.settings, list=lh.pgh_10)
        
        reading_card_layout.addWidget(self.card1, 0, 0)
        reading_card_layout.addWidget(self.card2, 0, 1)
        reading_card_layout.addWidget(self.card3, 1, 0)
        reading_card_layout.addWidget(self.card4, 1, 1)
        reading_card_layout.addWidget(self.card5, 2, 0)
        reading_card_layout.addWidget(self.card6, 2, 1)
        reading_card_layout.addWidget(self.card7, 3, 0)
        reading_card_layout.addWidget(self.card8, 3, 1)
        reading_card_layout.addWidget(self.card9, 4, 0)
        reading_card_layout.addWidget(self.card10, 4, 1)

        self.markDoneButton = QPushButton('Mark All Lists Done')
        self.markDoneButton.clicked.connect(self.markAllDone)
        print(self.settings.value('pghlistsDone', 0))
        if int(self.settings.value('pghlistsDone', 0)) > 0 and int(self.settings.value('pghlistsDone', 0)) < 10:
            self.markDoneButton.setText('Mark Remaining Lists Done')
        elif int(self.settings.value('pghlistsDone', 0)) == 10:
            self.markDoneButton.setText('Reset All Lists')
            self.markDoneButton.clicked.disconnect(self.markAllDone)
            self.markDoneButton.clicked.connect(self.resetAllDone)
        
        
        main_layout.addLayout(reading_card_layout)
        main_layout.addWidget(self.markDoneButton)

        container = QWidget()
        container.setLayout(main_layout)
        
        self.setCentralWidget(container)
    
    def initMcheyne(self):
        self.setWindowTitle(dt.now().strftime('%m-%d'))
        main_layout = QVBoxLayout()

        reading_card_layout = QGridLayout()
        self.card1 = card.ReadingCard(self, 'List 1', 'Matthew 1', listNum=1, settings=self.settings,list=None) # These aren't accurate, but I don't have the plan in front of me at the moment
        self.card2 = card.ReadingCard(self, 'List 2', 'Genesis 1', listNum=2, settings=self.settings,list=None) 
        self.card3 = card.ReadingCard(self, 'List 3', 'Romans 1', listNum=3, settings=self.settings,list=None)
        self.card4 = card.ReadingCard(self, 'List 4', '1 Corinthians 1', listNum=4, settings=self.settings,list=None)

        reading_card_layout.addWidget(self.card1, 0, 0)
        reading_card_layout.addWidget(self.card2, 0, 1)
        reading_card_layout.addWidget(self.card3, 1, 0)
        reading_card_layout.addWidget(self.card4, 1, 1)

        self.markDoneButton = card.QPushButton('Mark All Lists Done')
        self.markDoneButton.clicked.connect(self.markAllDone)
        if int(self.settings.value('mcheynelistsDone', 0)) > 0 and int(self.settings.value('mcheynelistsDone', 0)) < 4:
            self.markDoneButton.setText('Mark Remaining Lists Done')
        elif int(self.settings.value('mcheynelistsDone', 0)) == 4:
            self.markDoneButton.setText('Reset All Lists')
            self.markDoneButton.clicked.disconnect(self.markAllDone)
            self.markDoneButton.clicked.connect(self.resetAllDone)

        main_layout.addLayout(reading_card_layout)
        main_layout.addWidget(self.markDoneButton)
        container = QWidget()
        container.setLayout(main_layout)
        
        self.setCentralWidget(container)

    def markAllDone(self):
        if self.settings.value('readingPlan', "PGH") == "PGH":
            plan = "pgh"
            max = 10
        else:
            plan = "mcheyne"
            max = 4
        print("List 1 - {}".format(self.settings.value("{}List1Done".format(plan), False)))
        print("List 2 - {}".format(self.settings.value("{}List2Done".format(plan), False)))
        print("List 3 - {}".format(self.settings.value("{}List3Done".format(plan), False)))
        print("List 4 - {}".format(self.settings.value("{}List4Done".format(plan), False)))
        if max > 4:
            print("List 5 - {}".format(self.settings.value("{}List5Done".format(plan), False)))
            print("List 6 - {}".format(self.settings.value("{}List6Done".format(plan), False)))
            print("List 7 - {}".format(self.settings.value("{}List7Done".format(plan), False)))
            print("List 8 - {}".format(self.settings.value("{}List8Done".format(plan), False)))
            print("List 9 - {}".format(self.settings.value("{}List9Done".format(plan), False)))
            print("List 10 - {}".format(self.settings.value("{}List10Done".format(plan), False)))
        if self.settings.value("{}List1Done".format(plan), False) == "false":
            self.card1.markSingleDone()
            print("Marking List 1")
        if self.settings.value("{}List2Done".format(plan), False) == "false":
            self.card2.markSingleDone()
            print("Marking List 2")
        if self.settings.value("{}List3Done".format(plan), False) == "false":
            self.card3.markSingleDone()
            print("Marking List 3")
        if self.settings.value("{}List4Done".format(plan), False) == "false":
            self.card4.markSingleDone()
            print("Marking List 4")
        if max > 4:
            if self.settings.value("{}List5Done".format(plan), False) == "false":
                self.card5.markSingleDone()
                print("Marking List 5")
            if self.settings.value("{}List6Done".format(plan), False) == "false":
                self.card6.markSingleDone()
                print("Marking List 6")
            if self.settings.value("{}List7Done".format(plan), False) == "false":
                self.card7.markSingleDone()
                print("Marking List 7")
            if self.settings.value("{}List8Done".format(plan), False) == "false":
                self.card8.markSingleDone()
                print("Marking List 8")
            if self.settings.value("{}List9Done".format(plan), False) == "false":
                self.card9.markSingleDone()
                print("Marking List 9")
            if self.settings.value("{}List10Done".format(plan), False) == "false":
                self.card10.markSingleDone()
                print("Marking List 10")
        self.settings.setValue("{}listsDone".format(plan), max)
        print(self.settings.value("{}listsDone".format(plan), 0))
        self.markDoneButton.setText('Reset All Lists')
        self.markDoneButton.clicked.disconnect(self.markAllDone)
        self.markDoneButton.clicked.connect(self.resetAllDone)

    def resetAllDone(self):
        if self.settings.value('readingPlan', "PGH") == "PGH":
            plan = "pgh"
            max = 10
        else:
            plan = "mcheyne"
            max = 4
        if self.settings.value("{}List1Done".format(plan), False) == "true":
            print("Resetting List 1")
            self.card1.resetSingle()
        if self.settings.value("{}List2Done".format(plan), False) == "true":
            self.card2.resetSingle()
            print("Resetting List 2")
        if self.settings.value("{}List3Done".format(plan), False) == "true":
            self.card3.resetSingle()
            print("Resetting List 3")
        if self.settings.value("{}List4Done".format(plan), False) == "true":
            self.card4.resetSingle()
            print("Resetting List 4")
        if max > 4:
            if self.settings.value("{}List5Done".format(plan), False) == "true":
                self.card5.resetSingle()
                print("Resetting List 5")
            if self.settings.value("{}List6Done".format(plan), False) == "true":
                self.card6.resetSingle()
                print("Resetting List 6")
            if self.settings.value("{}List7Done".format(plan), False) == "true":
                self.card7.resetSingle()
                print("Resetting List 7")
            if self.settings.value("{}List8Done".format(plan), False) == "true":
                self.card8.resetSingle()
                print("Resetting List 8")
            if self.settings.value("{}List9Done".format(plan), False) == "true":
                self.card9.resetSingle()
                print("Resetting List 9")
            if self.settings.value("{}List10Done".format(plan), False) == "true":
                self.card10.resetSingle()
                print("Resetting List 10")
        self.settings.setValue("{}listsDone".format(plan), 0)
        print(self.settings.value("{}listsDone".format(plan), 0))
        self.markDoneButton.setText('Mark All Lists Done')
        self.markDoneButton.clicked.disconnect(self.resetAllDone)
        self.markDoneButton.clicked.connect(self.markAllDone)