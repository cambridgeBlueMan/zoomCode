from PyQt5 import QtCore, QtGui, QtWidgets

# insert appropriate names here
from vwBrightness import Ui_Dialog
#
from picamera import PiCamera
from time import sleep
import sys
import datetime
import cameraFunctions
"""
You may need to change the line declaring the class below. It will depend on the choice you make
for your containing window: main window, dialog box etc)
"""
class Code_Dialog(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        # Ui_Form is the main designer generated class. so instantiate one. Precede the variable name with
        # the word 'self'

        self.ui = Ui_Dialog()
        # now pass the main window object to it so that the setupUi method can draw all
        # the widgets into the window
        self.ui.setupUi(self)
        self.show()
        # now instantiate a camera object. Again the variable name is preceded by the word 'self'
        self.camera = PiCamera()
        # you might then declare and initialise some variable which will be available across the class
        self.framerate = 30.0
        self.resolution = (1920,1080)
        # you might then invoke some methods of your camera object
        self.camera.start_preview(fullscreen = False, window = (960,0,960,540))
        # or set sone attributes
        self.camera.sensor_mode = 1
        """
        Note the following line:
        
        self.framerate is a variable you named and initialised.
        self.camera.framerate is an attribute of the camera object
        the code line sets the camera's framerate to the value held in the framerate variable
        """
        self.camera.framerate = self.framerate

        # add your own method functions below

    def someMethodName(self):
        print(self)

    def AnotherMethod(self):
        print(self)
    def takePhoto(self):
        #print(self)
        vwPhoto = cameraFunctions.generateFileName('s')
        print(vwPhoto)
        self.camera.capture(vwPhoto)
    def startRecording(self):
        #print(self)
        vwVideo = cameraFunctions.generateFileName('v')
        print(vwVideo)
        self.camera.start_recording(vwVideo)
    def stopRecording(self):
        #print(self)
        #print(vwVideo)
        self.camera.stop_recording()
    def showPreview(self):
        #self.camera.start_preview()
        if self.sender().isChecked():
            self.camera.start_preview(fullscreen = False, window = (960,0,960,540))
        else:
            self.camera.stop_preview()
        print(self)
    
    def changeBrightness(self):
        #print(self)
        print(self.sender().value())
        self.camera.brightness = self.sender().value()


#######################################################################################
    #                           END OF CLASS
#######################################################################################
if __name__ == "__main__":
    import sys
    # instiantiate an app object from the QApplication class 
    app = QtWidgets.QApplication(sys.argv)
    # instantiate an object containing the logic code
    MainWindow = Code_Dialog()
    sys.exit(app.exec_())
                                                                                                                                                                                                                 
                                                                                                                                                                                                                 