import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import *

# définition d'une classe FenetreSimple qui hérite de QWidget
class FenetreSimple(QWidget):
    def __init__(self):
        super().__init__()
        self.execute()

    def execute(self):
        self.resize(250, 250)
        self.move(0, 500)
        self.setWindowTitle("Bonjour tout le monde! ")

        self.setWindowFlags(Qt.Popup) # Qt.Popup, Qt.Widget, Qt.Window, Qt.Dialog, Qt.ToolTip, Qt.SplashScreen

        self.show()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    application.setOverrideCursor(Qt.WaitCursor) # WaitCursor => curseur d'attente
    sys.exit(application.exec_())

