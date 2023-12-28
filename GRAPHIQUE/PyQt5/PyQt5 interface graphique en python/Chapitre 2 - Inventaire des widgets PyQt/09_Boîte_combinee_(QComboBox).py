import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox
from PyQt5.QtCore import *

# définition d'une classe FenetreSimple qui hérite de QWidget
class FenetreSimple(QWidget):
    def __init__(self):
        super().__init__()
        self.execute()

    def execute(self):
        self.resize(250, 300)
        self.move(50, 500)
        self.setWindowTitle("Exemple QComboBox")

        self.label = QLabel("Utilisation de QComBox", self)
        self.label.move(5, 5)

        self.cb = QComboBox(self)
        self.cb.addItem("France")
        self.cb.addItem("Italie")
        self.cb.addItems(["Espagne", 'Allemagne', 'Belgique'])
        self.cb.move(5, 30)
        self.cb.currentIndexChanged.connect(self.selectionchange)

        self.show()

        for i in range(self.cb.count()):
            print(self.cb.itemText(i))

    def selectionchange(self, i):
        self.label.setText(self.cb.currentText())

if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    sys.exit(application.exec_())
