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

        self.setWindowModality(Qt.ApplicationModal)

        self.show()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    #print("Fenetre modale? : "+ str(fenetre.isModal()))
    print(f"Fenetre modale? : {str(fenetre.isModal())}")

    sys.exit(application.exec_())


# une fenêtre modale est une fenêtre qu prend le contrôle du clavier, elle est en attente d'une action utilisateur et interdit toute autre action


