import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        self.setWindowTitle("Hello World")
        self.setGeometry(100, 100, 500, 500)

        # Your code ends here
        self.show()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
