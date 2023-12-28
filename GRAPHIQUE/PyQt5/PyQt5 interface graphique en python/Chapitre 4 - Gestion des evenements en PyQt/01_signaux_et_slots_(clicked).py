import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton

class FenetreSimple(QWidget):

    def __init__(self):
        super().__init__()
        self.execute()

    def exempleSlot(self):
        print("Le bouton a ete appuye.")

    def execute(self):
        self.disposition = QVBoxLayout()

        self.resize(250, 300)
        self.move(50, 300)
        self.setWindowTitle("Signaux et slots")

        # premiere façon de connecter le signal et le slot (rajouter la partie grisé aprés "Fermer")
        self.fermer = QPushButton("Fermer") #, clicked=self.exempleSlot
        self.disposition.addWidget(self.fermer)

        # deuxième façon de connecter le signal au slot
        self.fermer.clicked.connect(self.exempleSlot)

        self.setLayout(self.disposition)
        self.show()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    sys.exit(application.exec_())