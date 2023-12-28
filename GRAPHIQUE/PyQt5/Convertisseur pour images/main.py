import sys

from PyQt5.QtWidgets import QApplication

from package.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open("package/ressources/style/style.css").read())
    window = MainWindow()
    window.resize(1920 // 4, 1080 // 2)
    window.show()
    sys.exit(app.exec_())
