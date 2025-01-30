from utilities import variables as v
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import QSettings

class TimerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(v.APP_NAME)
        self.setGeometry(100, 100, 800, 600)

        self.settings = QSettings('UnquenchedServant','Unquenched-Bible')
        #self.executor = concurrent.futures.ThreadPoolExecutor()
        self.is_complete = False
        self.initUI()

    def initUI(self):
        self.test_label = QLabel('Hello, World!', self)
        layout = QVBoxLayout()
        layout.addWidget(self.test_label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
