from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt, QEvent
from title_bar import CustomTitleBar
from PySide6.QtGui import QMouseEvent


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Set centralwidget
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # Set layout
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 7)
        self.centralWidget.setLayout(self.verticalLayout)
        self.setCentralWidget(self.centralWidget)

        # Turn window frameless
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Config style
        self.configStyle()

        # Personalized title bar
        self.title_bar = CustomTitleBar(self)
        self.addWidgetToVerticalLayout(self.title_bar)

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVerticalLayout(self, widget: QWidget):
        self.verticalLayout.addWidget(widget)

    def configStyle(self):
        self.setStyleSheet('background-color: #1C1C1C;'
                           'border-radius: 5px')
