import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLineEdit, QPushButton

class FenetreSimple(QWidget):

    def __init__(self):
        super().__init__()
        self.execute()

    def exempleSlot(self):
        # copie le texte de la premiere ligne vers la deuxieme
        textCourant = self.edition.text()
        self.editionCopie.setText(textCourant)


    def execute(self):
        self.disposition = QVBoxLayout()

        self.resize(250, 300)
        self.move(50, 300)
        self.setWindowTitle("Signaux et slots")

        # premiere ligne
        self.edition = QLineEdit()
        self.disposition.addWidget(self.edition)

        # deuxieme ligne
        self.editionCopie = QLineEdit()
        self.disposition.addWidget(self.editionCopie)

        self.edition.textChanged.connect(self.exempleSlot) # connecte le signal vers le slot

        self.setLayout(self.disposition)
        self.show()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    sys.exit(application.exec_())