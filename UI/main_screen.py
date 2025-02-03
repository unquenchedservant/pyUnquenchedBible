from utilities import variables as v
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QGridLayout
from PyQt6.QtCore import QSettings
from datetime import datetime as dt
from .modules import card
class UnquenchedBible(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(v.APP_NAME)
        self.setGeometry(100, 100, 800, 300)

        self.settings = QSettings('UnquenchedServant','Unquenched-Bible')
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
        self.card1 = card.ReadingCard(self, 'Gospels', 'Matthew 1', listNum=1, settings=self.settings)
        self.card2 = card.ReadingCard(self, 'Pentateuch', 'Genesis 1', listNum=2, settings=self.settings)
        self.card3 = card.ReadingCard(self, 'Epistles I', 'Romans 1', listNum=3, settings=self.settings)
        self.card4 = card.ReadingCard(self, 'Epistles II', '1 Corinthians 1', listNum=4, settings=self.settings)
        self.card5 = card.ReadingCard(self, 'Poetry', 'Job 1', listNum=5, settings=self.settings)
        self.card6 = card.ReadingCard(self, 'Psalms', 'Psalm 1', listNum=6, settings=self.settings)
        self.card7 = card.ReadingCard(self, 'Proverbs', 'Proverbs 1', listNum=7, settings=self.settings)
        self.card8 = card.ReadingCard(self, 'History', 'Joshua 1', listNum=8, settings=self.settings)
        self.card9 = card.ReadingCard(self, 'Prophets', 'Isaiah 1', listNum=9, settings=self.settings)
        self.card10 = card.ReadingCard(self, 'Acts', 'Acts 1', listNum=10, settings=self.settings)
        
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
        
        main_layout.addLayout(reading_card_layout)

        container = QWidget()
        container.setLayout(main_layout)
        
        self.setCentralWidget(container)
    
    def initMcheyne(self):
        self.setWindowTitle(dt.now().strftime('%m-%d'))
        main_layout = QVBoxLayout()

        reading_card_layout = QGridLayout()
        self.card1 = card.ReadingCard(self, 'List 1', 'Matthew 1') # These aren't accurate, but I don't have the plan in front of me at the moment
        self.card2 = card.ReadingCard(self, 'List 2', 'Genesis 1') 
        self.card3 = card.ReadingCard(self, 'List 3', 'Romans 1')
        self.card4 = card.ReadingCard(self, 'List 4', '1 Corinthians 1')

        reading_card_layout.addWidget(self.card1, 0, 0)
        reading_card_layout.addWidget(self.card2, 0, 1)
        reading_card_layout.addWidget(self.card3, 1, 0)
        reading_card_layout.addWidget(self.card4, 1, 1)

        main_layout.addLayout(reading_card_layout)

        container = QWidget()
        container.setLayout(main_layout)
        
        self.setCentralWidget(container)
