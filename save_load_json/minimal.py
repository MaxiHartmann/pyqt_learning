# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtWidgets import QLineEdit
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc

# Only needed for access to command line arguments
import sys
import json


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.setFixedSize(qtc.QSize(400, 300))

        self.e1 = qtw.QLineEdit()
        self.e2 = qtw.QLineEdit()
        
        self.b1 = qtw.QPushButton("Save")
        self.b2 = qtw.QPushButton("Load")

        layout = qtw.QVBoxLayout()
        layout.addWidget(self.e1)
        layout.addWidget(self.e2)
        layout.addWidget(self.b1)
        layout.addWidget(self.b2)
        
        widget = qtw.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.b1.clicked.connect(self.save)
        self.b2.clicked.connect(self.load)
        self.filename = "test.json"


    def save(self):
        
        self.data = {}
        self.data["test"] = 1
        self.data["e1"] = self.e1.text()
        self.data["e2"] = self.e2.text()

        print("Save")
        with open(self.filename, 'w', encoding='utf-8') as writefile:
            json.dump(self.data, writefile, sort_keys=True, indent=4)


    def load(self):
        
        print("load")
        with open(self.filename, 'r') as f:
            data = json.load(f)

        
        self.e1.setText(data["e1"])
        self.e2.setText(data["e2"])

app = qtw.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
