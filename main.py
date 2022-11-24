import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    text_label = QLabel(widget)
    text_label.setText("Hello GitHub!")
    text_label.move(110,85)

    widget.setGeometry(50,50,320,200)
    widget.setWindowTitle("PyQt5 Example")
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()

