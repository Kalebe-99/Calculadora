from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE,MEDIUM_FONT_SIZE, SMALL_FONT_SIZE
from PySide6.QtCore import Qt


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px')
        self.setMinimumHeight(MEDIUM_FONT_SIZE*2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
