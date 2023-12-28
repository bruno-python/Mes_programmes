# Layout Vertical

import sys

# import 'QApplication' and tous les widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QHBoxLayout')
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())