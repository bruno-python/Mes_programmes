import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

def saluer():
    """ Fonction slot """
    if msg.text():
        msg.setText("")
    else:
        msg.setText(f'Hello Bruno')

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals et slots')
layout = QVBoxLayout()

btn = QPushButton('Saluer')
btn.clicked.connect(saluer) # cliquer pour saluer
#btn.clicked.connect(functools.partial(saluer, 'Bruno'))

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())

