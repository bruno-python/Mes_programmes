import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt5.QtCore import *

# définition d'une classe FenetreSimple qui hérite de QWidget
class FenetreSimple(QWidget):
    def __init__(self):
        super().__init__()
        self.execute()

    def execute(self):
        self.resize(250, 300)
        self.move(50, 500)
        self.setWindowTitle("Exemple QLineEdit ")

        label = QLabel("Nom : ", self)
        label.move(5, 5)

        line_edit = QLineEdit(self)
        line_edit.move(5, 30)
        line_edit.resize(150, 20)
        line_edit.setText("Valeur par défaut")

        self.show()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    sys.exit(application.exec_())
