import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

class MainWindow(QtWidgets.QMainWindow):

    path = "package/ressources/images/grille_"

    phrases = ["Quand tu as choisi, clique sur 'Start'",
               "Est-qu'il est dans la grille rouge",
               "Est-qu'il est dans la grille jaune",
               "Est-qu'il est dans la grille verte",
               "Est-qu'il est dans la grille bleu",
               "Est-qu'il est dans la grille violet"]

    cpt = 0

    def __init__(self):
        super().__init__()
        self.setWindowTitle("A quel nombre pense tu?")
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        #self.setup_connections()

    def create_widgets(self):
        # Creation du label pour inserer l'image
        self.lbl_image = QtWidgets.QLabel(self)

        # l'image dans le label
        self.image = QtGui.QImage(f"{self.path}{self.cpt}.jpg")
        self.pixmapImage = QtGui.QPixmap.fromImage(self.image)
        self.lbl_image.setPixmap(self.pixmapImage)
        self.lbl_image.setScaledContents(True)

        # Création du label pour le texte
        self.lbl_phrase = QtWidgets.QLabel(self.phrases[self.cpt])

        # Création des boutons
        self.btn_non = QtWidgets.QPushButton("Non")
        self.btn_non.setEnabled(False)
        #self.btn_non.clicked.connect(self.change_grille_non)

        self.btn_oui = QtWidgets.QPushButton("Oui")
        self.btn_oui.setEnabled(False)
        #self.btn_oui.clicked.connect(self.change_grille_oui)

        self.btn_start = QtWidgets.QPushButton('Start')
        self.btn_start.clicked.connect(self.button_start)


    def modify_widgets(self):
        self.lbl_phrase.setAlignment(QtCore.Qt.AlignCenter)

    def create_layouts(self):
        widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QGridLayout(widget)
        self.setCentralWidget(widget)

    def add_widgets_to_layouts(self):
        self.layout.addWidget(self.lbl_image, 0, 0, 1, 2)
        self.layout.addWidget(self.lbl_phrase, 1, 0, 1, 2)
        self.layout.addWidget(self.btn_non, 2, 0, 1, 1)
        self.layout.addWidget(self.btn_oui, 2, 1, 1, 1)
        self.layout.addWidget(self.btn_start, 3, 0, 1, 2)

    def button_start(self):
        self.cpt += 1
        self.image = QtGui.QImage(f"{self.path}{self.cpt}.jpg")
        self.pixmapImage = QtGui.QPixmap.fromImage(self.image)
        self.lbl_image.setPixmap(self.pixmapImage)
        self.lbl_image.setScaledContents(True)
        self.btn_start.setEnabled(False)
        self.btn_oui.setEnabled(True)
        self.btn_non.setEnabled(True)
        self.lbl_phrase.setText(self.phrases[self.cpt])

    """def button(self):
        while self.cpt < 5:
            self.cpt += 1
            return MainWindow.cpt
        else:
            self.btn_non.setEnabled(False)
            self.btn_oui.setEnabled(False)"""


    """def change_grille_non(self):
        self.button()
        # Passe a la grille suivante
        self.image = QtGui.QImage(f"{self.path}{self.cpt}.jpg")
        self.pixmapImage = QtGui.QPixmap.fromImage(self.image)
        self.lbl_image.setPixmap(self.pixmapImage)
        self.lbl_image.setScaledContents(True)
        # Modifie le label avec la nouvelle phrase
        self.lbl_info.setText(self.phrases["p_" + str(self.cpt)])"""


    """def change_grille_oui(self):
        self.button()
        # Passe a la grille suivante
        print(f'Cpt:{self.cpt}')
        print(f'Resultat:{self.resultat[self.cpt]}')
        self.image = QtGui.QImage(f"{self.path}{self.cpt}.jpg")
        self.pixmapImage = QtGui.QPixmap.fromImage(self.image)
        self.lbl_image.setPixmap(self.pixmapImage)
        self.lbl_image.setScaledContents(True)
        # Modifie le label avec la nouvelle phrase
        self.lbl_info.setText(self.phrases["p_" + str(self.cpt)])"""

    print(f"compteur: {cpt}")

# Aide placement sur grille
# ex: 1, 0, 1, 2
# ligne 1
# colonne 0
#
# prends 2 colonnes