import sys

from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from copy import deepcopy
from typing import List, Dict, Tuple
from copy import deepcopy
import matplotlib.pyplot as plt
import math

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Start(object):
    def setupUi(self, Start):
        Start.setObjectName("Start")
        Start.setEnabled(True)
        Start.resize(1455, 829)
        font = QtGui.QFont()
        font.setPointSize(12)
        Start.setFont(font)
        Start.setAutoFillBackground(False)
        Start.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.run = QtWidgets.QPushButton(Start)
        self.run.setGeometry(QtCore.QRect(160, 790, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.run.setFont(font)
        self.run.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.run.setObjectName("run")
        self.layoutWidget = QtWidgets.QWidget(Start)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 26, 511, 751))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lexp = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lexp.setFont(font)
        self.lexp.setSingleStep(0.2)
        self.lexp.setProperty("value", 1.0)
        self.lexp.setObjectName("lexp")
        self.gridLayout.addWidget(self.lexp, 14, 2, 1, 1)
        self.rely = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rely.setFont(font)
        self.rely.setSingleStep(0.2)
        self.rely.setProperty("value", 1.0)
        self.rely.setObjectName("rely")
        self.gridLayout.addWidget(self.rely, 1, 2, 1, 1)
        self.modp = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modp.setFont(font)
        self.modp.setSingleStep(0.2)
        self.modp.setProperty("value", 1.0)
        self.modp.setObjectName("modp")
        self.gridLayout.addWidget(self.modp, 16, 2, 1, 1)
        self.tool = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tool.setFont(font)
        self.tool.setSingleStep(0.2)
        self.tool.setProperty("value", 1.0)
        self.tool.setObjectName("tool")
        self.gridLayout.addWidget(self.tool, 17, 2, 1, 1)
        self.time = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.time.setFont(font)
        self.time.setSingleStep(0.2)
        self.time.setProperty("value", 1.0)
        self.time.setObjectName("time")
        self.gridLayout.addWidget(self.time, 5, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 12, 0, 1, 1)
        self.turn = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.turn.setFont(font)
        self.turn.setSingleStep(0.2)
        self.turn.setProperty("value", 1.0)
        self.turn.setObjectName("turn")
        self.gridLayout.addWidget(self.turn, 8, 2, 1, 1)
        self.salary = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.salary.setFont(font)
        self.salary.setMaximum(1000000)
        self.salary.setSingleStep(1000)
        self.salary.setProperty("value", 60000)
        self.salary.setObjectName("salary")
        self.gridLayout.addWidget(self.salary, 25, 1, 1, 2)
        self.pcap = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pcap.setFont(font)
        self.pcap.setSingleStep(0.2)
        self.pcap.setProperty("value", 1.0)
        self.pcap.setObjectName("pcap")
        self.gridLayout.addWidget(self.pcap, 12, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 17, 0, 1, 2)
        self.sced = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sced.setFont(font)
        self.sced.setSingleStep(0.2)
        self.sced.setProperty("value", 1.0)
        self.sced.setObjectName("sced")
        self.gridLayout.addWidget(self.sced, 18, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.radio_usual = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radio_usual.setFont(font)
        self.radio_usual.setObjectName("radio_usual")
        self.gridLayout.addWidget(self.radio_usual, 20, 0, 1, 1)
        self.acap = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acap.setFont(font)
        self.acap.setSingleStep(0.2)
        self.acap.setProperty("value", 0.86)
        self.acap.setObjectName("acap")
        self.gridLayout.addWidget(self.acap, 10, 2, 1, 1)
        self.data = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.data.setFont(font)
        self.data.setSingleStep(0.2)
        self.data.setProperty("value", 1.08)
        self.data.setObjectName("data")
        self.gridLayout.addWidget(self.data, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.radio_buildin = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radio_buildin.setFont(font)
        self.radio_buildin.setObjectName("radio_buildin")
        self.gridLayout.addWidget(self.radio_buildin, 22, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 15, 0, 1, 3)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 24, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 11, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.aexp = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aexp.setFont(font)
        self.aexp.setSingleStep(0.2)
        self.aexp.setProperty("value", 1.0)
        self.aexp.setObjectName("aexp")
        self.gridLayout.addWidget(self.aexp, 11, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 14, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 16, 0, 1, 2)
        self.cplx = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cplx.setFont(font)
        self.cplx.setSingleStep(0.2)
        self.cplx.setProperty("value", 1.0)
        self.cplx.setObjectName("cplx")
        self.gridLayout.addWidget(self.cplx, 3, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 3)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 9, 0, 1, 3)
        self.virt = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.virt.setFont(font)
        self.virt.setSingleStep(0.2)
        self.virt.setProperty("value", 1.0)
        self.virt.setObjectName("virt")
        self.gridLayout.addWidget(self.virt, 7, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 13, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 23, 0, 1, 3)
        self.vexp = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vexp.setFont(font)
        self.vexp.setSingleStep(0.2)
        self.vexp.setProperty("value", 1.0)
        self.vexp.setObjectName("vexp")
        self.gridLayout.addWidget(self.vexp, 13, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 4, 0, 1, 3)
        self.radio_inter = QtWidgets.QRadioButton(self.layoutWidget)
        self.radio_inter.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radio_inter.setFont(font)
        self.radio_inter.setChecked(True)
        self.radio_inter.setObjectName("radio_inter")
        self.gridLayout.addWidget(self.radio_inter, 21, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 19, 0, 1, 3)
        self.stor = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stor.setFont(font)
        self.stor.setSingleStep(0.2)
        self.stor.setProperty("value", 1.0)
        self.stor.setObjectName("stor")
        self.gridLayout.addWidget(self.stor, 6, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 10, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 25, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 18, 0, 1, 1)
        self.code = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.code.setFont(font)
        self.code.setSingleStep(0.2)
        self.code.setProperty("value", 55.0)
        self.code.setObjectName("code")
        self.gridLayout.addWidget(self.code, 24, 1, 1, 2)
        self.tableWorkTime = QtWidgets.QTableWidget(Start)
        self.tableWorkTime.setGeometry(QtCore.QRect(550, 40, 444, 90))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWorkTime.setFont(font)
        self.tableWorkTime.setObjectName("tableWorkTime")
        self.tableWorkTime.setColumnCount(2)
        self.tableWorkTime.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWorkTime.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWorkTime.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWorkTime.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWorkTime.setHorizontalHeaderItem(1, item)
        self.tableWorkTime.horizontalHeader().setDefaultSectionSize(140)
        self.tableWorkTime.verticalHeader().setDefaultSectionSize(30)
        self.tableWorkTime.verticalHeader().setMinimumSectionSize(23)
        self.label_23 = QtWidgets.QLabel(Start)
        self.label_23.setGeometry(QtCore.QRect(550, 20, 851, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Start)
        self.label_24.setGeometry(QtCore.QRect(550, 140, 851, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.tableLife = QtWidgets.QTableWidget(Start)
        self.tableLife.setGeometry(QtCore.QRect(550, 160, 853, 180))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableLife.setFont(font)
        self.tableLife.setObjectName("tableLife")
        self.tableLife.setColumnCount(3)
        self.tableLife.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableLife.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableLife.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableLife.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableLife.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableLife.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableLife.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableLife.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableLife.setHorizontalHeaderItem(2, item)
        self.tableLife.horizontalHeader().setDefaultSectionSize(140)
        self.tableLife.verticalHeader().setDefaultSectionSize(30)
        self.tableLife.verticalHeader().setMinimumSectionSize(23)
        self.label_25 = QtWidgets.QLabel(Start)
        self.label_25.setGeometry(QtCore.QRect(550, 350, 851, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.tableCOCOMO = QtWidgets.QTableWidget(Start)
        self.tableCOCOMO.setGeometry(QtCore.QRect(550, 370, 852, 272))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableCOCOMO.setFont(font)
        self.tableCOCOMO.setObjectName("tableCOCOMO")
        self.tableCOCOMO.setColumnCount(2)
        self.tableCOCOMO.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCOCOMO.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCOCOMO.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCOCOMO.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCOCOMO.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCOCOMO.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCOCOMO.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCOCOMO.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCOCOMO.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCOCOMO.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCOCOMO.setHorizontalHeaderItem(1, item)
        self.tableCOCOMO.horizontalHeader().setDefaultSectionSize(197)
        self.tableCOCOMO.verticalHeader().setDefaultSectionSize(30)
        self.tableCOCOMO.verticalHeader().setMinimumSectionSize(23)
        self.label_27 = QtWidgets.QLabel(Start)
        self.label_27.setGeometry(QtCore.QRect(1010, 40, 81, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.budget = QtWidgets.QLineEdit(Start)
        self.budget.setGeometry(QtCore.QRect(1090, 40, 311, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.budget.setFont(font)
        self.budget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.budget.setObjectName("budget")

        self.retranslateUi(Start)
        QtCore.QMetaObject.connectSlotsByName(Start)

    def retranslateUi(self, Start):
        _translate = QtCore.QCoreApplication.translate
        Start.setWindowTitle(_translate("Start", "COCOMO"))
        self.run.setText(_translate("Start", "ГОТОВО"))
        self.label_10.setText(_translate("Start", "PCAP (Способности программиста)"))
        self.label_5.setText(_translate("Start", "STOR (Ограничение объёма основной памяти)"))
        self.label_11.setText(_translate("Start", "TOOL (Использование программных инструментов)"))
        self.label_2.setText(_translate("Start", "DATA (Размер БД)"))
        self.radio_usual.setText(_translate("Start", "Обычный"))
        self.label_4.setText(_translate("Start", "TIME (Ограничение времени выполнения)"))
        self.radio_buildin.setText(_translate("Start", "Встроенный"))
        self.label_19.setText(_translate("Start", "Атрибуты проекта"))
        self.label_22.setText(_translate("Start", "Количество строк кода (KLOC)"))
        self.label_3.setText(_translate("Start", "CPLX (Сложность продукта)"))
        self.label_9.setText(_translate("Start", "AEXP (Знание приложений)"))
        self.label_6.setText(_translate("Start", "VIRT (Изменчивость виртуальной машины)"))
        self.label_7.setText(_translate("Start", "TURN (Время реакции компьютера)"))
        self.label_16.setText(_translate("Start", "LEXP (Знание ЯП)"))
        self.label_14.setText(_translate("Start", "MODP (Использование современных методов)"))
        self.label_15.setText(_translate("Start", "Атрибуты программного продукта"))
        self.label_18.setText(_translate("Start", "Атрибуты персонала"))
        self.label_12.setText(_translate("Start", "VEXP (Знание виртуальной машины)"))
        self.label_21.setText(_translate("Start", "Иное"))
        self.label_17.setText(_translate("Start", "Атрибуты компьютера"))
        self.radio_inter.setText(_translate("Start", "Промежуточный"))
        self.label_20.setText(_translate("Start", "Режим"))
        self.label_8.setText(_translate("Start", "ACAP (Способности аналитика)"))
        self.label_26.setText(_translate("Start", "Средняя зарплата"))
        self.label.setText(_translate("Start", "RELY (Требуемая надежность)"))
        self.label_13.setText(_translate("Start", "SCED (Требуемые сроки разработки)"))
        item = self.tableWorkTime.verticalHeaderItem(0)
        item.setText(_translate("Start", "Без планирования"))
        item = self.tableWorkTime.verticalHeaderItem(1)
        item.setText(_translate("Start", "С планированием"))
        item = self.tableWorkTime.horizontalHeaderItem(0)
        item.setText(_translate("Start", "Трудозатраты"))
        item = self.tableWorkTime.horizontalHeaderItem(1)
        item.setText(_translate("Start", "Время"))
        self.label_23.setText(_translate("Start", "Результаты"))
        self.label_24.setText(_translate("Start", "Распределение работ и времени по стадиям жизненного цикла"))
        item = self.tableLife.verticalHeaderItem(0)
        item.setText(_translate("Start", "Планирование и определение требований"))
        item = self.tableLife.verticalHeaderItem(1)
        item.setText(_translate("Start", "Проектирование продукта"))
        item = self.tableLife.verticalHeaderItem(2)
        item.setText(_translate("Start", "Детальное проектирование"))
        item = self.tableLife.verticalHeaderItem(3)
        item.setText(_translate("Start", "Кодирование и тестирование отдельных модулей"))
        item = self.tableLife.verticalHeaderItem(4)
        item.setText(_translate("Start", "Интеграция и тестирование"))
        item = self.tableLife.horizontalHeaderItem(0)
        item.setText(_translate("Start", "Трудозатраты"))
        item = self.tableLife.horizontalHeaderItem(1)
        item.setText(_translate("Start", "Время "))
        item = self.tableLife.horizontalHeaderItem(2)
        item.setText(_translate("Start", "Сотрудники"))
        self.label_25.setText(_translate("Start", "Стандартное распределение работ по видам деятельности WBS в модели COCOMO"))
        item = self.tableCOCOMO.verticalHeaderItem(0)
        item.setText(_translate("Start", "Анализ требований"))
        item = self.tableCOCOMO.verticalHeaderItem(1)
        item.setText(_translate("Start", "Проектирование продукта"))
        item = self.tableCOCOMO.verticalHeaderItem(2)
        item.setText(_translate("Start", "Программирование"))
        item = self.tableCOCOMO.verticalHeaderItem(3)
        item.setText(_translate("Start", "Планирование тестирования"))
        item = self.tableCOCOMO.verticalHeaderItem(4)
        item.setText(_translate("Start", "Верификация и аттестация"))
        item = self.tableCOCOMO.verticalHeaderItem(5)
        item.setText(_translate("Start", "Канцелярия проекта"))
        item = self.tableCOCOMO.verticalHeaderItem(6)
        item.setText(_translate("Start", "Управление конфигурацией и обеспечение качества"))
        item = self.tableCOCOMO.verticalHeaderItem(7)
        item.setText(_translate("Start", "Создание руководств"))
        item = self.tableCOCOMO.horizontalHeaderItem(0)
        item.setText(_translate("Start", "Бюджет (%)"))
        item = self.tableCOCOMO.horizontalHeaderItem(1)
        item.setText(_translate("Start", "Трудозатраты"))
        self.label_27.setText(_translate("Start", "Бюджет"))


class TaskWindow(QMainWindow):
    def __init__(self):
        super(TaskWindow, self).__init__()
        self.ui = Ui_Start()
        self.ui.setupUi(self)

        self.ui.run.clicked.connect(self.run)

    def run(self):
        params = deepcopy(DEFAULT)
        params['RELY'] = float(self.ui.rely.text().replace(',', '.'))
        params['DATA'] = float(self.ui.data.text().replace(',', '.'))
        params['CPLX'] = float(self.ui.cplx.text().replace(',', '.'))
        params['TIME'] = float(self.ui.time.text().replace(',', '.'))
        params['STOR'] = float(self.ui.stor.text().replace(',', '.'))
        params['VIRT'] = float(self.ui.virt.text().replace(',', '.'))
        params['TURN'] = float(self.ui.turn.text().replace(',', '.'))
        params['ACAP'] = float(self.ui.acap.text().replace(',', '.'))
        params['AEXP'] = float(self.ui.aexp.text().replace(',', '.'))
        params['PCAP'] = float(self.ui.pcap.text().replace(',', '.'))
        params['VEXP'] = float(self.ui.vexp.text().replace(',', '.'))
        params['LEXP'] = float(self.ui.lexp.text().replace(',', '.'))
        params['MODP'] = float(self.ui.modp.text().replace(',', '.'))
        params['TOOL'] = float(self.ui.tool.text().replace(',', '.'))
        params['SCED'] = float(self.ui.sced.text().replace(',', '.'))

        size = float(self.ui.code.text().replace(',', '.'))
        salary = int(self.ui.salary.text())
        variant = NORMAL
        if self.ui.radio_inter.isChecked():
            variant = INTER
        elif self.ui.radio_buildin.isChecked():
            variant = BUILDIN

        res = runExperiment(params, variant, size, salary)

        self.ui.tableWorkTime.setItem(0, 0, QTableWidgetItem(str('{:.3f}'.format(res['laborCosts']))))
        self.ui.tableWorkTime.setItem(0, 1, QTableWidgetItem(str('{:.3f}'.format(res['time']))))
        self.ui.tableWorkTime.setItem(1, 0, QTableWidgetItem(str('{:.3f}'.format(res['planWork']))))
        self.ui.tableWorkTime.setItem(1, 1, QTableWidgetItem(str('{:.3f}'.format(res['planTime']))))

        self.ui.tableLife.setItem(0, 0, QTableWidgetItem(str('{:.3f}'.format(res['planWorkSingle']))))
        self.ui.tableLife.setItem(0, 1, QTableWidgetItem(str('{:.3f}'.format(res['planTimeSingle']))))
        self.ui.tableLife.setItem(0, 2, QTableWidgetItem(str(res['planPeople'])))

        self.ui.tableLife.setItem(1, 0, QTableWidgetItem(str('{:.3f}'.format(res['designWork']))))
        self.ui.tableLife.setItem(1, 1, QTableWidgetItem(str('{:.3f}'.format(res['designTime']))))
        self.ui.tableLife.setItem(1, 2, QTableWidgetItem(str(res['designPeople'])))

        self.ui.tableLife.setItem(2, 0, QTableWidgetItem(str('{:.3f}'.format(res['detailWork']))))
        self.ui.tableLife.setItem(2, 1, QTableWidgetItem(str('{:.3f}'.format(res['detailTime']))))
        self.ui.tableLife.setItem(2, 2, QTableWidgetItem(str(res['detailPeople'])))

        self.ui.tableLife.setItem(3, 0, QTableWidgetItem(str('{:.3f}'.format(res['codingWork']))))
        self.ui.tableLife.setItem(3, 1, QTableWidgetItem(str('{:.3f}'.format(res['codingTime']))))
        self.ui.tableLife.setItem(3, 2, QTableWidgetItem(str(res['codingPeople'])))

        self.ui.tableLife.setItem(4, 0, QTableWidgetItem(str('{:.3f}'.format(res['integWork']))))
        self.ui.tableLife.setItem(4, 1, QTableWidgetItem(str('{:.3f}'.format(res['integTime']))))
        self.ui.tableLife.setItem(4, 2, QTableWidgetItem(str(res['integPeople'])))

        self.ui.tableCOCOMO.setItem(0, 0, QTableWidgetItem(str(res['analysis'])))
        self.ui.tableCOCOMO.setItem(0, 1, QTableWidgetItem(str('{:.3f}'.format(res['anPeople']))))

        self.ui.tableCOCOMO.setItem(1, 0, QTableWidgetItem(str(res['design'])))
        self.ui.tableCOCOMO.setItem(1, 1, QTableWidgetItem(str('{:.3f}'.format(res['dePeople']))))

        self.ui.tableCOCOMO.setItem(2, 0, QTableWidgetItem(str(res['coding'])))
        self.ui.tableCOCOMO.setItem(2, 1, QTableWidgetItem(str('{:.3f}'.format(res['coPeople']))))

        self.ui.tableCOCOMO.setItem(3, 0, QTableWidgetItem(str(res['planning'])))
        self.ui.tableCOCOMO.setItem(3, 1, QTableWidgetItem(str('{:.3f}'.format(res['plPeople']))))

        self.ui.tableCOCOMO.setItem(4, 0, QTableWidgetItem(str(res['ver'])))
        self.ui.tableCOCOMO.setItem(4, 1, QTableWidgetItem(str('{:.3f}'.format(res['verPeople']))))

        self.ui.tableCOCOMO.setItem(5, 0, QTableWidgetItem(str(res['office'])))
        self.ui.tableCOCOMO.setItem(5, 1, QTableWidgetItem(str('{:.3f}'.format(res['ofPeople']))))

        self.ui.tableCOCOMO.setItem(6, 0, QTableWidgetItem(str(res['quality'])))
        self.ui.tableCOCOMO.setItem(6, 1, QTableWidgetItem(str('{:.3f}'.format(res['quPeople']))))

        self.ui.tableCOCOMO.setItem(7, 0, QTableWidgetItem(str(res['manuals'])))
        self.ui.tableCOCOMO.setItem(7, 1, QTableWidgetItem(str('{:.3f}'.format(res['maPeople']))))

        self.ui.budget.setText(str('{:.3f}'.format(res['budget'])))




NUM_LEVELS = 5
SIZE = 100
xArr = ['низкий уровень', 'номинальный уровень', 'высокий уровень']

# Типы проектов
NORMAL = {'c1': 3.2, 'p1': 1.05, 'c2': 2.5, 'p2': 0.38}  # Обычный вариант - некрупный проект, нет нововведений, всё знакомо
INTER = {'c1': 3.0, 'p1': 1.12, 'c2': 2.5, 'p2': 0.35}  # Промежуточный вариант - средний проект, есть инновации
BUILDIN = {'c1': 2.8, 'p1': 1.2, 'c2': 2.5, 'p2': 0.32}  # Встроенный вариант - крупный проект, значительный объем инноваций

# Атрибуты программного продукта
RELY = [0.75, 0.86, 1.0, 1.15, 1.4]  # Требуемая надежность
DATA = [None, 0.94, 1.0, 1.08, 1.16]  # Размер БД
CPLX = [0.7, 0.85, 1.0, 1.15, 1.3]  # Сложность продукта

# Атрибуты копьютера
TIME = [None, None, 1.0, 1.11, 1.5]  # Ограничение времени выполнения
STOR = [None, None, 1.0, 1.06, 1.21]  # Ограничение объёма основной памяти
VIRT = [None, 0.87, 1.0, 1.15, 1.30]  # Изменчивость виртуальной машины
TURN = [None, 0.87, 1.0, 1.07, 1.15]  # Время реакции компьютера

# Атрибуты персонала
ACAP = [1.46, 1.19, 1.0, 0.86, 0.71]  # Способности аналитика
AEXP = [1.29, 1.15, 1.0, 0.91, 0.82]  # Знание приложений
PCAP = [1.42, 1.17, 1.0, 0.86, 0.7]   # Способности программиста
VEXP = [1.21, 1.1, 1.0, 0.9, None]    # Знание виртуальной машины
LEXP = [1.14, 1.07, 1.0, 0.95, None]  # Знание ЯП

# Атрибуты проекта
MODP = [1.24, 1.1, 1.0, 0.91, 0.82]  # Использование современных методов
TOOL = [1.24, 1.1, 1.0, 0.91, 0.82]  # Использование программных инструментов
SCED = [1.23, 1.08, 1.0, 1.04, 1.1]  # Требуемые сроки разработки

DEFAULT = {
    'RELY': RELY[2],
    'DATA': DATA[2],
    'CPLX': CPLX[2],
    'TIME': TIME[2],
    'STOR': STOR[2],
    'VIRT': VIRT[2],
    'TURN': TURN[2],
    'ACAP': ACAP[2],
    'AEXP': AEXP[2],
    'PCAP': PCAP[2],
    'VEXP': VEXP[2],
    'LEXP': LEXP[2],
    'MODP': MODP[2],
    'TOOL': TOOL[2],
    'SCED': SCED[2],
}


def getEAF(params: Dict[str, float]) -> float:
    mult = 1
    for elem in params.values():
        mult *= elem

    return mult


def getLaborCosts(c1: float, eaf: float, size: float, p1: float) -> float:
    return c1 * eaf * size ** p1


def getTime(c2: float, laborCosts: float, p2:float) -> float:
    return c2 * laborCosts ** p2


def calculate(params: Dict[str, float], variant: Dict[str, float], size: float) -> Tuple[float, float]:
    eaf = getEAF(params)
    laborCosts = getLaborCosts(variant['c1'], eaf, size, variant['p1'])
    time = getTime(variant['c2'], laborCosts, variant['p2'])

    return laborCosts, time


def process(variant: Dict[str, float], key: str, value: float, size: int):
    params = deepcopy(DEFAULT)
    params[key] = value

    return calculate(params, variant, size)


def process_2(variant: Dict[str, float], size: int):
    params = deepcopy(DEFAULT)

    return calculate(params, variant, size)


def runExperiment(params: Dict[str, float], variant: Dict[str, float], size: float, salary: int):
    res = {}
    res['laborCosts'], res['time'] = calculate(params, variant, size)

    res['planWork'] = res['laborCosts'] * 1.08
    res['planTime'] = res['time'] * 1.36

    res['planWorkSingle'] = res['laborCosts'] * 0.08
    res['planTimeSingle'] = res['time'] * 0.36
    res['planPeople'] = math.ceil(res['planWorkSingle'] / res['planTimeSingle'])

    res['designWork'] = res['laborCosts'] * 0.18
    res['designTime'] = res['time'] * 0.36
    res['designPeople'] = math.ceil(res['designWork'] / res['designTime'])

    res['detailWork'] = res['laborCosts'] * 0.25
    res['detailTime'] = res['time'] * 0.18
    res['detailPeople'] = math.ceil(res['detailWork'] / res['detailTime'])

    res['codingWork'] = res['laborCosts'] * 0.26
    res['codingTime'] = res['time'] * 0.18
    res['codingPeople'] = math.ceil(res['codingWork'] / res['codingTime'])

    res['integWork'] = res['laborCosts'] * 0.31
    res['integTime'] = res['time'] * 0.28
    res['integPeople'] = math.ceil(res['integWork'] / res['integTime'])

    res['analysis'] = 4
    res['anPeople'] = res['laborCosts'] * 0.04

    res['design'] = 12
    res['dePeople'] = res['laborCosts'] * 0.12

    res['coding'] = 44
    res['coPeople'] = res['laborCosts'] * 0.44

    res['planning'] = 6
    res['plPeople'] = res['laborCosts'] * 0.06

    res['ver'] = 14
    res['verPeople'] = res['laborCosts'] * 0.14

    res['office'] = 7
    res['ofPeople'] = res['laborCosts'] * 0.07

    res['quality'] = 7
    res['quPeople'] = res['laborCosts'] * 0.07

    res['manuals'] = 6
    res['maPeople'] = res['laborCosts'] * 0.06

    res['budget'] = res['laborCosts'] * salary

    salary = {
        "Programmer": salary,
        "Analytic": salary * 1.4,
        "Manager": salary * 1.3,
        "Tester": salary * 0.65,
    }

    budget = []
    budget += [(((salary['Manager'] + salary['Analytic']) / 2) * res['designPeople'] * res['planTimeSingle'])]
    budget += [(((salary['Programmer'] + salary['Analytic']) / 2) * res['designPeople'] * res['designTime'])]
    budget += [(((salary['Programmer'] + salary['Analytic']) / 2) * res['detailPeople'] * res['detailTime'])]
    budget += [(((salary['Programmer'] + salary['Tester']) / 2) * res['codingPeople'] * res['codingTime'])]
    budget += [(((salary['Programmer'] + salary['Tester']) / 2) * res['integPeople'] * res['integTime'])]

    s = 0
    for i in range(len(budget)):
        s += budget[i]

    allTimeInfo = [res['planTimeSingle'], res['designTime'],
                   res['detailTime'], res['codingTime'],
                   res['integTime']]
    allPeopleInfo = [res['planPeople'], res['designPeople'],
                     res['detailPeople'], res['codingPeople'],
                     res['integPeople']]

    xData, yData = [], []

    s = 0
    for i in range(len(allTimeInfo)):
        time = s
        while time < s + allTimeInfo[i]:
            xData.append(time)
            yData.append(allPeopleInfo[i])
            time += 1
        s += allTimeInfo[i]

    plt.title('Сотрудники')
    plt.grid(True)
    plt.bar(xData, yData)
    plt.xlabel("Месяцы")
    plt.ylabel("Количество сотрудников")
    plt.show()

    return res


def draw(laborMODP, laborTOOL, laborSCED, timeMODP, timeTOOL, timeSCED):
    _, axs = plt.subplots(1, 2)
    colorArr = [['green', 'black', 'blue'], ['red', 'yellow', 'purple'], ['grey', 'orange', 'fuchsia']]
    typeArr = ['обычный тип проекта', 'промежуточный тип проекта', 'встроенный тип проекта']
    axs[0].set_title('Влияние MODP/TOOL/SCED на трудоёмкость (РМ)')
    axs[0].set(ylabel="PM, количество человеко-месяцев")
    axs[0].grid()

    axs[1].set_title("Влияние MODP/TOOL/SCED на время разработки (TМ)")
    axs[1].set(ylabel="PM, количество месяцев")
    axs[1].grid()

    for i in range(len(laborMODP)):
        axs[0].plot(xArr, laborMODP[i], label='MODP ' + typeArr[i], color=colorArr[i][0])
        axs[0].plot(xArr, laborTOOL[i], label='TOOL ' + typeArr[i], linestyle='--', color=colorArr[i][1], dashes=(2, 4))
        axs[0].plot(xArr, laborSCED[i], label='SCED ' + typeArr[i], linestyle=':', color=colorArr[i][2])

        axs[1].plot(xArr, timeMODP[i], label='MODP ' + typeArr[i], color=colorArr[i][0])
        axs[1].plot(xArr, timeTOOL[i], label='TOOL ' + typeArr[i], linestyle='--', color=colorArr[i][1], dashes=(2, 4))
        axs[1].plot(xArr, timeSCED[i], label='SCED ' + typeArr[i], linestyle=':', color=colorArr[i][2])

    axs[0].legend()
    axs[1].legend()
    plt.show()


def doTask1():
    laborMODP, laborTOOL, laborSCED = [], [], []
    timeMODP, timeTOOL, timeSCED = [], [], []

    for variant in [NORMAL, INTER, BUILDIN]:
        laborMODPArr, laborTOOLArr, laborSCEDArr = [], [], []
        timeMODPArr, timeTOOLArr, timeSCEDArr = [], [], []

        for level in range(1, NUM_LEVELS - 1):
            laborCosts, time = process(variant, 'MODP', MODP[level], SIZE)
            laborMODPArr.append(laborCosts)
            timeMODPArr.append(time)

            laborCosts, time = process(variant, 'TOOL', TOOL[level], SIZE)
            laborTOOLArr.append(laborCosts)
            timeTOOLArr.append(time)

            laborCosts, time = process(variant, 'SCED', SCED[level], SIZE)
            laborSCEDArr.append(laborCosts)
            timeSCEDArr.append(time)

        laborMODP.append(laborMODPArr)
        laborTOOL.append(laborTOOLArr)
        laborSCED.append(laborSCEDArr)

        timeMODP.append(timeMODPArr)
        timeTOOL.append(timeTOOLArr)
        timeSCED.append(timeSCEDArr)

    draw(laborMODP, laborTOOL, laborSCED, timeMODP, timeTOOL, timeSCED)



if __name__ == '__main__':
    app = QApplication([])
    application = TaskWindow()
    application.show()

    sys.exit(app.exec())