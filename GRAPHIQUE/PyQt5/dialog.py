import sys

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout

class Dialog(QDialog):
    """ Dialog """
    def __init__(self, parent= None):
        """ initialise """
        super().__init__(parent)
        self.setWindowTitle('QDialog')
        dlgLayout = QVBoxLayout()
        fromLayout = QFormLayout()
        fromLayout.addRow('Name:', QLineEdit())
        fromLayout.addRow('Age:', QLineEdit())
        fromLayout.addRow('Job:', QLineEdit())
        fromLayout.addRow('Hobbies:', QLineEdit())
        dlgLayout.addLayout(fromLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
