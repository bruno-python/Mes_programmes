import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

# creation d'une sous classe de QMainWindow
class PyCalcUI(QMainWindow):
    """ PyCalc (GUI) """
    def __init__(self):
        super().__init__()
        # Propriete de la fenêtre
        self.setWindowTitle('PyCalc')
        self.setFixedSize(235, 235)
        # Widget central
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

def main():
    # Creation d'une instance de QApplication
    pycalc = QApplication(sys.argv)
    # Affiche la calculatrice
    view = PyCalcUI()
    view.show()
    # Execute la boucle main
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()

