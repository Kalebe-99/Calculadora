from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, MEDIUM_FONT_SIZE, SMALL_FONT_SIZE, MINIMUM_WIDTH
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from utils import isEmpty, isnNumOrDotOrComma


class Display(QLineEdit):
    eqPressed = Signal()
    deletePressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)
    squarePressed = Signal()
    oneDividedByXPressed = Signal()
    percentPressed = Signal()
    negatePressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px;'
                           f'color: white')
        self.setMinimumHeight(MEDIUM_FONT_SIZE*2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setContentsMargins(5, 10, 5, 5)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Delete, KEYS.Key_Backspace]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isOperator = key in [KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Asterisk, KEYS.Key_Slash, KEYS.Key_P]
        isPercentage = key in [KEYS.Key_Percent]
        isSquare = key in [KEYS.Key_V]
        isOneDividedByX = key in [KEYS.Key_X]
        isNegate = key in [KEYS.Key_N]

        if isEnter or text == '=':
            self.eqPressed.emit()
            return event.ignore()

        if isDelete:
            self.deletePressed.emit()
            return event.ignore()

        if isEsc:
            self.clearPressed.emit()
            return event.ignore()

        if isPercentage:
            self.percentPressed.emit()
            return event.ignore()

        if isSquare:
            self.squarePressed.emit()
            return event.ignore()

        if isOneDividedByX:
            self.oneDividedByXPressed.emit()
            return event.ignore()

        if isNegate:
            self.oneDividedByXPressed.emit()
            return event.ignore()

        if isOperator:
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()

        if isEmpty(text):
            return event.ignore()

        if isnNumOrDotOrComma(text):
            text = text
            self.inputPressed.emit(text)
            return event.ignore()