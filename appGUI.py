# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import pyqtgraph as pg
pg.setConfigOption("background",pg.mkColor(242, 243, 245))
pg.setConfigOption("foreground",'k')

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt

matplotlib.use('QT5Agg')

class MatplotlibCanvas(FigureCanvasQTAgg):
	def __init__(self,parent=None, dpi = 120):
		self.fig, self.axes = plt.subplots()
		super(MatplotlibCanvas,self).__init__(self.fig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1236, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.signalPlotterControlsAndViewLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.signalPlotterControlsAndViewLayout.setContentsMargins(0, 0, 0, 0)
        self.signalPlotterControlsAndViewLayout.setObjectName("signalPlotterControlsAndViewLayout")
        self.topLeftSideLayout = QtWidgets.QHBoxLayout()
        self.topLeftSideLayout.setObjectName("topLeftSideLayout")
        self.YAxesSliderLayout = QtWidgets.QHBoxLayout()
        self.YAxesSliderLayout.setObjectName("YAxesSliderLayout")
        self.YAxesSliderLabelLayout = QtWidgets.QVBoxLayout()
        self.YAxesSliderLabelLayout.setObjectName("YAxesSliderLabelLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.YAxesSliderLabelLayout.addItem(spacerItem)
        self.YAxesLabel = QtWidgets.QLabel(self.layoutWidget)
        self.YAxesLabel.setMaximumSize(QtCore.QSize(16, 80))
        self.YAxesLabel.setText("")
        self.YAxesLabel.setPixmap(QtGui.QPixmap(".\\ySlider.png"))
        self.YAxesLabel.setScaledContents(True)
        self.YAxesLabel.setObjectName("YAxesLabel")
        self.YAxesSliderLabelLayout.addWidget(self.YAxesLabel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.YAxesSliderLabelLayout.addItem(spacerItem1)
        self.YAxesSliderLayout.addLayout(self.YAxesSliderLabelLayout)
        self.YAxesSlider = QtWidgets.QSlider(self.layoutWidget)
        self.YAxesSlider.setOrientation(QtCore.Qt.Vertical)
        self.YAxesSlider.setObjectName("YAxesSlider")
        self.YAxesSliderLayout.addWidget(self.YAxesSlider)
        self.topLeftSideLayout.addLayout(self.YAxesSliderLayout)
        self.signalPlotter = PlotWidget(self.layoutWidget)
        self.signalPlotter.setObjectName("signalPlotter")
        self.topLeftSideLayout.addWidget(self.signalPlotter)
        self.signalPlotterControlsAndViewLayout.addLayout(self.topLeftSideLayout)
        self.bottomLeftSideLayout = QtWidgets.QHBoxLayout()
        self.bottomLeftSideLayout.setObjectName("bottomLeftSideLayout")
        self.emptySpace = QtWidgets.QLabel(self.layoutWidget)
        self.emptySpace.setMinimumSize(QtCore.QSize(16, 0))
        self.emptySpace.setMaximumSize(QtCore.QSize(16, 1600))
        self.emptySpace.setText("")
        self.emptySpace.setObjectName("emptySpace")
        self.bottomLeftSideLayout.addWidget(self.emptySpace)
        self.bottomLeftSide_withoutSpaceLayout = QtWidgets.QVBoxLayout()
        self.bottomLeftSide_withoutSpaceLayout.setObjectName("bottomLeftSide_withoutSpaceLayout")
        self.XAxesSlider = QtWidgets.QSlider(self.layoutWidget)
        self.XAxesSlider.setOrientation(QtCore.Qt.Horizontal)
        self.XAxesSlider.setObjectName("XAxesSlider")
        self.bottomLeftSide_withoutSpaceLayout.addWidget(self.XAxesSlider)
        self.XAxesSliderLayout = QtWidgets.QVBoxLayout()
        self.XAxesSliderLayout.setObjectName("XAxesSliderLayout")
        self.XAxesSliderLabelLayout = QtWidgets.QHBoxLayout()
        self.XAxesSliderLabelLayout.setObjectName("XAxesSliderLabelLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.XAxesSliderLabelLayout.addItem(spacerItem2)
        self.XAxesLabel = QtWidgets.QLabel(self.layoutWidget)
        self.XAxesLabel.setMaximumSize(QtCore.QSize(80, 16))
        self.XAxesLabel.setText("")
        self.XAxesLabel.setPixmap(QtGui.QPixmap(".\\xSlider.png"))
        self.XAxesLabel.setScaledContents(True)
        self.XAxesLabel.setObjectName("XAxesLabel")
        self.XAxesSliderLabelLayout.addWidget(self.XAxesLabel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.XAxesSliderLabelLayout.addItem(spacerItem3)
        self.XAxesSliderLayout.addLayout(self.XAxesSliderLabelLayout)
        self.bottomLeftSide_withoutSpaceLayout.addLayout(self.XAxesSliderLayout)
        self.bottomLeftSideLayout.addLayout(self.bottomLeftSide_withoutSpaceLayout)
        self.signalPlotterControlsAndViewLayout.addLayout(self.bottomLeftSideLayout)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.allSpectogramControlsAndViewLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.allSpectogramControlsAndViewLayout.setContentsMargins(0, 0, 0, 0)
        self.allSpectogramControlsAndViewLayout.setObjectName("allSpectogramControlsAndViewLayout")
        self.topRightSideLayout = QtWidgets.QHBoxLayout()
        self.topRightSideLayout.setObjectName("topRightSideLayout")
        self.spectogramLayout = QtWidgets.QHBoxLayout()
        self.spectogramLayout.setObjectName("spectogramLayout")
        self.topRightSideLayout.addLayout(self.spectogramLayout)
        self.intensityRangeSlider = QRangeSlider(self.layoutWidget1)
        self.intensityRangeSlider.setOrientation(QtCore.Qt.Vertical)
        self.intensityRangeSlider.setObjectName("intensityRangeSlider")
        self.topRightSideLayout.addWidget(self.intensityRangeSlider)
        self.allSpectogramControlsAndViewLayout.addLayout(self.topRightSideLayout)
        self.bottomRightSideLayout = QtWidgets.QHBoxLayout()
        self.bottomRightSideLayout.setObjectName("bottomRightSideLayout")
        self.selectChannelLayout = QtWidgets.QVBoxLayout()
        self.selectChannelLayout.setObjectName("selectChannelLayout")
        self.selectChannelLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.selectChannelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.selectChannelLabel.setObjectName("selectChannelLabel")
        self.selectChannelLayout.addWidget(self.selectChannelLabel)
        self.channelComboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.channelComboBox.setObjectName("channelComboBox")
        self.channelComboBox.addItem("")
        self.channelComboBox.addItem("")
        self.channelComboBox.addItem("")
        self.selectChannelLayout.addWidget(self.channelComboBox)
        self.bottomRightSideLayout.addLayout(self.selectChannelLayout)
        self.selectColorLayout = QtWidgets.QVBoxLayout()
        self.selectColorLayout.setObjectName("selectColorLayout")
        self.colorPaletteLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.colorPaletteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.colorPaletteLabel.setObjectName("colorPaletteLabel")
        self.selectColorLayout.addWidget(self.colorPaletteLabel)
        self.colorPaletteComboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.colorPaletteComboBox.setObjectName("colorPaletteComboBox")
        self.colorPaletteComboBox.addItem("")
        self.colorPaletteComboBox.addItem("")
        self.colorPaletteComboBox.addItem("")
        self.colorPaletteComboBox.addItem("")
        self.colorPaletteComboBox.addItem("")
        self.selectColorLayout.addWidget(self.colorPaletteComboBox)
        self.bottomRightSideLayout.addLayout(self.selectColorLayout)
        self.allSpectogramControlsAndViewLayout.addLayout(self.bottomRightSideLayout)
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1236, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSignal = QtWidgets.QMenu(self.menubar)
        self.menuSignal.setObjectName("menuSignal")
        self.menuColor = QtWidgets.QMenu(self.menubar)
        self.menuColor.setObjectName("menuColor")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen_csv_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_csv_file.setObjectName("actionOpen_csv_file")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionPrint_to_PDF = QtWidgets.QAction(MainWindow)
        self.actionPrint_to_PDF.setObjectName("actionPrint_to_PDF")
        self.actionChannel_1 = QtWidgets.QAction(MainWindow)
        self.actionChannel_1.setCheckable(True)
        self.actionChannel_1.setObjectName("actionChannel_1")
        self.actionChannel_2 = QtWidgets.QAction(MainWindow)
        self.actionChannel_2.setCheckable(True)
        self.actionChannel_2.setObjectName("actionChannel_2")
        self.actionChannel_3 = QtWidgets.QAction(MainWindow)
        self.actionChannel_3.setCheckable(True)
        self.actionChannel_3.setObjectName("actionChannel_3")
        self.actionRed = QtWidgets.QAction(MainWindow)
        self.actionRed.setCheckable(True)
        self.actionRed.setObjectName("actionRed")
        self.actionGreen = QtWidgets.QAction(MainWindow)
        self.actionGreen.setCheckable(True)
        self.actionGreen.setObjectName("actionGreen")
        self.actionBlue = QtWidgets.QAction(MainWindow)
        self.actionBlue.setCheckable(True)
        self.actionBlue.setObjectName("actionBlue")
        self.actionPause = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPause.setIcon(icon)
        self.actionPause.setObjectName("actionPause")
        self.actionPlay = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlay.setIcon(icon1)
        self.actionPlay.setObjectName("actionPlay")
        self.actionZoom_in = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\icons/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_in.setIcon(icon2)
        self.actionZoom_in.setObjectName("actionZoom_in")
        self.actionZoom_out = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\icons/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_out.setIcon(icon3)
        self.actionZoom_out.setObjectName("actionZoom_out")
        self.actionSpeed_up = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpeed_up.setIcon(icon4)
        self.actionSpeed_up.setObjectName("actionSpeed_up")
        self.actionSpeed_down = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\icons/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpeed_down.setIcon(icon5)
        self.actionSpeed_down.setObjectName("actionSpeed_down")
        self.menuFile.addAction(self.actionOpen_csv_file)
        self.menuFile.addAction(self.actionPrint_to_PDF)
        self.menuSignal.addAction(self.actionChannel_1)
        self.menuSignal.addAction(self.actionChannel_2)
        self.menuSignal.addAction(self.actionChannel_3)
        self.menuColor.addAction(self.actionRed)
        self.menuColor.addAction(self.actionGreen)
        self.menuColor.addAction(self.actionBlue)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSignal.menuAction())
        self.menubar.addAction(self.menuColor.menuAction())
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addAction(self.actionPlay)
        self.toolBar.addAction(self.actionZoom_in)
        self.toolBar.addAction(self.actionZoom_out)
        self.toolBar.addAction(self.actionSpeed_up)
        self.toolBar.addAction(self.actionSpeed_down)

        self.spectogramCanv = MatplotlibCanvas(self)
        self.spectogramCanv.fig.set_facecolor((242/255,243/255,245/255))
        self.spectogramCanv.axes.set_facecolor((242/255,243/255,245/255))
        self.spectogramLayout.addWidget(self.spectogramCanv)
        
        
        self.splitter.setSizes([814,400])

        divider = make_axes_locatable(self.spectogramCanv.axes)
        self.colorBarAxes = divider.append_axes('right', size='5%', pad=0.05)
        self.colorBarAxes.set_facecolor((242/255,243/255,245/255))
        self.intensityRangeSlider.setValue([0,99])
        self.XAxesSlider.setValue(99)
        self.YAxesSlider.setValue(50)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectChannelLabel.setText(_translate("MainWindow", "Select Channel"))
        self.channelComboBox.setItemText(0, _translate("MainWindow", "Channel 1"))
        self.channelComboBox.setItemText(1, _translate("MainWindow", "Channel 2"))
        self.channelComboBox.setItemText(2, _translate("MainWindow", "Channel 3"))
        self.colorPaletteLabel.setText(_translate("MainWindow", "Select Color Palette"))
        self.colorPaletteComboBox.setItemText(0, _translate("MainWindow", "Viridis"))
        self.colorPaletteComboBox.setItemText(1, _translate("MainWindow", "Plasma"))
        self.colorPaletteComboBox.setItemText(2, _translate("MainWindow", "Inferno"))
        self.colorPaletteComboBox.setItemText(3, _translate("MainWindow", "Magma"))
        self.colorPaletteComboBox.setItemText(4, _translate("MainWindow", "Cividis"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSignal.setTitle(_translate("MainWindow", "Signal"))
        self.menuColor.setTitle(_translate("MainWindow", "Color"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen_csv_file.setText(_translate("MainWindow", "Open CSV File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionPrint_to_PDF.setText(_translate("MainWindow", "Print to PDF"))
        self.actionChannel_1.setText(_translate("MainWindow", "Channel 1"))
        self.actionChannel_2.setText(_translate("MainWindow", "Channel 2"))
        self.actionChannel_3.setText(_translate("MainWindow", "Channel 3"))
        self.actionRed.setText(_translate("MainWindow", "Red"))
        self.actionGreen.setText(_translate("MainWindow", "Green"))
        self.actionBlue.setText(_translate("MainWindow", "Blue"))
        self.actionPause.setText(_translate("MainWindow", "Pause"))
        self.actionPlay.setText(_translate("MainWindow", "play"))
        self.actionZoom_in.setText(_translate("MainWindow", "zoom in"))
        self.actionZoom_out.setText(_translate("MainWindow", "zoom out"))
        self.actionSpeed_up.setText(_translate("MainWindow", "speed up"))
        self.actionSpeed_down.setText(_translate("MainWindow", "speed down"))
from pyqtgraph import PlotWidget
from qtrangeslider import QRangeSlider


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
