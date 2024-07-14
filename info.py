from PySide6.QtWidgets import QLabel, QWidget
from variables import SMALL_FONT_SIZE
from PySide6.QtCore import Qt

class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;'
                           f'color: pink')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setContentsMargins(5, 10, 5, 5)

