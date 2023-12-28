import sys

from PyQt5 import QtWidgets, QtGui, QtCore, QtCore

class MainWindow:

    phrases ={"p_0" : "Quand tu as choisi, clique sur 'Start'",
              "p_1" : "Est-qu'il est dans la grille rouge",
              "p_2" : "Est-qu'il est dans la grille jaune",
              "p_3" : "Est-qu'il est dans la grille verte",
              "p_4" : "Est-qu'il est dans la grille bleu",
              "p_5" : "Est-qu'il est dans la grille violet"
             }
    resultat = {1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}
    cpt = 0

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setStyleSheet(open("package/ressources/style/style.css").read())
        self.window = QtWidgets.QMainWindow()

        # Chemin de l'image de la grille
        self.path = "package/ressources/images/grille_"

        self.init_Gui()

        self.window.setWindowTitle("A quel nombre pense tu?")
        self.window.setGeometry(800, 300, 475, 600)
        self.window.show()
        sys.exit(self.app.exec_())

    # Creé la fonction qui initialise la GUI
    def init_Gui(self):
        # Creation du label pour inserer l'image
        self.lbl_image = QtWidgets.QLabel(self.window)
        self.lbl_image.setGeometry(38, 38, 400, 400)

        # l'image dans le label
        self.image = QtGui.QImage(f"{self.path}{self.cpt}.jpg")
        self.pixmapImage = QtGui.QPixmap.fromImage(self.image)

        self.lbl_image.setPixmap(self.pixmapImage)
        self.lbl_image.setScaledContents(True)

        # Création du label pour le texte
        self.lbl_info = QtWidgets.QLabel(self.phrases["p_" + str(self.cpt)], self.window)
        self.lbl_info.setGeometry(120, 450, 250, 30)

        # Création des boutons
        self.btn_oui = QtWidgets.QPushButton("Oui", self.window)
        self.btn_oui.setGeometry(250, 500, 120, 30)
        self.btn_oui.setEnabled(False)
        self.btn_oui.clicked.connect(self.change_grille_oui)

        self.btn_non = QtWidgets.QPushButton("Non", self.window)
        self.btn_non.setGeometry(100, 500, 120, 30)
        self.btn_non.clicked.connect(self.change_grille_non)
        self.btn_non.setEnabled(False)

        self.btn_start = QtWidgets.QPushButton("Start", self.window)
        self.btn_start.setGeometry(180, 550,120, 30)
        self.btn_start.clicked.connect(self.button_start)


    def button_start(self):
        self.cpt = self.cpt + 1
        self.image = QtGui.QImage(f"{self.path}{self.cpt}.jpg")
        self.pixmapImage = QtGui.QPixmap.fromImage(self.image)
        self.lbl_image.setPixmap(self.pixmapImage)
        self.lbl_image.setScaledContents(True)
        self.btn_start.setEnabled(False)
        self.btn_oui.setEnabled(True)
        self.btn_non.setEnabled(True)
        self.lbl_info.setText(self.phrases["p_" + str(self.cpt)])

    def button(self):
        while self.cpt < 5:
            self.cpt += 1
            return MainWindow.cpt
        else:
            self.btn_non.setEnabled(False)
            self.btn_oui.setEnabled(False)


    def change_grille_non(self):
        self.button()
        # Passe a la grille suivante
        self.image = QtGui.QImage(f"{self.path}{self.cpt}.jpg")
        self.pixmapImage = QtGui.QPixmap.fromImage(self.image)
        self.lbl_image.setPixmap(self.pixmapImage)
        self.lbl_image.setScaledContents(True)
        # Modifie le label avec la nouvelle phrase
        self.lbl_info.setText(self.phrases["p_" + str(self.cpt)])


    def change_grille_oui(self):
        self.button()
        # Passe a la grille suivante
        print(f'Cpt:{self.cpt}')
        print(f'Resultat:{self.resultat[self.cpt]}')
        self.image = QtGui.QImage(f"{self.path}{self.cpt}.jpg")
        self.pixmapImage = QtGui.QPixmap.fromImage(self.image)
        self.lbl_image.setPixmap(self.pixmapImage)
        self.lbl_image.setScaledContents(True)
        # Modifie le label avec la nouvelle phrase
        self.lbl_info.setText(self.phrases["p_" + str(self.cpt)])


nain = MainWindow()


