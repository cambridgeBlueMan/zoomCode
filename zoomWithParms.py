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
"""
for horizontal movement across the sensor the only thing that changes is x
if y is zero then you are travelling from left to right
y could be any value up to (3040-1080)/3040. This is 0.6447368421052632
so effectively y could be any value up to .664 or 1960 pixels

max x is (4056-1080)/4056. This is 0.7337278106508875

Similarly x doesnt have to start at 0 and doesn't have to end at 

"""
startZoom = (count/framerate*duration , 0,1920/4056, 1080/3040)

delta = 1/framerate*duration

# top left to top right
#for count in range(0, framerate*duration):
x = 0
startX = 0.2
endX = 0.2
while x < (4056-1920)/4056 - endX:
    #start of iteration
    x = startX + count/(framerate*duration)

    camera.zoom = (x , 0,1920/4056, 1080/3040)
    print(x)
    #print(camera.zoom)
    sleep(1/zoomSpeed )
    count += 1
    print (count)
    #end of iteration
print("any key to quit")
input()
sys.exit()