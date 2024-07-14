from PySide6.QtWidgets import (QWidget,
                               QHBoxLayout,
                               QToolButton,
                               QLabel)
from variables import MINIMIZE_ICON_PATH, CLOSE_ICON_PATH, CALCULATOR_ICON_PATH
from style import MIN_BUTTON_STYLE, CLOSE_BUTTON_STYLE
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt, QSize, QEvent


class CustomTitleBar(QWidget):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(5, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)
        self.initial_pos = None

        self.icon = QLabel()
        self.icon.setPixmap(QIcon(str(CALCULATOR_ICON_PATH)).pixmap(16, 16))
        self.icon.setFixedSize(18, 18)
        self.layout.addWidget(self.icon)

        self.title = QLabel('Calculadora')
        self.title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.title.setStyleSheet(
            """margin: 5px;
               color: #808080
            """
        )
        self.layout.addWidget(self.title)

        self.closebutton = QToolButton()
        self.closebutton.clicked.connect(self.window().close)
        self.closebutton.setIcon(QIcon(str(CLOSE_ICON_PATH)))
        self.closebutton.setStyleSheet(CLOSE_BUTTON_STYLE)
        self.closebutton.setFixedSize(28, 28)

        self.minimizebutton = QToolButton()
        self.minimizebutton.clicked.connect(self.window().showMinimized)
        self.minimizebutton.setIcon(QIcon(str(MINIMIZE_ICON_PATH)))
        self.minimizebutton.setFixedSize(28, 28)
        self.minimizebutton.setStyleSheet(MIN_BUTTON_STYLE)

        self.layout.addWidget(self.minimizebutton)
        self.layout.addWidget(self.closebutton)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.initialPos = event.position().toPoint()
        super().mousePressEvent(event)
        event.accept()

    def mouseMoveEvent(self, event):
        if self.initialPos is not None:
            delta = event.position().toPoint() - self.initialPos
            self.window().move(
                self.window().x() + delta.x(),
                self.window().y() + delta.y(),
            )
        super().mouseMoveEvent(event)
        event.accept()

    def mouseReleaseEvent(self, event):
        self.initialPos = None
        super().mouseReleaseEvent(event)
        event.accept()