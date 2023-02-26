import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import uic


class Ui(qtw.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi("layout.ui", self)
        self.show()



if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())

