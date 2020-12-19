import picamera
from time import sleep
camera = picamera.PiCamera()
import sys
#camera.zoom =  (0,0, 0.47337278106508873, 0.35526315789473684)
camera.zoom = (0,0,1920/4056,1080/3040)
# this preview size is half the full size
camera.start_preview(fullscreen = False, window = (0,0,960,540))
camera.resolution=  (1920,1080)
#camera.start_recording("vid1.h264")

# 30fps is the default camera framerate4
framerate = 30
zoomSpeed = 40
duration = 30
count = 0

# x,y,w,h
startZoom = (count/framerate*duration , 0,1920/4056, 1080/3040)

delta = 1/framerate*duration

# top left to top right
#while count < framerate*duration:
    

for count in range(0, framerate*duration):
    #start of iteration
    camera.zoom = (count/(2*framerate*duration) , count/(2*framerate*duration),1920/4056, 1080/3040)
    #print(camera.zoom)
    sleep(1/zoomSpeed )
    print (count)
    #count = count + 1
    #end of iteration
sys.exit()

