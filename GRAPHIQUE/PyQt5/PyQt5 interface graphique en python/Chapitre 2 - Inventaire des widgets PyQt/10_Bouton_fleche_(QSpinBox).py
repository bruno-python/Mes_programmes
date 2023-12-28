import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSpinBox
from PyQt5.QtCore import *

# définition d'une classe FenetreSimple qui hérite de QWidget
class FenetreSimple(QWidget):
    def __init__(self):
        super().__init__()
        self.execute()

    def execute(self):
        self.resize(250, 300)
        self.move(50, 500)
        self.setWindowTitle("Exemple QSpinBox")

        self.label = QLabel("", self)
        self.label.move(5, 5)
        self.label.resize(150, 20)

        self.spinner = QSpinBox(self)
        self.spinner.move(5, 35)
        self.spinner.valueChanged.connect(self.valuechange)

        self.show()

    def valuechange(self):
        self.label.setText("Valeur courante : " + str(self.spinner.value()))

if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    sys.exit(application.exec_())
