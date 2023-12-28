import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction

def boutonPresse(bouton):
    print("Le bouton presse est le suivant: ", bouton.text())


def principal():
    application = QApplication(sys.argv)

    fenetre = QMainWindow()

    fenetre.setGeometry(100, 100, 200, 100)
    fenetre.setWindowTitle("QToolBar")

    barre = fenetre.addToolBar("Barre d'outils d'exemple")

    action1 = QAction("Creer")
    barre.addAction(action1)

    action2 = QAction("Ouvrir")
    barre.addAction(action2)

    action3 = QAction("Copier")
    barre.addAction(action3)

    action4 = QAction("Coller")
    barre.addAction(action4)

    barre.actionTriggered[QAction].connect(boutonPresse)

    fenetre.show()

    application.exec_()

if __name__ == '__main__':
    principal()
