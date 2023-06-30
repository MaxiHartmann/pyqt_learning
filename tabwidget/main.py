#!/bin/python3

import PyQt5.QtCore as qtc
import PyQt5.QtWidgets as qtw
import sys
import json
import glob
import pandas as pd

from setup import Setup

class Window(qtw.QWidget):
    def __init__(self):
        qtw.QWidget.__init__(self)
        Vlayout = qtw.QVBoxLayout()
        self.setWindowTitle("Create tabs...")
        self.setFixedWidth(500)


        self.lineedit_path = qtw.QLineEdit("./data_1/")
        self.lineedit_name = qtw.QLineEdit("A")
        self.button_add = qtw.QPushButton("Add Path")
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
        Vlayout.addWidget(self.tabwidget)
        Vlayout.addWidget(self.button_plot)
        Vlayout.addWidget(self.button_print_setups)
        Vlayout.addWidget(self.button_close)

        ###################
        #### Connect Buttons
        #--->
        self.button_add.clicked.connect(self.init_setup)
        self.button_plot.clicked.connect(self.plot)
        self.button_close.clicked.connect(self.close)
        self.button_print_setups.clicked.connect(self.print_setups)
        self.tabwidget.tabCloseRequested.connect(lambda index: self.delete_data(index))

        self.list_setups = []

    def print_setups(self):
        for setup in self.list_setups:
            setup.print_setup() 

    def init_setup(self):
        name = self.lineedit_name.text()
        path = self.lineedit_path.text()
        s = Setup(name, path)
        self.list_setups.append(s)

        self.create_tab(s)

    def create_tab(self, setup):
        name = setup.name
        path = setup.path

        tab = qtw.QWidget()
        listwidget = qtw.QListWidget()

        files = setup.probefiles

        listwidget.clear()
        for f in files:
            f = f.replace(path, '')
            print(f"Found: {f}")
            qtw.QListWidgetItem(f, listwidget)
            listwidget.setCurrentRow(setup.selected_probe)

        Vlayout = qtw.QVBoxLayout()
        Vlayout.addWidget(qtw.QLabel(path))
        Vlayout.addWidget(listwidget)
        tab.setLayout(Vlayout)
        self.tabwidget.addTab(tab, name)
        self.tabwidget.setCurrentIndex(self.tabwidget.count() - 1)

    def plot(self):
        self.set_selected_probes()
        self.read_files()
        self.print_data()

    def set_selected_probes(self):
        for i in range(self.tabwidget.count()):
            tab = self.tabwidget.widget(i)
            listwidget = tab.findChild(qtw.QListWidget)
            selected_row = listwidget.currentRow()
            self.list_setups[i].selected_probe = selected_row

    def read_files(self):
        for setup in self.list_setups:
            probe_idx = setup.selected_probe
            setup.load_data(probe_idx)

    def print_data(self):
        for setup in self.list_setups:
            df = setup.data
            probename = setup.probefiles[setup.selected_probe]
            print(f"{probename}")
            print(df)

    def delete_data(self, index):
        self.tabwidget.removeTab(index)
        print(f"-->remove index: {index}")
        del self.list_setups[index]
        for setup in self.list_setups:
            print(f"{setup.name}")

app = qtw.QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())

