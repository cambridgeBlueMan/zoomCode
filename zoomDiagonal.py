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
# top right to top left
for count in range(framerate*duration, 0, -1):
    camera.zoom = (count/(2*framerate*duration) , 0,1920/4056, 1080/3040)
    #print(camera.zoom)
    sleep(1/zoomSpeed )
    #print (count)
    
  
# top left to bottom left
for count in range(0, framerate*duration):
    camera.zoom = (0, count/(2*framerate*duration) ,1920/4056, 1080/3040)
    #print(camera.zoom)
    sleep(1/zoomSpeed )
    #print (count)
    
# bottom left to top left
for count in range(framerate*duration, 0, -1):
    camera.zoom = (0, count/(2*framerate*duration) ,1920/4056, 1080/3040)
    #print(camera.zoom)
    sleep(1/zoomSpeed )
    #print (count)



maxW = 1
maxH = 1
startX = 1068/4056
endX = 0
startY = 980/3040
endY = 0
startW = 1920/4056
endW = 1
startH = 980/3040
endH = 1

 
# zooming out from centre
for count in range(0, framerate*duration):
    # x will get smaller and eventually be 0, as we move to the and full sensor view
    x = (startX - ((startX*count)/(framerate*duration)))
    # y will get smaller and eventually be 0 as we move to the top and full sensor view
    y = (startY - ((startY*count)/(framerate*duration)))
    # width will grow from startwidth to eventauuly be full sensor size
    w = (startW + ((maxW - startW)*count)/(framerate*duration))
    # height will start from startheight and eventually be full sensor height
    h = (startH + ((maxH - startH)*count)/(framerate*duration))
    camera.zoom = (x,y,w,h)
    #print(camera.zoom)
    sleep(1/zoomSpeed )
    #print (count)

# zooming in from full sensor view
for count in range(0, framerate*duration):
    # x starts at 0 and eventually grows to be startX
    mul = count/(framerate*duration)
    x = startX*mul
    # y starts at 0 and eventually startY 
    y = startY*mul
    # width will shrink from 1 down to startW
    w = 1 - ((1-startW)*mul)
    # height will start from startheight and eventually be full sensor height
    h = 1 - ((1-startH)*mul)  
    camera.zoom = (x,y,w,h)
    #print(camera.zoom)
    sleep(1/zoomSpeed )
    #print (count)
camera.stop_recording