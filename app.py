# Required packages
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import pyqtgraph as pg
from pyqtgraph import *
import pyqtgraph.exporters
import numpy as np
import matplotlib
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
import pathlib
import sys
from matplotlib.backends.backend_pdf import PdfPages, PdfFile
import os
from reportlab.pdfgen import canvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from appGUI import Ui_MainWindow
from matplotlib.colors import ListedColormap

matplotlib.use('QT5Agg')




# self.spectogramCanv.axes.clear()
# self.colorBarAxes.clear()

# self.spectogramCanv.fig.tight_layout()
# self.spectogramCanv.draw()

class mainApp(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(mainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.xCoff = 5
        self.yCoff = 1.2

        self.channel_1_timer = QtCore.QTimer()
        self.channel_2_timer = QtCore.QTimer()
        self.channel_3_timer = QtCore.QTimer()

        self.allChannelsTimers = [
            self.channel_1_timer,
            self.channel_2_timer,
            self.channel_3_timer
        ]

        # color = (R,G,B) RGB : 0 -> 255
        self.redPen = pg.mkPen(color=(255, 0, 0)) # RED
        self.greenPen = pg.mkPen(color=(0, 255, 0)) # Green
        self.bluePen = pg.mkPen(color=(0, 0, 255)) # BLue

        self.pens = [
            self.redPen , 
            self.greenPen, 
            self.bluePen
        ]
        
        self.actionChannals = [self.ui.actionChannel_1, self.ui.actionChannel_2, self.ui.actionChannel_3]
        self.colors = [self.ui.actionRed, self.ui.actionGreen, self.ui.actionBlue]

        self.signalViewerLegend = self.ui.signalPlotter.addLegend(offset=(-30, 1))
        self.ui.signalPlotter.plotItem.setLimits(xMin=0, xMax=60, yMin=-0.6, yMax=0.6)
        self.ui.signalPlotter.plotItem.setLabel('left', 'Amplitude')
        self.ui.signalPlotter.plotItem.setLabel('bottom','Time')

        self.signalPlotters = [
            self.ui.signalPlotter.plot([], [], pen = self.pens[0]),
            self.ui.signalPlotter.plot([], [], pen = self.pens[1]),
            self.ui.signalPlotter.plot([], [], pen = self.pens[2])
        ]
        
        self.xAxesData = [None] * 3
        self.yAxesData = [None] * 3
        self.incRate = [0] * 3
        self.signalLastIndex = [0] * 3
        self.selectedColorTracker = [0,1,2] # -> 0 for RED 
        self.spectogramChannel = 0 
        self.fileName = [None] * 3
        self.select_signal(0)

        self.ui.actionOpen_csv_file.triggered.connect(lambda: self.load())
        self.ui.actionZoom_in.triggered.connect(lambda: self.zoomIn())
        self.ui.actionZoom_out.triggered.connect(lambda: self.zoomOut())
        self.ui.actionPause.triggered.connect(lambda: self.pause())
        self.ui.actionPlay.triggered.connect(lambda: self.play())
        self.ui.actionSpeed_up.triggered.connect(lambda: self.speedUp())
        self.ui.actionSpeed_down.triggered.connect(lambda: self.speedDown())
        self.ui.actionPrint_to_PDF.triggered.connect(lambda: self.saveAs())

        self.ui.actionChannel_1.triggered.connect(lambda: self.select_signal(0))
        self.ui.actionChannel_2.triggered.connect(lambda: self.select_signal(1))
        self.ui.actionChannel_3.triggered.connect(lambda: self.select_signal(2))

        self.ui.actionRed.triggered.connect(lambda: self.select_color(0))
        self.ui.actionGreen.triggered.connect(lambda: self.select_color(1))
        self.ui.actionBlue.triggered.connect(lambda: self.select_color(2))

        self.ui.channelComboBox.currentIndexChanged.connect(self.changeSpectogramChannel)
        self.ui.colorPaletteComboBox.currentIndexChanged['QString'].connect(self.drawSpectogram)
        
        self.ui.XAxesSlider.valueChanged.connect(lambda: self.moveInX())
        self.ui.YAxesSlider.valueChanged.connect(lambda: self.moveInY())
        self.ui.intensityRangeSlider.valueChanged.connect(lambda: self.changeSliderValue())


    def changeSliderValue(self):
        self.drawSpectogram(self.ui.colorPaletteComboBox.currentText())


    def read_file(self):

        path = QFileDialog.getOpenFileName(self, 'Open CSV File', '', 'CSV Files (*.csv)')[0]
        self.fileName[self.selectedChannel] = os.path.basename(path)
        
        self.ui.signalPlotter.plotItem.setTitle(self.fileName[self.selectedChannel])

        self.data = np.genfromtxt(path, delimiter=',')
        self.xAxesData[self.selectedChannel] = list(self.data[:, 0])
        self.yAxesData[self.selectedChannel] = list(self.data[:, 1])

        samplingRateOfSignal = np.ceil(1/(self.xAxesData[self.selectedChannel][1] - self.xAxesData[self.selectedChannel][0]))
        self.incRate[self.selectedChannel] = int(samplingRateOfSignal/10)

        self.drawSpectogram(self.ui.colorPaletteComboBox.currentText())



    def load(self):

        self.read_file()

        self.signalPlotters[self.selectedChannel].setData([],[])
        self.signalPlotters[self.selectedChannel].setPen(self.pens[self.selectedColor])
        self.updateLegend()
       

        self.signalLastIndex[self.selectedChannel] = 0
        self.allChannelsTimers[self.selectedChannel].setInterval(100)
        self.allChannelsTimers[self.selectedChannel].timeout.connect(lambda : self.updatePlot())
        self.allChannelsTimers[self.selectedChannel].start()


    # signalLastIndex is the Index

    def updateLegend(self):
        self.signalViewerLegend.clear()
        for IDX in range(3):
            if self.fileName[IDX] == None:
                continue
            self.signalViewerLegend.addItem(self.signalPlotters[IDX], self.fileName[IDX])


    def updatePlot(self):
        graphXAxesData = self.xAxesData[self.selectedChannel][:self.signalLastIndex[self.selectedChannel]]
        graphYAxesData = self.yAxesData[self.selectedChannel][:self.signalLastIndex[self.selectedChannel]]
        self.signalLastIndex[self.selectedChannel] += self.incRate[self.selectedChannel]
        
        self.ui.signalPlotter.plotItem.setLimits(xMin=0, xMax=max(max(graphXAxesData),5), yMin=-0.6, yMax=0.6)

        xMax = max(graphXAxesData, default=0)
        xMin = xMax-5

        # shrink range of x-axis
        self.ui.signalPlotter.plotItem.setXRange(xMin, xMax)
        
        # Plot the new data
        self.signalPlotters[self.selectedChannel].setData(graphXAxesData, graphYAxesData)

    def select_signal(self, channel):

        for signalLastIndex in range(3):
            self.actionChannals[signalLastIndex].setChecked(False)
        self.actionChannals[channel].setChecked(True)


        self.selectedChannel = channel

        self.ui.signalPlotter.plotItem.setTitle(self.fileName[channel])
        self.select_color(self.selectedColorTracker[channel])
        self.reset()


    def select_color(self, color):

        for signalLastIndex in range(3):
            self.colors[signalLastIndex].setChecked(False)
        self.colors[color].setChecked(True)

        self.selectedColorTracker[self.selectedChannel] = color
        self.selectedColor = color

        self.signalPlotters[self.selectedChannel].setPen(self.pens[self.selectedColor])

        
    def drawSpectogram(self, colorMap):

        self.clearSpectogram()
        
        if self.xAxesData[self.spectogramChannel] == None:
            return
        
        spectogramColorMap = colorMap.lower()
        vmax, vmin = self.ui.intensityRangeSlider.value()
        vmax, vmin = -vmax, -vmin
        self.ui.spectogramCanv.axes.specgram(self.yAxesData[self.spectogramChannel], cmap = spectogramColorMap, vmin = vmin, vmax = vmax)
        spectogramImage = self.ui.spectogramCanv.axes.images[0]
        self.ui.spectogramCanv.fig.colorbar(mappable = spectogramImage, cax = self.ui.colorBarAxes)
        self.ui.spectogramCanv.draw()

    def clearSpectogram(self):
        self.ui.spectogramCanv.axes.cla()
        self.ui.colorBarAxes.cla()
        self.ui.spectogramCanv.draw()



    def changeSpectogramChannel(self, index):
        self.spectogramChannel = index
        self.drawSpectogram(self.ui.colorPaletteComboBox.currentText())



    def reset(self):
        for timer in self.allChannelsTimers:
            timer.setInterval(100)
            timer.stop()

    def play(self) :
        # if (self.channalsStates[self.selectedChannel].isChecked()):
        self.allChannelsTimers[self.selectedChannel].start()

    def pause(self):
        self.allChannelsTimers[self.selectedChannel].stop()

    def zoomIn(self):
        xrange, yrange = self.ui.signalPlotter.viewRange()
        self.xCoff /= 2
        self.yCoff /= 2
        self.ui.signalPlotter.setYRange(yrange[0]/2, yrange[1]/2, padding=0)
        self.ui.signalPlotter.setXRange(xrange[0]/2, xrange[1]/2, padding=0)

    def zoomOut(self):
        self.xCoff *= 2
        self.yCoff *= 2
        xrange, yrange = self.ui.signalPlotter.viewRange()
        self.ui.signalPlotter.setYRange(yrange[0]*2, yrange[1]*2, padding=0)
        self.ui.signalPlotter.setXRange(xrange[0]*2, xrange[1]*2, padding=0)

    def speedUp(self):
        _timer = self.allChannelsTimers[self.selectedChannel]
        _timer.setInterval(max(_timer.interval()-20,0))
    # we don't want to get an interval with minus that's why i made it to be 0 at the minimum value
    
    def speedDown(self):
        _timer = self.allChannelsTimers[self.selectedChannel]
        _timer.setInterval(_timer.interval()+20)


    def moveInX(self):
        graphXAxesData = self.xAxesData[self.selectedChannel][:self.signalLastIndex[self.selectedChannel]]
        value = self.ui.XAxesSlider.value()/100
        xMax = max(graphXAxesData)*value
        xMin = xMax - self.xCoff
        self.ui.signalPlotter.plotItem.setXRange(xMin, xMax)

    def moveInY(self):
        graphYAxesData = self.yAxesData[self.selectedChannel][:self.signalLastIndex[self.selectedChannel]]
        value = self.ui.YAxesSlider.value()/100 - 0.5
        if value > 0:
            yMax = max(graphYAxesData)*value
            yMin = yMax - self.yCoff
            self.ui.signalPlotter.plotItem.setYRange(yMin, yMax)
    
    def saveAs(self):
        report = PdfPages('report.pdf')

        for IDX in range(3):
            if self.xAxesData[IDX] != None:
                report.savefig(self.getFigure(IDX))
                report.savefig(self.getSpectrogram(IDX))
                report.savefig(self.sigMean(IDX))

        report.close()


    def getFigure(self,i):
        fig = plt.figure(figsize=(10, 5))

        plt.plot(self.xAxesData[i][:self.signalLastIndex[i]],self.yAxesData[i][:self.signalLastIndex[i]])
        plt.xlabel('time (sec)')
        plt.ylabel('amplitude (mv)')
        return fig

    def getSpectrogram(self,i):
        # fs = 1 / (self.x[1] - self.x[0])
        fig = plt.figure(figsize=(10, 5))
        plt.specgram(self.yAxesData[i], Fs=200)
        plt.ylabel('time (sec)')
        plt.xlabel('frequency (Hz)')
        return fig



    def sigMean(self,i):

            graphYAxesData = self.yAxesData[i][:self.signalLastIndex[i]]
            graphXAxesData = self.xAxesData[i][:self.signalLastIndex[i]]
            time = max(graphXAxesData)

            print('Mean of your_column_number :            ', (np.mean(graphYAxesData)))
            mean = np.mean(graphYAxesData)
            maximum = np.max(graphYAxesData)
            minimum = np.min(graphYAxesData)
            Std = np.std(graphYAxesData)
            data = [["mean", mean], ["maximum", maximum], ["minimum", minimum], ["standard devision", Std],["time", time]]
            table = pd.DataFrame(data)      #https://stackoverflow.com/questions/32137396/how-do-i-plot-only-a-table-in-matplotlib
            fig, ax = plt.subplots(figsize=(12, 4))

            ax.axis('tight')
            ax.axis('off')
            ax.table(cellText=table.values,colLabels=table.columns,loc='center')
            return fig


if __name__ == '__main__':      
    app = QtWidgets.QApplication(sys.argv)
    main = mainApp()
    main.show()
    sys.exit(app.exec_())