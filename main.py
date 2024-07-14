import sys

from PySide6.QtGui import QIcon
from main_window import MainWindow
from display import Display
from PySide6.QtWidgets import QApplication
from variables import CALCULATOR_ICON_PATH
from info import Info
from buttons import ButtonsGrid

if __name__ == '__main__':
    #inicia a aplicação
    app = QApplication()
    app.setApplicationName('Calculadora')
    window = MainWindow()

    # icon
    icon = QIcon(str(CALCULATOR_ICON_PATH))
    app.setWindowIcon(icon)

    # Info
    info = Info('')
    window.addWidgetToVerticalLayout(info)

    # Display
    display = Display()
    window.addWidgetToVerticalLayout(display)

    #Buttons Grid
    buttonsGrid = ButtonsGrid(display, info)
    window.verticalLayout.addLayout(buttonsGrid)

    #Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
