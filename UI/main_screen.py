from utilities import variables as v
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import QSettings
from datetime import datetime as dt
from .modules import card
class UnquenchedBible(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(v.APP_NAME)
        self.setGeometry(100, 100, 800, 600)

        self.settings = QSettings('UnquenchedServant','Unquenched-Bible')
        #self.executor = concurrent.futures.ThreadPoolExecutor()
        self.is_complete = False
        if self.settings.value('readingPlan','PGH') == 'PGH': # PGH, Mcheyne
            self.initPGH()
        else:
            self.initMcheyne()
        #self.initUI()
    
    def initPGH(self):
        self.setWindowTitle(dt.now().strftime('%m-%d'))
        main_layout = QVBoxLayout()
        
        self.card1 = card.ReadingCard(self, 'Gospels', 'Matthew 1')
        self.card2 = card.ReadingCard(self, 'Pentateuch', 'Genesis 1')
        self.card3 = card.ReadingCard(self, 'Epistles I', 'Romans 1')
        self.card4 = card.ReadingCard(self, 'Epistles II', '1 Corinthians 1')
        self.card5 = card.ReadingCard(self, 'Poetry', 'Job 1')
        self.card6 = card.ReadingCard(self, 'Psalms', 'Psalm 1')
        self.card7 = card.ReadingCard(self, 'Proverbs', 'Proverbs 1')
        self.card8 = card.ReadingCard(self, 'History', 'Joshua 1')
        self.card9 = card.ReadingCard(self, 'Prophets', 'Isaiah 1')
        self.card10 = card.ReadingCard(self, 'Acts', 'Acts 1')
        
        main_layout.addLayout(self.card1)
        main_layout.addLayout(self.card2)
        main_layout.addLayout(self.card3)
        main_layout.addLayout(self.card4)
        main_layout.addLayout(self.card5)
        main_layout.addLayout(self.card6)
        main_layout.addLayout(self.card7)
        main_layout.addLayout(self.card8)
        main_layout.addLayout(self.card9)
        main_layout.addLayout(self.card10)

        container = QWidget()
        container.setLayout(main_layout)
        
        self.setCentralWidget(container)
    
    def initMcheyne(self):
        self.setWindowTitle(dt.now().strftime('%m-%d'))
        main_layout = QVBoxLayout()
        self.title_label1 = QLabel('List 1', self)
        self.title_label2 = QLabel('List 2', self)
        self.title_label3 = QLabel('List 3', self)
        self.title_label4 = QLabel('List 4', self)

        main_layout.addWidget(self.title_label1)
        main_layout.addWidget(self.title_label2)
        main_layout.addWidget(self.title_label3)
        main_layout.addWidget(self.title_label4)

        container = QWidget()
        container.setLayout(main_layout)
        
        self.setCentralWidget(container)
