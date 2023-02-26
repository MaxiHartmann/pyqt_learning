import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import uic
import pandas as pd
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Ui(qtw.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("layout.ui", self)

        # load raw data
        self.raw_data = pd.read_csv("./data/sinus.csv")
        self.textEdit.setText(self.raw_data.to_string())

        # create figure
        self.sc = MplCanvas(self, width=8, height=6, dpi=100)
        self.sc.axes.plot()

        self.horizontal_layout = qtw.QHBoxLayout(self.frame_plot)
        self.horizontal_layout.addWidget(self.sc)

        self.update_plot()
        self.show()

        # Connect to functions
        self.btn_plot.clicked.connect(self.update_plot)
        self.spinbox_start.valueChanged.connect(self.update_plot)
        self.spinbox_end.valueChanged.connect(self.update_plot)


    def update_plot(self):
        self.truncate_data()
        self.sc.axes.cla()
        x0 = self.raw_data["x"]
        y0 = self.raw_data["y"]
        x1 = self.data["x"]
        y1 = self.data["y"]
        self.sc.axes.plot(x0, y0, label='raw')
        self.sc.axes.plot(x1, y1, color='red', label='selection')

        self.sc.axes.axvline(self.spinbox_start.value(), color='black')
        self.sc.axes.axvline(self.spinbox_end.value(), color='black')
        self.sc.axes.legend()
        self.sc.draw()

    def truncate_data(self):
        xmin = self.spinbox_start.value()
        xmax = self.spinbox_end.value()
        df = self.raw_data
        self.data = df.loc[(df['x'] >= xmin) & (df['x'] <= xmax)]

    def add_selection_to_plot(self):
        # todo 
        # just change the selected data in plot
        pass




if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())
