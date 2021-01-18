from PyQt5 import QtCore, QtGui, QtWidgets
from zoomCodeGui import Ui_Form
from picamera import PiCamera
from time import sleep
import sys
import datetime
import cameraFunctions
"""
MainWindow.ui is a file initially created in QtDesigner.  This file is then translated into
a single Python class called Ui_MainWindow by pyuic5.

(substitue MainWindow for the name you gave the Dialo or MianWindow object in Designer)
"""
#from camera2 import *


"""
The Code_MainWindow class is to define all the logic and functions for the program to operate
Most of these functions will already have been referenced in the designer file via signal/slot connections

Note that this class has to inherit from the relevant parent class. In this case a QDialog,
but could as easily be a QMainMenu

remember that this means that this is a Dialog window or other window with some added code/methods

This Dialog window with added code will be passed to an instance of the automatically
created Designer class. This designer created class has methods to draw the various widgets and associate them 
with the passed instance of the code/widget class
"""
class Code_Form(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        # Ui_MainWindow is the main designer generated class. so create one
        self.camera = PiCamera()
        self.ui = Ui_Form()
        # now pass the main window object to it so that the setupUi method can draw all
        # the widgets into the window
        self.ui.setupUi(self)
        self.show()
        # initialise vars
        #self.doCameraStuff()
        #self.camera = PiCamera()
        # get indents from the line edit objects
        # set pixel width and height
        self.sensorWidth = 4056
        self.sensorHeight = 3040
        self.pixelWidth  = 1/self.sensorWidth
        self.pixelHeight = 1/self.sensorHeight
        self.resolutionWidth = 960 #1920
        self.resolutionHeight = 1080
        self.camera.resolution = (self.resolutionWidth, self.resolutionHeight)
        #self.camera.rotation = 180
        # set framerate 
        self.framerate = 30.0
        self.duration = self.getDuration()
        self.speed = 4
        self.increment = 1.0/self.sensorWidth #(self.framerate*self.duration)
        self.resolution = (1920,1080)
        self.indents = self.getIndents
        self.camera.start_preview(fullscreen = False, window = (1260,0,480,540))
        self.camera.sensor_mode = 1
        self.camera.framerate = self.framerate
        self.fig = 1440
        
    def generateFileName(self):
        filePrefix = "vid_"
        fileExtension = ".h264"
        return filePrefix + str(datetime.datetime.now()).replace(':','_').replace('.', '_').replace(' ','') + fileExtension
  
    def getIndents(self):
         # get indents from the line edit objects and put them into a dictionary
        indents = {
            "left": float(self.ui.leftIndent.text())/self.sensorWidth,
            "right": float(self.ui.rightIndent.text())/self.sensorWidth,
            "top": float(self.ui.topIndent.text())/self.sensorHeight,
            "bottom": float(self.ui.bottomIndent.text())/self.sensorHeight
            }
        #print(indents)
        return(indents)
        
    def setAndShowPreview(self,but):
        self.camera.stop_preview()
        print(self.sender().objectName())
        indents = self.getIndents()
        print(type(indents))
        # which preview is it?
        width = self.resolutionWidth/self.sensorWidth
        height = self.resolutionWidth/self.sensorWidth
        if self.sender().objectName() == 'rightPreview':
            startZoom = (((self.sensorWidth -self.resolutionWidth)/self.sensorWidth) - indents["right"] ,
                         indents["top"], width, height)  
        elif self.sender().objectName() == 'leftPreview':
            startZoom = (indents["left"],
                         indents["top"], width, height)  
        elif self.sender().objectName() == 'topPreview':
            startZoom = (indents["left"],
                         indents["top"] , width, height)  
        elif self.sender().objectName() == 'bottomPreview':
            startZoom = (indents["left"], (((self.sensorHeight-self.resolutionHeight)/self.sensorHeight) - indents["bottom"]) ,
                         width, height)  
        elif self.sender().objectName() == 'fullSensor':
            startZoom = (0,0,self.sensorWidth,self.sensorHeight)
            
        # now set the zoom and show the preview   
        self.camera.zoom = startZoom
        self.camera.start_preview(fullscreen = False, window = (960,0,960,540))
        
    def leftToRight(self):
        # top left to top right
        indents = self.getIndents()
        x = 0
        count = 0
        self.camera.start_preview(fullscreen = False, window = (960,0,960,540))
        while True:
            #start of iteration
            x = indents["left"] + self.increment*float(count)*self.speed
            if x >= (4056-1920)/4056 - indents["right"]:
                break
            #print(x)
            self.camera.zoom = (x , indents["top"], self.resolutionWidth/self.sensorWidth, self.resolutionWidth/self.sensorWidth)
            #print(camera.zoom)
            sleep(1/self.framerate)
            count += 1
            #print (count)
            #end of iteration
            
    def topToBottom(self):
        
        # top to bottom
        indents = self.getIndents()
        y = 0
        count = 0
        self.camera.start_preview(fullscreen = False, window = (960,0,960,540))
        while True:
            y = indents["top"] + + self.increment*float(count)*self.speed
            print(y)
            if y > ((3040-1080)/3040) - (indents["top"] + indents["bottom"]):
                break
            self.camera.zoom = (indents["left"], y ,self.resolutionWidth/self.sensorWidth, self.resolutionWidth/self.sensorWidth)
            #print(camera.zoom)
            sleep(1/self.framerate )
            count += 1

    def bottomToTop(self):
        indents = self.getIndents()
        y = 1
        count = 0
        self.camera.start_preview(fullscreen = False, window = (960,0,960,540))
        # bottom to top 
        while True:
            y = ((3040-1080)/3040) - + self.increment*float(count)*self.speed
            if y <=0:
                break
            self.camera.zoom = (indents["left"], y ,self.resolutionWidth/self.sensorWidth, self.resolutionWidth/self.sensorWidth)
            #print(camera.zoom)
            sleep(1/self.framerate )
            count += 1
                 
    def rightToLeft(self):
        # top right to top left
        indents = self.getIndents()
        x = 1 - indents["right"]
        count = 0 #framerate*duration
        self.camera.start_preview(fullscreen = False, window = (960,0,960,540))    
        #for count in range(framerate*duration, 0, -1):
        while True:
            x = (1 - (self.resolutionWidth/self.sensorWidth)) - + self.increment*float(count)*self.speed
            self.camera.zoom = (x , indents["top"],
                                self.resolutionWidth/self.sensorWidth,
                                self.resolutionWidth/self.sensorWidth)
            if x <=indents["left"]:
                break
            #print(camera.zoom)
            sleep(1/self.framerate )
            count += 1
    
    def doZoom(self):
        # Is this a left to right zoom? 
        if self.sender().objectName()=='lrShow':
            # If so then are we going l-r or r-l
            if self.ui.left.isChecked():
                self.leftToRight()
            if self.ui.right.isChecked():
                self.rightToLeft()
        else:
            # This is top to bottom
            if self.ui.top.isChecked():
                self.topToBottom()
            else:
                self.bottomToTop()
                
    def getFileNameFromUser(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName() #getExistingDirectory(args[0], "get directory", "/home")
        #print (self.ui.path.text())
        #print (fileName)
        #print(args)
        #ui.path.setText(fileName[0])
        #print (self.ui.path.text())
        return fileName[0]
    
    def doCaptureStill(self):
        if self.ui.isGetFileName.isChecked():
            fileName = self.getFileNameFromUser()      
        else:
            fileName = cameraFunctions.generateFileName('v')
        #self.camera.capture(fileName)
        self.camera.start_recording(fileName)
    def doZoomWithRecord(self):
        print(self.ui.isGetFileName.isChecked())
        if self.ui.isGetFileName.isChecked():
            fileName = self.getFileNameFromUser()      
        else:
            fileName = cameraFunctions.generateFileName('v')
        self.camera.start_recording(fileName)
        # Is this a left to right zoom? 
        if self.sender().objectName()=='lrRecord':
            # If so then are we going l-r or r-l
            if self.ui.left.isChecked():
                self.leftToRight()
            if self.ui.right.isChecked():
                self.rightToLeft()
        else:
            # This is top to bottom
            if self.ui.top.isChecked():
                self.topToBottom()
            else:
                self.bottomToTop()
        self.camera.stop_recording()
        
    def doQuit(args):
        if self.camera.recording:
            self.camera.stop_recording()
        print(args)
        sys.exit(app.exec_())
        
    def getSaveFileName(*args):
        directory = QtWidgets.QFileDialog.getSaveFileName() #getExistingDirectory(args[0], "get directory", "/home")
        print (ui.path.text())
        print (directory)
        print(args)
        ui.path.setText(directory[0])
        print (ui.path.text())
        
    def getDuration(self):
        print(self)
        self.duration=float(self.ui.duration.text())
        self.increment = 1.0/(self.framerate*self.duration)
        return self.duration


#######################################################################################
    #                           END OF CLASS
#######################################################################################
if __name__ == "__main__":
    import sys
    # instiantiate an app object from the QApplication class 
    app = QtWidgets.QApplication(sys.argv)
    # instantiate an object containing the logic code
    MainWindow = Code_Form()
    sys.exit(app.exec_())


