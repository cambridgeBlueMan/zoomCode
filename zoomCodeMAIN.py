from PyQt5 import QtCore, QtGui, QtWidgets
from zoomCodeGui import Ui_Form
from picamera import PiCamera
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
        #self.leftIndent = 0
        self.topIndent = 0
        #self.topIndent = 0
        #self.bottomIndent = 0
        self.camera.start_preview(fullscreen = False, window = (960,0,960,540))
        
    def setAndShowPreview(self,but):
        print(self.topIndent)
        # get indents from the line edit objects
        leftIndent = float(self.ui.leftIndent.text())
        rightIndent = float(self.ui.rightIndent.text())
        topIndent = float(self.ui.topIndent.text())
        bottomIndent = float(self.ui.bottomIndent.text())
        print(leftIndent)
        
        self.camera.stop_preview()
        print(self.sender().objectName())
        # which preview is it?
        if self.sender().objectName() == 'rightPreview':
            startZoom = (((4056-1920)/4056) - rightIndent , topIndent, 1920/4056, 1080/3040)  
        elif self.sender().objectName() == 'leftPreview':
            startZoom = (leftIndent, topIndent, 1920/4056, 1080/3040)
        elif self.sender().objectName() == 'topPreview':
            startZoom = (leftIndent, topIndent ,1920/4056, 1080/3040)
        elif self.sender().objectName() == 'bottomPreview':
            startZoom = (leftIndent, (((3040-1080)/3040) - bottomIndent) ,1920/4056, 1080/3040)
            
        # now set the zoom and show the preview   
        self.camera.zoom = startZoom
        self.camera.start_preview(fullscreen = False, window = (960,0,960,540))
if __name__ == "__main__":
    import sys
    # instiantiate an app object from the QApplication class 
    app = QtWidgets.QApplication(sys.argv)
    # instantiate an object containing the logic code
    MainWindow = Code_Form()
    sys.exit(app.exec_())


