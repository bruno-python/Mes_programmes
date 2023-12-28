import sys

# import 'QApplication' and tous les widgets
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# creation d'une instance de 'QApplication'
application = QApplication(sys.argv)

# creation d'une instance de mon application graphique
window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)

# affiche mon application graphique
window.show()

# execute en boucle l'application
sys.exit(application.exec_())
