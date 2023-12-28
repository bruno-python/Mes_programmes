import sys

from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar
from PyQt5.QtCore import QTimer

# définition d'une classe FenetreSimple qui hérite de QWidget
class FenetreSimple(QWidget):
    def __init__(self):
        super().__init__()
        self.execute()

    def execute(self):
        self.resize(500, 300)
        self.move(50, 500)
        self.setWindowTitle("Exemple QProgressBar")

        self.progress = QProgressBar(self)
        self.progress.setGeometry(5, 20, 350, 20)
        self.progress.setValue(0)

        self.show()

        self.timer =QTimer(self)
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(100)

    def handleTimer(self):
        valeur = self.progress.value()
        if valeur < 100:
            valeur = valeur + 5
            self.progress.setValue(valeur)
        else:
            self.timer.stop()


if __name__ == '__main__':
    application = QApplication(sys.argv)
    fenetre = FenetreSimple()
    sys.exit(application.exec_())
