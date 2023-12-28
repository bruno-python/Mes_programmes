import sys
from PyQt5.QtWidgets import QApplication, QWidget

# définition d'une classe FenetreSimple qui hérite de QWidget
class FenetreSimple(QWidget):
    def __init__(self):
        super().__init__()
        self.execute()

    def execute(self):
        self.resize(250, 250)
        self.move(0, 500)
        self.setWindowTitle("Bonjour tout le monde! ")
        self.show()

application = QApplication(sys.argv)
fenetre = FenetreSimple()
sys.exit(application.exec_())







