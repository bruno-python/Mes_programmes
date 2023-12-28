import sys

from PyQt5 import QtWidgets

from package.main_window import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open("package/ressources/style/style.css").read())
    window = MainWindow()
    window.resize(400, 500)
    window.show()
    sys.exit(app.exec_())
