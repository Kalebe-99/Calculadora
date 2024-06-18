from main_window import MainWindow
from display import Display
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon
from info import Info

if __name__ == '__main__':
    #inicia a aplicação
    app = QApplication()

    #janela principal
    window = MainWindow()

    #icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVerticalLayout(info)

    #Cria o display
    display = Display()
    window.addWidgetToVerticalLayout(display)

    #Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()