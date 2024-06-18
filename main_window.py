from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.verticalLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.verticalLayout)
        self.setCentralWidget(self.centralWidget)
        self.setWindowTitle('Calculadora')
        self.configStyle()


    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVerticalLayout(self, widget: QWidget):
        self.verticalLayout.addWidget(widget)

    def configStyle(self):
        self.setStyleSheet('background-color: pink;')


