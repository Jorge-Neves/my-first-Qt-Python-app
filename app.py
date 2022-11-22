import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QWidgets.QWidget):
    def __ini__(self):
        super().__init__()

        self.hello = ["Hello GitHub", "Olá GitHub", "Bonjour GitHub"]

        self.button = QtWidgets.QPushButton("Click")
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))