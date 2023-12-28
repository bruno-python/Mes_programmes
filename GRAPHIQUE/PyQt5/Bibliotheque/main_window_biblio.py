from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout

class MainWindowBiblio(QMainWindow):
    def __init__(self):
        super(MainWindowBiblio, self).__init__()

        #self.resize(300, 150)
        self.setWindowTitle("BiblioApp")
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.label = QLabel("Titre", self.centralWidget)
        self.lineEditTitre = QLineEdit(self.centralWidget)
        self.pushbuttonOk = QPushButton("OK", self.centralWidget)

        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.addWidget(self.label)
        self.hBoxLayout.addWidget(self.lineEditTitre)
        self.vBoxLayout = QVBoxLayout(self.centralWidget)
        self.vBoxLayout.addLayout(self.hBoxLayout)
        self.vBoxLayout.addWidget(self.pushbuttonOk)
        self.pushbuttonOk.clicked.connect(self.onPushButtonOkClicked)

    def onPushButtonOkClicked(self):
        QMessageBox.information(self, "Info", "Titre : " + self.lineEditTitre.text())


