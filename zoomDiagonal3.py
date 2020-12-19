import picamera
from time import sleep
camera = picamera.PiCamera()
import sys
#camera.zoom =  (0,0, 0.47337278106508873, 0.35526315789473684)
camera.zoom = (0,0,1920/4056,1080/3040)
# this preview size is half the full size
camera.start_preview(fullscreen = False, window = (0,0,int(960),int(540)))
camera.resolution=  (1920,1080)
camera.start_recording("vid1.h264")

# 30fps is the default camera framerate4
framerate = 30
zoomSpeed = 60
duration = 80
count = 0


startX = (4056-1920)/4056
    
endX = 0
startY = 980/3040
endY = 0
startW = 1920/4056
endW = 1
startH = 980/3040
endH = 1
# x,y,w,h
startZoom = (count/framerate*duration , 0, 1920/4056, 1080/3040)

delta = 1/framerate*duration

# move diagonally
#while count < framerate*duration:
count=0
x=0
w=1920/4056
y=0
h=1080/3040
while  (y+h) <= 1:
    count=count +1

#for count in range(0, framerate*duration):
    #start of iteration
    x = startX - count/(2*framerate*duration)
    y = count/(2*framerate*duration)
    h =(980/3040 + ((1 - startH)*count)/(framerate*duration))
    w =(1920/4056 + ((1 - startW)*count)/(framerate*duration))
    
    camera.zoom = (x, y, w, h)
    #print(camera.zoom)
    sleep(1/zoomSpeed )
    #print ("This is count: " + str (count))

#print ("Right hand border: " + str(x+w))
    #print ("Bottom border: " + str (y+h))
    
print("hit any key to finish")
input ()
camera.stop_recording
sys.exit()


