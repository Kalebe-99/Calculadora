from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from PySide6.QtCore import Slot
from utils import isValidNumber, isnNumOrDotOrComma
from style import COMMON_BUTTON_STYLE, SPECIAL_BUTTON_STYLE, EQUAL_BUTTON_STYLE
from math import sqrt

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from info import Info


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(COMMON_BUTTON_STYLE)
        self.setMaximumSize(75, 60)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['%', 'C', '◀', '÷'],
            ['¹/x', '^', '²√x', '×'],
            ['7', '8', '9', '-'],
            ['4', '5', '6', '+'],
            ['1', '2', '3', '='],
            ['+/-', '0', '.']
        ]
        self.display = display
        self.display.setStyleSheet('color: #FFC0DF;'
                                   f'font-size: {MEDIUM_FONT_SIZE}px;')
        self.info = info
        self._equation = ''
        self._left = None
        self._right = None
        self._operator = None
        self._makeGrid()
        self.setContentsMargins(10, 10, 10, 0)

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value: str):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):

        self.display.eqPressed.connect(self._eq)
        self.display.deletePressed.connect(self.display.backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)
        self.display.oneDividedByXPressed.connect(self.oneDividedByX)
        self.display.squarePressed.connect(self.square)
        self.display.percentPressed.connect(self.percentage)
        self.display.negatePressed.connect(self.negate)

        for i, row in enumerate(self._gridMask):
            for j, number in enumerate(row):
                button = Button(number)

                if button.text() == '=':
                    button.setStyleSheet(EQUAL_BUTTON_STYLE)
                    self._configSpecialButton(button)

                elif not isnNumOrDotOrComma(button.text()):
                    button.setStyleSheet(SPECIAL_BUTTON_STYLE)
                    self._configSpecialButton(button)

                if button.text() == '=':
                    self.addWidget(button, i, j, 2, 1)
                    button.setFixedSize(75, 75)
                elif button.text() != '':
                    self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertToDisplay, button.text()
                                      .replace('*', '×')
                                      .replace('/', '÷'))
                self._connectButtonClicked(button, slot)

    @staticmethod
    def _connectButtonClicked(button, slot):
        button.clicked.connect(slot)  # type: ignore

    def _configSpecialButton(self, button):
        buttonText = button.text()

        if buttonText == 'C':
            self._connectButtonClicked(button, self._clear)

        if buttonText == '+':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._configLeftOp, button)
            )
        if buttonText == '-':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._configLeftOp, button)
            )
        if buttonText == '×':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._configLeftOp, button)
            )
        if buttonText == '÷':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._configLeftOp, button)
            )
        if buttonText == '^':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._configLeftOp, button)
            )

        if buttonText == '=':
            self._connectButtonClicked(
                button,
                self._eq
            )
        if buttonText == '◀':
            self._connectButtonClicked(
                button,
                self.display.backspace
            )

        if buttonText == '%':
            self._connectButtonClicked(button, self.percentage)

        if buttonText == '²√x':
            self._connectButtonClicked(button, self.square)

        if buttonText == '¹/x':
            self._connectButtonClicked(button, self.oneDividedByX)

        if buttonText == '+/-':
            self._connectButtonClicked(button, self.negate)

    @staticmethod
    def _makeSlot(func, *args, **kwargs):
        @Slot(bool)
        def interna():
            func(*args, **kwargs)
        return interna

    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = (self.display.text() + text)
        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._operator = None
        self.info.setText('')
        self.display.clear()

    @Slot()
    def _configLeftOp(self, text):
        if isinstance(text, Button):
            text = text.text()
        displayText = self.display.text()
        self.display.clear()

        if not isValidNumber(displayText) and self._left is None:
            self.info.setText('Valor da esquerda nulo')
            return

        if self._left is None:
            self._left = (float(displayText))

        self._operator = text.replace('*', '×').replace('/', '÷')
        self.equation = f'{self._left} {self._operator} '

    @Slot()
    def _eq(self):
        if self._operator:
            displayText = self.display.text()

            if not isValidNumber(displayText):
                return

            self._right = float(displayText)
            self.equation = f'{self._left} {self._operator} {self._right}'
            try:

                result = eval(str(self.equation)
                              .replace('÷', '/')
                              .replace('×', '*')
                              .replace('^', '**')
                              )
            except ZeroDivisionError:
                self.display.setText('Não é possível dividir por zero')
                return
            except OverflowError:
                self.display.setText('Número muito grande')
                return

            self.display.clear()
            self.info.setText(f'{str(self.equation)
                              .replace('/', '÷')
                              .replace('*', '×')
                              .replace('**', '^')} =')
            self.display.setText(str(result))
            self._left = result

    @Slot()
    def percentage(self):

        if not isValidNumber(self.display.text()) and self._left is None:
            self.info.setText('Valor da esquerda nulo')
            return

        if self.display.text():
            self._left = float(self.display.text())
            self.info.setText(f'{str(self._left)}% =')
            self.display.setText(str(self._left/100))
            self._left = self._left/100

    @Slot()
    def square(self):

        if not isValidNumber(self.display.text()) and self._left is None:
            self.info.setText('Valor da esquerda nulo')
            return

        if self.display.text():
            self._left = float(self.display.text())
            self.info.setText(f'²√{str(self._left)} =')
            self.display.setText(str(sqrt(self._left)))
            self._left = sqrt(self._left)

    @Slot()
    def oneDividedByX(self):

        if not isValidNumber(self.display.text()) and self._left is None:
            self.info.setText('Valor da esquerda nulo')
            return

        if self.display.text():
            self._left = float(self.display.text())
            self.info.setText(f'¹/{str(self._left)}=')
            self.display.setText(str(1/self._left))
            self._left = 1 / self._left

    @Slot()
    def negate(self):

        if not isValidNumber(self.display.text()) and self._left is None:
            self.info.setText('Valor da esquerda nulo')
            return

        if self.display.text():
            self.display.setText(f'{float(self.display.text()) * -1}')
