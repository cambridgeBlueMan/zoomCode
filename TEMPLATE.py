from PyQt5 import QtCore, QtGui, QtWidgets

# insert appropriate names here
from 'yourGuiFile' import 'classNameInYourGuiFile'
#
from picamera import PiCamera
from time import sleep
import sys
import datetime
"""
You may need to change the line declaring the class below. It will depend on the choice you make
for your containing window: main window, dialog box etc)
"""
class Code_Form(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        # Ui_Form is the main designer generated class. so instantiate one. Precede the variable name with
        # the word 'self'
        
        self.ui = Ui_Form()
        # now pass the main window object to it so that the setupUi method can draw all
        # the widgets into the window
        self.ui.setupUi(self)
        self.show()
        # now instantiate a camera object. Again the variable name is preceded by the word 'self'
        self.camera = PiCamera()
        # you might then declare and initialise some variable which will be available across the class
        self.framerate = 50.0
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


