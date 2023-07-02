#!/bin/python3

import PyQt5.QtCore as qtc
import PyQt5.QtWidgets as qtw
import sys
import json
import glob
import pandas as pd
# import matplotlib.pyplot as plt
# matplotlib.use('Qt5Agg')

from setup import Setup
from mplcanvas import MplCanvas


class Window(qtw.QWidget):
    def __init__(self):
        qtw.QWidget.__init__(self)
        self.setFixedWidth(1200)
        self.setWindowTitle("Dataloader...")
        Hlayout = qtw.QHBoxLayout()
        self.setLayout(Hlayout)


        # Left
        Vlayout = qtw.QVBoxLayout()
        self.lineedit_path = qtw.QLineEdit("./data_1/")
        self.lineedit_name = qtw.QLineEdit("A")
        self.button_add = qtw.QPushButton("Add Path")
        self.button_plot = qtw.QPushButton("plot")
        self.button_print_setups = qtw.QPushButton("Print setups")
        self.button_close = qtw.QPushButton("Close")

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

        
        Hlayout.addLayout(Vlayout)
        self.sc = MplCanvas(self, width=8, height=5, dpi=100)
        Hlayout.addWidget(self.sc)


        ###################
        #### Connect Buttons
        #--->
        self.button_add.clicked.connect(self.init_setup)
        self.button_plot.clicked.connect(self.plot)
        self.button_close.clicked.connect(self.close)
        self.button_print_setups.clicked.connect(self.print_setups)
        self.tabwidget.tabCloseRequested.connect(lambda index: self.delete_data(index))



        self.list_setups = []
        self.current_setup_idx = -1

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
        listwidget.itemClicked.connect(self.set_selected_probes)

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
        self.current_setup_idx = len(self.list_setups) - 1 
        self.tabwidget.setCurrentIndex(self.current_setup_idx)

    def plot(self):
        self.read_files()
        self.print_data()
        self.create_matplotlib()


    def create_matplotlib(self):

        self.sc.axes.clear()

        for s in self.list_setups:
            if s.probefiles[s.selected_probe] != "None":

                x = s.data['x']
                y = s.data['y']
                l = f"{s.name}:p{s.selected_probe}"
                self.sc.axes.plot(x, y, label=l)

        self.sc.axes.legend()
        self.sc.draw()

        

    def set_selected_probes(self):
        current_tab = self.current_setup_idx
        tab = self.tabwidget.widget(current_tab)
        listwidget = tab.findChild(qtw.QListWidget)
        selected_row = listwidget.currentRow()
        self.list_setups[current_tab].selected_probe = selected_row
        # print(f"Current tab: {current_tab} {selected_row} {listwidget.currentItem().text()}")

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
