import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap

# définition d'une classe FenetreSimple qui hérite de QWidget
class FenetreSimple(QWidget):
    def __init__(self):
        super().__init__()
        self.execute()

    def execute(self):
        self.resize(250, 250)
        self.move(0, 500)
        self.setWindowTitle("Bonjour tout le monde! ")

        label1 = QLabel("PyQt", self)
        label1.setText(label1.text() + '5')
        label1.setMargin(5)
        label1.setIndent(15)

        self.show()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    sys.exit(application.exec_())
