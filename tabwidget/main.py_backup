#!/bin/python3

import PyQt5.QtCore as qtc
import PyQt5.QtWidgets as qtw
import sys
import json
import glob
import pandas as pd

from .setup import Setup

class Window(qtw.QWidget):
    def __init__(self):
        qtw.QWidget.__init__(self)
        Vlayout = qtw.QVBoxLayout()
        self.setWindowTitle("Create tabs...")
        self.setFixedWidth(500)


        self.lineedit_path = qtw.QLineEdit("./data_1/")
        self.lineedit_name = qtw.QLineEdit("A")
        self.button_add = qtw.QPushButton("Add Path")
        # self.button_search = qtw.QPushButton("Search...")
        self.button_plot = qtw.QPushButton("plot")
        self.button_print_setups = qtw.QPushButton("Print setups")
        self.button_close = qtw.QPushButton("Close")

        self.setLayout(Vlayout)
        self.tabwidget = qtw.QTabWidget()
        self.tabwidget.setTabsClosable(True)

        Hlayout_1 = qtw.QHBoxLayout()
        label = qtw.QLabel("Path:")
        Hlayout_1.addWidget(label)
        Hlayout_1.addWidget(self.lineedit_path)

        Hlayout_2 = qtw.QHBoxLayout()
        label = qtw.QLabel("Name:")
        Hlayout_2.addWidget(label)
        Hlayout_2.addWidget(self.lineedit_name)

        Vlayout.addLayout(Hlayout_1)
        Vlayout.addLayout(Hlayout_2)
        Vlayout.addWidget(self.button_add)
        # Vlayout.addWidget(self.button_search)
        Vlayout.addWidget(self.tabwidget)
        Vlayout.addWidget(self.button_plot)
        Vlayout.addWidget(self.button_print_setups)
        Vlayout.addWidget(self.button_close)

        self.button_add.clicked.connect(self.add_setup)
        # self.button_search.clicked.connect(self.search_for_probes)
        self.button_plot.clicked.connect(self.plot)
        self.button_close.clicked.connect(self.close)
        self.button_print_setups.clicked.connect(self.print_setups)
        self.tabwidget.tabCloseRequested.connect(lambda index: self.delete_data(index))

        self.list_setups = []

    def print_setups(self):
        for setup in self.list_setups:
            print(json.dumps(setup, indent=4))


    def init_setup(self):
        name = self.lineedit_name.text()
        path = self.lineedit_path.text()
        s = Setup(name, path)
        self.list_setups.append(s)



    def add_setup(self):
        name = self.lineedit_name.text()
        path = self.lineedit_path.text()

        index = len(self.list_setups)

        new_name = name
        prefix = 2
        previous_names = [n["name"] for n in self.list_setups]
        while (new_name in previous_names):
            new_name = f"{name}_{prefix}"
            prefix += 1

        self.list_setups.append({
            "name": new_name, 
            "path": path})

        print(f"create new Dataset: {new_name} from {path}")

        for setup in self.list_setups:
            print(f"{setup}")

        tab = qtw.QWidget()
        Vlayout = qtw.QVBoxLayout()
        Vlayout.addWidget(qtw.QLabel(path))
        Vlayout.addWidget(qtw.QListWidget())
        tab.setLayout(Vlayout)
        self.tabwidget.addTab(tab, new_name)

        self.tabwidget.setCurrentIndex(self.tabwidget.count() - 1)

        self.search_for_probes()

        

    def plot(self):
        self.set_selected_probes()
        self.read_files()
        self.print_data()


    def set_selected_probes(self):
        for i in range(self.tabwidget.count()):
            tab = self.tabwidget.widget(i)
            # index = self.tabwidget.currentIndex()
            listwidget = tab.findChild(qtw.QListWidget)
            selected_row = listwidget.currentRow()
            # print(f"probe_idx: {selected_row}")
            self.list_setups[i]["Selected_probe"] = selected_row

    def read_files(self):
        for setup in self.list_setups:
            probe_idx = setup["Selected_probe"]
            filename = setup["Probes"][probe_idx]

            if filename != "None":
                df = pd.read_csv(filename)
                setup["Data"] = df.to_dict()
            else:
                setup.pop("Data", None)


    def print_data(self):
        for setup in self.list_setups:
            df = setup["Data"]
            probename = setup["Probes"][setup["Selected_probe"]]
            print(f"{probename}")
            print(df)


    def search_for_probes(self):
        index = self.tabwidget.currentIndex()

        if index != -1:
            setup = self.list_setups[index]
            path = setup["path"]
            print(f"current index: {index} -- search in {path}") 

            files = glob.glob(f"{path}**/*probe*.csv", recursive=True)
            files.sort()
            files.append("None")
            setup["Probes"] = files
            setup["Selected_probe"] = 0
            tab = self.tabwidget.currentWidget()
            listwidget = tab.findChild(qtw.QListWidget)
            listwidget.clear()

            for f in files:
                f = f.replace(path, '')
                print(f"Found: {f}")
                qtw.QListWidgetItem(f, listwidget)
            listwidget.setCurrentRow(setup["Selected_probe"])

        else:
            print("No setups loaded!")



    def delete_data(self, index):

        self.tabwidget.removeTab(index)
        print(f"-->remove index: {index}")
        del self.list_setups[index]
        for setup in self.list_setups:
            print(f"{setup}")

app = qtw.QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())

