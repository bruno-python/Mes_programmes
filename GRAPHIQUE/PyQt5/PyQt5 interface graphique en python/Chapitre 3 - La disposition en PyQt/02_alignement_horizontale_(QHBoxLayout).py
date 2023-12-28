from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

# Création de la fenêtre
app = QApplication([])
fenetre = QWidget()

# disposition a l'horizontale
disposition = QHBoxLayout()

disposition.addWidget(QPushButton('Premier'))
disposition.addWidget(QPushButton('Deuxieme'))
disposition.addWidget(QPushButton('Troisieme'))
disposition.addWidget(QPushButton('Quatrieme'))
disposition.addWidget(QPushButton('Cinquuieme'))

fenetre.setLayout(disposition)

fenetre.show()
app.exec_()
