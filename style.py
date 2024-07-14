from variables import MEDIUM_FONT_SIZE

COMMON_BUTTON_STYLE = f'''QPushButton {{
        background-color: #660033;
        color: #FFC0DF;
        font-size: {MEDIUM_FONT_SIZE}px;
        border-radius: 3px;
    }}
    QPushButton:hover {{
        background-color: #520029;
        color: #ECB6D1;
        font-size: {MEDIUM_FONT_SIZE}px;
        border-radius: 3px;
    }}
    QPushButton:pressed {{
        background-color: #36001B;
        color: #CE9AB4;
        font-size: {MEDIUM_FONT_SIZE}px;
        border-radius: 3px;
    }}'''

SPECIAL_BUTTON_STYLE = f'''QPushButton {{
        background-color: #94004A;
        color: #FFC0DF;
        font-size: {MEDIUM_FONT_SIZE}px;
        border-radius: 3px;
    }}
    QPushButton:hover {{
        background-color: #810041;
        color: #ECB6D1;
        font-size: {MEDIUM_FONT_SIZE}px;
        border-radius: 3px;
    }}
    QPushButton:pressed {{
        background-color: #690035;
        color: #CE9AB4;
        font-size: {MEDIUM_FONT_SIZE}px;
        border-radius: 3px;
    }}'''

EQUAL_BUTTON_STYLE = f'''QPushButton {{
        background-color: #FF0371;
        color: black;
        font-size: {MEDIUM_FONT_SIZE}px;
        border-radius: 3px;
    }}
    QPushButton:hover {{
        background-color: #A90A4F;
        color: black;
        font-size: {MEDIUM_FONT_SIZE}px;
        border-radius: 3px;
    }}
    QPushButton:pressed {{
        background-color: #000000;
        color: #C71585;
        font-size: {MEDIUM_FONT_SIZE}px;
        border-radius: 3px;
    }}'''

MIN_BUTTON_STYLE = f'''QToolButton {{
        border: none
    }}
    QToolButton:hover {{
        background-color: #292929;
        color: black;
        font-size: {MEDIUM_FONT_SIZE}px;
        border-radius: 3px;
    }}
    QToolButton:pressed {{
        background-color: #202020;
        color: #C71585;
        font-size: {MEDIUM_FONT_SIZE}px;
        border-radius: 3px;
    }}'''

CLOSE_BUTTON_STYLE = f'''QToolButton {{
        border: none
    }}
    QToolButton:hover {{
        background-color: #B30F0F;
        color: black;
        font-size: {MEDIUM_FONT_SIZE}px;
        border-radius: 3px;
    }}
    QToolButton:pressed {{
        background-color: #720404;
        color: #C71585;
        font-size: {MEDIUM_FONT_SIZE}px;
        border-radius: 3px;
    }}'''