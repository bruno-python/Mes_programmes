import sys

from PyQt5.QtWidgets import QApplication

from main_window_biblio import MainWindowBiblio


app = QApplication(sys.argv)
mainWindow = MainWindowBiblio()
mainWindow.show()

rc = app.exec_()
sys.exit(rc)