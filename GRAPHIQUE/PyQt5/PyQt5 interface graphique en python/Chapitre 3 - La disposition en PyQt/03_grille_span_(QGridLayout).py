from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
# Création de la fenêtre
app = QApplication([])
fenetre = QWidget()

fenetre.setGeometry(100, 100, 200, 100)
fenetre.setWindowTitle("QGridLayout span")

disposition = QGridLayout()

# (0 => ligne), (0 => colonne), (2 => portée ligne), (2 => portée colonne), (direction)
disposition.addWidget(QPushButton('0-1-3-4'), 0, 0, 2, 2, Qt.AlignRight)
disposition.addWidget(QPushButton('2'), 0, 2)
disposition.addWidget(QPushButton('5'), 1, 2)
disposition.addWidget(QPushButton('6'), 2, 0)
disposition.addWidget(QPushButton('7'), 2, 1)
disposition.addWidget(QPushButton('8'), 2, 2)
disposition.addWidget(QPushButton('9'), 3, 0)
disposition.addWidget(QPushButton('+'), 3, 1)
disposition.addWidget(QPushButton('='), 3, 2)

fenetre.setLayout(disposition)

fenetre.show()
app.exec_()