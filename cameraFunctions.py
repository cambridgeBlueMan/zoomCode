from picamera import PiCamera
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import sys
import datetime

def generateFileName(type='n'):
    """
    generate a unique generic filename for either a video file or a still image jpeg file.
    
    usage:
    
        name = generateFileName(type)
    
    will return the filename as a string to the variable 'name'.
    
    type can be 'v' for video, or 's' for still image. default is 'n' for none :)
    
    """
    if type == 'v':
        path = "/home/pi/Videos/"
        filePrefix = "video_"
        fileExtension = ".h264"
        # assemble and return filename and path
        return path + filePrefix + str(datetime.datetime.now()).replace(':','_').replace('.', '_').replace(' ','') + fileExtension
    if type == 's':
        # assemble and return filename and path
        path = "/home/pi/Pictures/"
        filePrefix = "image_"
        fileExtension = ".jpeg"
        return path + filePrefix + str(datetime.datetime.now()).replace(':','_').replace('.', '_').replace(' ','') + fileExtension
    if type == 'n':
        print("You must provide a file type for this function")
        
def getFileNameFromUser():
    """
    open a qt file dialog box so that the user can provide their own filename
    """
    fileName = QtWidgets.QFileDialog.getSaveFileName() #getExistingDirectory(args[0], "get directory", "/home")
    return fileName[0]
    
"""


name = generateFileName('s')
print(name)
camera = PiCamera()
#camera.brightness = 55
#camera.zoom = (1000,1000,1024,768)

camera.start_preview(fullscreen = False, window = (900, 0, 960,540))
camera.resolution = (1920,1080)
# Camera warm-up time
while True:
    i = input()
    if i == 'q':
        sys.exit()
    if i == '':
        print('in else')
        name = generateFileName()
        #camera.capture(name)
        camera.start_recording(name)
    if i == 's':
        camera.stop_recording()

"""