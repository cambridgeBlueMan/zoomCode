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
        #self.topIndent = 0
        #self.topIndent = 0
        #self.bottomIndent = 0
         # get indents from the line edit objects
        leftIndent = float(self.ui.leftIndent.text())
        rightIndent = float(self.ui.rightIndent.text())
        topIndent = float(self.ui.topIndent.text())
        bottomIndent = float(self.ui.bottomIndent.text())
        print(leftIndent)
        self.camera.start_preview(fullscreen = False, window = (960,0,960,540))
        
    def setAndShowPreview(self,but):
       
        
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
        elif self.sender().objectName() == 'fullSensor':
            startZoom = (0,0,4056,3040)
        
            
        # now set the zoom and show the preview   
        self.camera.zoom = startZoom
        self.camera.start_preview(fullscreen = False, window = (960,0,960,540))
        
    def leftToRight(self):
        # top left to top right
        x = 0
        count = 0
        self.camera.start_preview(fullscreen = False, window = (960,0,960,540))
        while True:
            #start of iteration
            x = self.leftIndent + increment*float(count)
            if x >= (4056-1920)/4056 - self.rightIndent:
                break
            #print(x)
            self.camera.zoom = (x , self.topIndent,1920/4056, 1080/3040)
            #print(camera.zoom)
            sleep(1/zoomSpeed )
            count += 1
            #print (count)
            #end of iteration
            """
    def top_to_bottom():
        # top to bottom
        y = 0
        count = 0
        camera.start_preview(fullscreen = False, window = (960,0,960,540))
        while True:
            y = topIndent + increment*count
            if y > ((3040-1080)/3040) - (topIndent + bottomIndent):
                break
            camera.zoom = (leftIndent, y ,1920/4056, 1080/3040)
            #print(camera.zoom)
            sleep(1/zoomSpeed )
            count += 1
            #print (count)

    def bottom_to_top():
        y = 1
        count = 0
        camera.start_preview(fullscreen = False, window = (960,0,960,540))
        # bottom to top 
        while True:
            y = ((3040-1080)/3040) - increment*count
            if y <=0:
                break
            camera.zoom = (leftIndent, y ,1920/4056, 1080/3040)
            #print(camera.zoom)
            sleep(1/zoomSpeed )
            count += 1
            #print (count)
            
        
    def right_to_left():
        # top right to top left
        x = 1 - rightIndent
        count = 0 #framerate*duration
        camera.start_preview(fullscreen = False, window = (960,0,960,540))    
        #for count in range(framerate*duration, 0, -1):
        while True:
            x = (1 - ((4056-1920)/4056) - leftIndent) - increment*float(count)
            camera.zoom = (x , topIndent, 1920/4056, 1080/3040)
            if x <=leftIndent:
                break
            #print(camera.zoom)
            sleep(1/zoomSpeed )
            count += 1
            #print (count)
     """



    def doZoom(self):
        print(self)
        # Is this a left to right zoom? 
        if self.sender().objectName()=='lrShow':
            print('in lrshow')
            # If so then are we going l-r or r-l
            if self.ui.left.isChecked():
                print('in left')
                self.leftToRight()
            if self.ui.right.isChecked():
                print('in right')
        else:
            # This is top to bottom
            print('in tbshow')
            if self.ui.top.isChecked():
                print('top')
            else:
                print('bottom')
        
        #we need to know who sent this and we need to know which way they want it to go.who sent it is contained in the object name of the button and which way to go is contained in the state of the radio button
    def doZoomWithRecord(args):
        print(args)
    def doQuit(args):
        print(args)
        sys.exit(app.exec_())
    def setDuration(args):
        print(args)
        duration=float(self.ui.duration.text())

#######################################################################################
if __name__ == "__main__":
    import sys
    # instiantiate an app object from the QApplication class 
    app = QtWidgets.QApplication(sys.argv)
    # instantiate an object containing the logic code
    MainWindow = Code_Form()
    sys.exit(app.exec_())


