import sys
from PyQt5.QtWidgets import QTabWidget, QWidget, QApplication, QFormLayout, QVBoxLayout, QHBoxLayout, QLineEdit, QCheckBox

# classe et initialisateur

class MyQTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super (MyQTabWidget, self).__init__(parent)
        self.onglet1 = QWidget()
        self.onglet2 = QWidget()
        self.onglet3 = QWidget()

        # Création des onglets
        self.addTab(self.onglet1, "Données gènèrales")
        self.addTab(self.onglet2, "Sports préféres")
        self.addTab(self.onglet3, "Loisirs culturels préféres")

        self.creationOnglet1()
        self.creationOnglet2()
        self.creationOnglet3()

        self.setWindowTitle("QTabWidget")

    # Remplissage de l'onglet 1
    def creationOnglet1(self):
        disposition = QFormLayout()
        disposition.addRow("Nom", QLineEdit())
        disposition.addRow("Prénom", QLineEdit())
        disposition.addRow("Ville", QLineEdit())
        self.setTabText(0, "Données gènèrales") # onglet 1
        self.onglet1.setLayout(disposition)

    # Remplissage de l'onglet 2
    def creationOnglet2(self):
        disposition = QVBoxLayout()
        disposition.addWidget(QCheckBox("Football"))
        disposition.addWidget(QCheckBox("Cyclisme"))
        disposition.addWidget(QCheckBox("Tennis"))
        self.setTabText(1, "Sports préféres") # onglet 2
        self.onglet2.setLayout(disposition)

    # Remplissage de l'onglet 3
    def creationOnglet3(self):
        disposition = QHBoxLayout()
        disposition.addWidget(QCheckBox("Visite de musées"))
        disposition.addWidget(QCheckBox("Musique"))
        disposition.addWidget(QCheckBox("Dessin et arts graphiques"))
        self.setTabText(2, "Loisirs culturels préféres") # onglet 3
        self.onglet3.setLayout(disposition)


def principal():
    application = QApplication(sys.argv)
    composant = MyQTabWidget()
    composant.show()
    sys.exit(application.exec_())



if __name__ == '__main__':
    principal()