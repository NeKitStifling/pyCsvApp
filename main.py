from PyQt5 import QtWidgets, QtGui,QtCore, Qt
import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QColorDialog, QFontDialog, QApplication, QMainWindow, QGridLayout,QWidget,QTableView, QTableWidget, QTableWidgetItem, qApp, QApplication, QMessageBox, QFileDialog 
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QToolBar, QAction
import pandas as pd
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
import sklearn.preprocessing
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from scipy.interpolate import interp1d



class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


class MainWindow(QMainWindow):

    global df1

    def __init__(self):
        super().__init__()
        uic.loadUi("design.ui", self)
        self.title = 'App for opperations with CSV by Ustinov Nikita'
        self.setWindowIcon(QtGui.QIcon('img/TeaBag.jpg'))
        self.statusBar().showMessage('Developed by Nikita Ustinov student from group FI901 in the year 2022. Program is working')
        self.mainScreenButtons()
        self.menuButtons()
        self.toolButtons()
        self.show()

    def mainScreenButtons(self):
        self.exitButton.clicked.connect(qApp.quit)
        # self.linearButton.clicked.connect(self.interpolation)
        self.maleRadio.toggled.connect(self.maleSelected)
        self.femaleRadio.toggled.connect(self.femaleSelected)
        self.primerButton.clicked.connect(self.graph1)
        self.myltiButton.clicked.connect(self.graph2)
        self.subplButton.clicked.connect(self.graph3)
        self.dat3DButton.clicked.connect(self.graph4)
        self.linearButton.clicked.connect(self.linearFunc)
        self.timeButton.clicked.connect(self.timeFunc)
        self.indexButton.clicked.connect(self.indexFunc)
        self.valuesButton.clicked.connect(self.valuesFunc)
        self.padButton.clicked.connect(self.padFunc)
        self.nearestButton.clicked.connect(self.nearestFunc)
        self.zeroButton.clicked.connect(self.zeroFunc)
        self.slinearButton.clicked.connect(self.slinearFunc)
        self.quadraticButton.clicked.connect(self.quadraticFunc)
        self.cubicButton.clicked.connect(self.cubicFunc)
        self.splineButton.clicked.connect(self.splineFunc)
        self.barycentricButton.clicked.connect(self.barycentricFunc)
        self.kroghButton.clicked.connect(self.kroghFunc)
        self.piePolButton.clicked.connect(self.piecewisePolynominalFunc)
        self.pchipButton.clicked.connect(self.pchipFunc)
        self.akimaButton.clicked.connect(self.akimaFunc)
        self.cubicsplineButton.clicked.connect(self.cubicsplineFunc)
        self.showGraph.clicked.connect(self.showGraphFunc)
        self.showGraph2.clicked.connect(self.showGraphFunc2)
        self.reset1.clicked.connect(self.tableReset)
        self.reset2.clicked.connect(self.tableReset2)

        # self.graphComBox.activated[str].connect(self.graph)



    def menuButtons(self):
        self.actionExit.triggered.connect(qApp.quit)
        self.actionOpenFile.triggered.connect(self.openCSV)
        self.actionPrint.triggered.connect(self.printDialog)
        self.actionFont.triggered.connect(self.fontDialog)
        self.actionColor.triggered.connect(self.colorDialog)

    def toolButtons(self):
        self.toolExit.triggered.connect(qApp.quit)
        self.toolPrint.triggered.connect(self.printDialog)

    def openCSV(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.csv)")
        f = open(fname[0], 'r')
        global df1
        df1 = pd.read_csv(f)
        model = pandasModel(df1)
        view = QTableView()
        view.setModel(model)
        self.tableView.setModel(model)

    def fontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.tableView.setFont(font)
            self.tableView2.setFont(font)


    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.tableView.print_(printer)

    def colorDialog(self):
        color = QColorDialog.getColor()
        self.tableView.setTextColor(color)

    def maleSelected(self, selected):
        if selected:
            self.genderSelectionLabel.setText("You are male")

    def femaleSelected(self, selected):
        if selected:
            self.genderSelectionLabel.setText("You are female")

    new_window = Toplevel()

    def graph1(new_window):
            from graph import primer1
    def graph2(new_window):
            from graph import mylti
    def graph3(new_window):
            from graph import subplot
    def graph4(new_window):
            from graph import data3D




    # def graph(new_window):
    #     print ("pepe")

    def linearFunc(self):
        global y
        y=df1.interpolate(method="linear")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)
    
    def timeFunc(self):
        global y
        y=df1.interpolate(method="time")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)
    
    def indexFunc(self):
        global y
        y=df1.interpolate(method="index")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)

    def valuesFunc(self):
        global y
        y=df1.interpolate(method="values")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)
    
    def padFunc(self):
        global y
        y=df1.interpolate(method="pad")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)

    def nearestFunc(self):
        global y
        y=df1.interpolate(method="nearest")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)

    def zeroFunc(self):
        global y
        y=df1.interpolate(method="zero")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)

    def slinearFunc(self):
        global y
        y=df1.interpolate(method="slinear")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)

    def quadraticFunc(self):
        global y
        y=df1.interpolate(method="quadratic")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)
    
    def cubicFunc(self):
        global y
        y=df1.interpolate(method="cubic")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)
    
    def splineFunc(self):
        global y
        y=df1.interpolate(method="spline", order=2)
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)

    def barycentricFunc(self):
        global y
        y=df1.interpolate(method="barycentric")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)
    
    def polynominalFunc(self):
        global y
        y=df1.interpolate(method="polynominal")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)
    
    def kroghFunc(self):
        global y
        y=df1.interpolate(method="krogh")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)
    
    def piecewisePolynominalFunc(self):
        global y
        y=df1.interpolate(method="piecewise_polynomial")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)

    def pchipFunc(self):
        global y
        y=df1.interpolate(method="pchip")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)

    def akimaFunc(self):
        global y
        y=df1.interpolate(method="akima")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)

    def cubicsplineFunc(self):
        global y
        y=df1.interpolate(method="cubicspline")
        model = pandasModel(y)
        view = QTableView()
        view.setModel(model)
        self.tableView2.setModel(model)
    

    def showGraphFunc(self):
        df1.set_index('Index').plot()
        plt.show()

    def showGraphFunc2(self):
        y.set_index('Index').plot()
        plt.show()

    def tableReset(self):
        self.tableView.setModel(None)
    
    def tableReset2(self):
        self.tableView2.setModel(None)


 

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = MainWindow()
    app.exec_()
