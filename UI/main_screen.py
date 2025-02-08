from utilities import variables as v
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QGridLayout, QPushButton, QMenu
from PyQt6.QtCore import QSettings, QTimer, QDateTime, QTime
from PyQt6.QtGui import QAction
from datetime import datetime as dt
from .modules import card
from utilities import list_helpers as lh
import datetime
import sys

class UnquenchedBible(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(v.APP_NAME)
        self.setGeometry(100, 100, 800, 300)
        self.day = datetime.datetime.now().day
        self.month = datetime.datetime.now().month
        self.year = datetime.datetime.now().year
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
        self.menu = None
        self.readingMenu = None
        self.settingsMenu = None
        self.psalms = False
        if self.settings.value('readingPlan','PGH') == 'PGH': # PGH, Mcheyne
            self.initPGH()
        else:
            self.initMcheyne()
        self.setupMidnightTimer()
        if int(self.settings.value('yearLastComplete', 0)) < self.year:
            print("Resetting - Year")
            self.resetAllDone()
        else:
            if int(self.settings.value('monthLastComplete', 0)) < self.month:
                print("Resetting - Month")
                self.resetAllDone()
            else:
                if int(self.settings.value('dayLastComplete', 0)) < self.day:
                    print("Resetting - Day")
                    self.resetAllDone()
    
    def initPGH(self):
        self.setWindowTitle(dt.now().strftime('%m-%d'))
        main_layout = QVBoxLayout()
        self.psalms = self.settings.value('psalms', False)
        if self.psalms == "true":
            self.psalms = True
        if self.psalms == "false":
            self.psalms = False
        
        reading_card_layout = QGridLayout()
        self.card1 = card.ReadingCard(self, 'Gospels', lh.pgh_1[int(self.settings.value("pghList1", 1))-1], listNum=1, settings=self.settings, list=lh.pgh_1)
        self.card2 = card.ReadingCard(self, 'Pentateuch', lh.pgh_2[int(self.settings.value("pghList2", 1))-1], listNum=2, settings=self.settings, list=lh.pgh_2)
        self.card3 = card.ReadingCard(self, 'Epistles I', lh.pgh_3[int(self.settings.value("pghList3", 1))-1], listNum=3, settings=self.settings, list=lh.pgh_3)
        self.card4 = card.ReadingCard(self, 'Epistles II', lh.pgh_4[int(self.settings.value("pghList4", 1))-1], listNum=4, settings=self.settings, list=lh.pgh_4)
        self.card5 = card.ReadingCard(self, 'Poetry', lh.pgh_5[int(self.settings.value("pghList5", 1))-1], listNum=5, settings=self.settings, list=lh.pgh_5)
        self.card6 = card.ReadingCard(self, 'Psalms', lh.pgh_6[int(self.settings.value("pghList6", 1))-1], listNum=6, settings=self.settings, list=lh.pgh_6, psalms=self.psalms)
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
        
        self.handleMenu()

        self.setCentralWidget(container)

    
    def initMcheyne(self):
        self.setWindowTitle(dt.now().strftime('%m-%d'))
        self.psalms = self.settings.value('psalms', False)
        if self.psalms == "true":
            self.psalms = True
        if self.psalms == "false":
            self.psalms = False
        main_layout = QVBoxLayout()

        reading_card_layout = QGridLayout()
        self.card1 = card.ReadingCard(self, 'List 1', 'Matthew 1', listNum=1, settings=self.settings,list=None) # These aren't accurate, but I don't have the plan in front of me at the moment
        self.card2 = card.ReadingCard(self, 'List 2', 'Genesis 1', listNum=2, settings=self.settings,list=None) 
        self.card3 = card.ReadingCard(self, 'List 3', 'Romans 1', listNum=3, settings=self.settings,list=None)
        self.card4 = card.ReadingCard(self, 'List 4', '1 Corinthians 1', listNum=4, settings=self.settings,list=None)
        if self.psalms:
            self.card5 = card.ReadingCard(self, "Psalms", "Psalm 1", listNum=5, settings=self.settings, list=None, psalms=True) # Playing with something. 

        reading_card_layout.addWidget(self.card1, 0, 0)
        reading_card_layout.addWidget(self.card2, 0, 1)
        reading_card_layout.addWidget(self.card3, 1, 0)
        reading_card_layout.addWidget(self.card4, 1, 1)
        if self.psalms:
            reading_card_layout.addWidget(self.card5, 2, 0)

        self.markDoneButton = QPushButton('Mark All Lists Done')
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
        self.handleMenu()
        self.setCentralWidget(container)

    def handleMenu(self):
        if not self.menu:
            self.menu = self.menuBar()
            self.settingsMenu = self.menu.addMenu('Settings')
            self.readingMenu = QMenu('Reading Plan', self)   
            self.settingsMenu.addMenu(self.readingMenu)
            self.exitAction = QAction('Exit', self)
            self.exitAction.triggered.connect(self.close)
            self.menu.addAction(self.exitAction)
        for action in self.settingsMenu.actions():
            self.settingsMenu.removeAction(action)
        for action in self.readingMenu.actions():
            self.readingMenu.removeAction(action)
        #self.settingsMenu.addMenu(self.readingMenu)

        # Reading Plan Toggle
        #pghChecked = "✓" if self.settings.value('readingPlan', 'PGH') == 'PGH' else ''
        #mcheyneChecked = "✓" if self.settings.value('readingPlan', 'PGH') == 'Mcheyne' else ''
        #pghAction = QAction('pgh{}'.format(pghChecked), self)
        #mcheyneAction = QAction('mcheyne{}'.format(mcheyneChecked), self)
        #pghAction.triggered.connect(lambda: self.setActivePlan('PGH'))
        #mcheyneAction.triggered.connect(lambda: self.setActivePlan('Mcheyne'))
        #self.readingMenu.addAction(pghAction)
        #self.readingMenu.addAction(mcheyneAction)

        # Psalms Toggle
        psalmsChecked = "✓" if self.settings.value('psalms', False) else ''
        psalmsAction = QAction("Psalms{}".format(psalmsChecked), self)
        psalmsAction.triggered.connect(lambda: self.changePsalms())
        self.settingsMenu.addAction(psalmsAction)

        # Bible Types
        self.bibleMenu = QMenu('Bible Source', self)
        self.settingsMenu.addMenu(self.bibleMenu)
        logosChecked = "✓" if self.settings.value('bibleType', 'Logos') == 'Logos' else ''
        logosAction = QAction('Logos{}'.format(logosChecked), self)
        logosAction.triggered.connect(lambda: self.setBibleType('Logos'))
        logosWebChecked = "✓" if self.settings.value('bibleType', 'Logos') == 'LogosWeb' else ''
        logosWebAction = QAction('LogosWeb{}'.format(logosWebChecked), self)
        logosWebAction.triggered.connect(lambda: self.setBibleType('LogosWeb'))
        bgChecked = "✓" if self.settings.value('bibleType', 'Logos') == 'BibleGateway' else ''
        bgAction = QAction('BibleGateway{}'.format(bgChecked), self)
        bgAction.triggered.connect(lambda: self.setBibleType('BibleGateway'))
        if not sys.platform == "linux": #linux doesn't have Logos. hence Logos web
            self.bibleMenu.addAction(logosAction)
        self.bibleMenu.addAction(bgAction)
       # self.bibleMenu.addAction(logosWebAction)
       # I just took one look at the URL scheme for Logos web and said "nope."
    def setBibleType(self, bibleType):
        self.settings.setValue('bibleType', bibleType)

    def changePsalms(self):
        if self.settings.value('psalms', False):
            self.settings.setValue('psalms', False)
        else:
            self.settings.setValue('psalms', True)
        if self.settings.value('readingPlan', 'PGH') == 'PGH':
            self.initPGH()
        else:
            self.initMcheyne()

    def setActivePlan(self, plan):
        self.settings.setValue('readingPlan', plan)
        if plan == 'PGH':
            self.initPGH()
        else:
            self.initMcheyne()
    def markAllDone(self):
        if self.settings.value('readingPlan', "PGH") == "PGH":
            plan = "pgh"
            max = 10
        else:
            plan = "mcheyne"
            max = 4
        if self.settings.value("{}List1Done".format(plan), False) == "false":
            self.card1.markSingleDone()
        if self.settings.value("{}List2Done".format(plan), False) == "false":
            self.card2.markSingleDone()
        if self.settings.value("{}List3Done".format(plan), False) == "false":
            self.card3.markSingleDone()
        if self.settings.value("{}List4Done".format(plan), False) == "false":
            self.card4.markSingleDone()
        if max > 4:
            if self.settings.value("{}List5Done".format(plan), False) == "false":
                self.card5.markSingleDone()
            if self.settings.value("{}List6Done".format(plan), False) == "false":
                self.card6.markSingleDone()
            if self.settings.value("{}List7Done".format(plan), False) == "false":
                self.card7.markSingleDone()
            if self.settings.value("{}List8Done".format(plan), False) == "false":
                self.card8.markSingleDone()
            if self.settings.value("{}List9Done".format(plan), False) == "false":
                self.card9.markSingleDone()
            if self.settings.value("{}List10Done".format(plan), False) == "false":
                self.card10.markSingleDone()
        self.settings.setValue("{}listsDone".format(plan), max)
        self.markDoneButton.setText('Reset All Lists')
        self.markDoneButton.clicked.disconnect(self.markAllDone)
        self.markDoneButton.clicked.connect(self.resetAllDone)

    def setupMidnightTimer(self):
        now = QDateTime.currentDateTime()
        midnight = QDateTime(now.date().addDays(1), QTime(0,0,0))
        secsToMidnight = now.secsTo(midnight)
        self.midnight_timer = QTimer(self)
        self.midnight_timer.setSingleShot(True)
        self.midnight_timer.timeout.connect(self.handleMidnight)
        self.midnight_timer.start(secsToMidnight * 1000)
    
    # This should only be called once per app open
    def handleMidnight(self):
        self.resetAllDone()
        self.midnight_timer.setInterval(24 * 60 * 60 * 1000)
        self.midnight_timer.setSingleShot(False)
        self.midnight_timer.timeout.connect(self.resetAllDone)
        self.midnight_timer.start()

    def resetAllDone(self):
        if self.settings.value('readingPlan', "PGH") == "PGH":
            plan = "pgh"
            max = 10
        else:
            plan = "mcheyne"
            max = 4
        if self.settings.value("{}List1Done".format(plan), False) == "true":
            self.card1.resetSingle()
        if self.settings.value("{}List2Done".format(plan), False) == "true":
            self.card2.resetSingle()
        if self.settings.value("{}List3Done".format(plan), False) == "true":
            self.card3.resetSingle()
        if self.settings.value("{}List4Done".format(plan), False) == "true":
            self.card4.resetSingle()
        if max > 4:
            if self.settings.value("{}List5Done".format(plan), False) == "true":
                self.card5.resetSingle()
            if self.settings.value("{}List6Done".format(plan), False) == "true":
                self.card6.resetSingle()
            if self.settings.value("{}List7Done".format(plan), False) == "true":
                self.card7.resetSingle()
            if self.settings.value("{}List8Done".format(plan), False) == "true":
                self.card8.resetSingle()
            if self.settings.value("{}List9Done".format(plan), False) == "true":
                self.card9.resetSingle()
            if self.settings.value("{}List10Done".format(plan), False) == "true":
                self.card10.resetSingle()
        self.settings.setValue("{}listsDone".format(plan), 0)
        self.markDoneButton.setText('Mark All Lists Done')
        try:
            self.markDoneButton.clicked.disconnect(self.resetAllDone)
        except:
            print("Not connected")
        self.markDoneButton.clicked.connect(self.markAllDone)