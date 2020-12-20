import picamera
from time import sleep
camera = picamera.PiCamera()
import sys
#camera.zoom =  (0,0, 0.47337278106508873, 0.35526315789473684)
camera.zoom = (0,0,1920/4056,1080/3040)
# this preview size is half the full size
camera.resolution=  (1920,1080)
#camera.start_recording("vid1.h264")

# 30fps is the default camera framerate4
framerate = 30.0
zoomSpeed = 40
duration = 30.0
count = 0






increment = 1.0/(framerate*duration)

# top left to top right
#for count in range(0, framerate*duration):
leftIndent = 0.1
rightIndent = 0.1
topIndent = 0
bottomIndent = 0
def left_to_right():
    x = 0
    count = 0
    camera.start_preview(fullscreen = False, window = (960,0,960,540))
    while x < (4056-1920)/4056 - rightIndent:
        #start of iteration
        x = leftIndent + increment*float(count)
        print(x)
        camera.zoom = (x , 0,1920/4056, 1080/3040)
        #print(camera.zoom)
        sleep(1/zoomSpeed )
        count += 1
        print (count)
        #end of iteration
def right_to_left():
    # top right to top left
    x = 1 - rightIndent
    count = 0 #framerate*duration
    camera.start_preview(fullscreen = False, window = (960,0,960,540))    
    #for count in range(framerate*duration, 0, -1):
    while x > (0 + leftIndent):
        x = (1 - ((4056-1920)/4056) - leftIndent) - increment*float(count)
        camera.zoom = (x , 0, 1920/4056, 1080/3040)
        #print(camera.zoom)
        sleep(1/zoomSpeed )
        count += 1
        print (count)
    
print("r to run. sp for start preview. ep for end preview. c to clear the preview. zlr to run the zoom left to right")
print("zrl to run the zoom right to left")
while True:
    cmd = input ()
    if cmd == "sp":
        startZoom = (leftIndent + (increment*count) , 0,1920/4056, 1080/3040)
        camera.zoom = startZoom
        camera.start_preview(fullscreen = False, window = (960,0,960,540))
    if cmd == "ep":
        camera.stop_preview()
        startZoom = (((4056-1920)/4056) - rightIndent , 0,1920/4056, 1080/3040)
        camera.zoom = startZoom
        camera.start_preview(fullscreen = False, window = (960,0,960,540))
    if cmd == "c":
        camera.stop_preview()
    if cmd == "zlr":
        left_to_right()
    if cmd =="zrl":
        right_to_left()
    if cmd == "q":
        sys.exit()


camera.start_preview(fullscreen = False, window = (0,0,960,540))


    

#print("any key to quit")
#input()
    
# top right to top left
for count in range(framerate*duration, 0, -1):
    camera.zoom = (increment*count/2 , 0,1920/4056, 1080/3040)
    #print(camera.zoom)
    sleep(1/zoomSpeed )
    #print (count)
    
  
# top left to bottom left
for count in range(0, framerate*duration):
    camera.zoom = (0, increment*count/2 ,1920/4056, 1080/3040)
    #print(camera.zoom)
    sleep(1/zoomSpeed )
    #print (count)
    
# bottom left to top left
for count in range(framerate*duration, 0, -1):
    camera.zoom = (0, increment*count/2 ,1920/4056, 1080/3040)
    #print(camera.zoom)
    sleep(1/zoomSpeed )
    #print (count)



maxW = 1
maxH = 1
leftIndent = 1068/4056
rightIndent = 0
startY = 980/3040
endY = 0
startW = 1920/4056
endW = 1
startH = 980/3040
endH = 1

 
# zooming out from centre
for count in range(0, framerate*duration):
    # x will get smaller and eventually be 0, as we move to the and full sensor view
    x = (leftIndent - ((leftIndent*count)/(framerate*duration)))
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
    # x starts at 0 and eventually grows to be leftIndent
    mul = count/(framerate*duration)
    x = leftIndent*mul
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

# x,y,w,h
"""
for horizontal movement across the sensor the only thing that changes is x
if y is zero then you are travelling from left to right
y could be any value up to (3040-1080)/3040. This is 0.6447368421052632
so effectively y could be any value up to .664 or 1960 pixels

max x is (4056-1080)/4056. This is 0.7337278106508875

Similarly x doesnt have to start at 0 and doesn't have to end at 

"""