import picamera
from time import sleep
camera = picamera.PiCamera()
import sys
import datetime
#camera.zoom =  (0,0, 0.47337278106508873, 0.35526315789473684)
camera.zoom = (0,0,1920/4056,1080/3040)
# this preview size is half the full size
camera.resolution=  (1920,1080)
#camera.start_recording("vid1.h264")


filePrefix = "vid_"
fileExtension = ".h264"

# 30fps is the default camera framerate4
framerate = 30.0
zoomSpeed = 30.0
duration = 30.0
count = 0





increment = 1.0/(framerate*duration)


leftIndent = 0.0
rightIndent = 0.0
topIndent = 0.0
bottomIndent = 0.0


def generate_file_name():
    return filePrefix + str(datetime.datetime.now()).replace(':','_').replace('.', '_').replace(' ','') + fileExtension

def left_to_right():
    # top left to top right
    x = 0
    count = 0
    camera.start_preview(fullscreen = False, window = (960,0,960,540))
    while True:
        #start of iteration
        x = leftIndent + increment*float(count)
        if x >= (4056-1920)/4056 - rightIndent:
            break
        #print(x)
        camera.zoom = (x , topIndent,1920/4056, 1080/3040)
        #print(camera.zoom)
        sleep(1/zoomSpeed )
        count += 1
        #print (count)
        #end of iteration
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
    x = 1 - rightInden
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
 



print("q to quit. fp for full preview. splr for start preview. eplr for end preview. c to clear the preview. zlr to run the zoom left to right")
print("zrl to run the zoom right to left etc. upper case Z to record the zoom")
print("li, ri, ti and bi to set indents")
while True:
    cmd = input ()
    # LEFT TO RIGHT
    if cmd == "splr" or cmd == "eprl":
        startZoom = (leftIndent, topIndent, 1920/4056, 1080/3040)
        camera.zoom = startZoom
        camera.start_preview(fullscreen = False, window = (960,0,960,540))
    if cmd == "eplr" or cmd == "sprl":
        camera.stop_preview()
        startZoom = (((4056-1920)/4056) - rightIndent , topIndent, 1920/4056, 1080/3040)
        camera.zoom = startZoom
        camera.start_preview(fullscreen = False, window = (960,0,960,540))
    # TOP TO BOTTOM PREVIEWS  
    if cmd == "sptb" or cmd == "epbt":
        camera.stop_preview()
        camera.zoom = (leftIndent, topIndent ,1920/4056, 1080/3040)
        camera.start_preview(fullscreen = False, window = (960,0,960,540))
    if cmd == "eptb" or cmd =="spbt":
        camera.stop_preview()
        camera.zoom = (leftIndent, (((3040-1080)/3040) - bottomIndent) ,1920/4056, 1080/3040)
        camera.start_preview(fullscreen = False, window = (960,0,960,540))
    
    if cmd == "fp":
        camera.stop_preview()
        camera.zoom = (0,0,4056,3040)
        camera.start_preview(fullscreen = False, window = (960,0,960,540))
    if cmd == "Fp":
        camera.stop_preview()
        camera.zoom = (0,0,4056,3040)
        camera.start_preview(fullscreen = False, window = (950,0,960,540))
        fileName = generate_file_name()
        camera.start_recording(fileName)
        input()
        camera.stop_recording()
    if cmd == "c":
        camera.stop_preview()
    # ZOOM LEFT RIGHT
    if cmd == "zlr":
        left_to_right()
    # ZOOM LEFT TO RIGHT WITH RECORD
    if cmd == "Zlr":
        fileName = generate_file_name()
        camera.start_recording(fileName)
        left_to_right()
        camera.stop_recording()
    # ZOOM RIGHT TO LEFT
    if cmd == "zrl":
        right_to_left()
    # ZOOM RIGHT TO LEFT WITH RECOR-D
    if cmd == "Zrl":
        fileName = generate_file_name()
        camera.start_recording(fileName)
        right_to_left()
        camera.stop_recording()
    # ZOOM TOP TO BOTTOM
    if cmd == "ztb":
        top_to_bottom()
    # ZOOM TOP TO BOTTOM WITH RECORD
    if cmd == "Ztb":
        fileName = generate_file_name()
        camera.start_recording(fileName)
        top_to_bottom()
        camera.stop_recording()
    #ZOOM BOTTOM TO TOP
    if cmd == "zbt":
        bottom_to_top()
    #ZOOM BOTTOM TO TOP WITH RECORDING
    if cmd == "Zbt":
        fileName = generate_file_name()
        camera.start_recording(fileName)
        bottom_to_top()
        camera.stop_recording()
    if cmd == "q":
        sys.exit()
    if cmd == "li":
        indent=input()
        print (indent)
        leftIndent = float(indent)
    if cmd == "ri":
        indent=input()
        leftIndent = float(indent)
    if cmd == "ti":
        indent=input()
        leftIndent = float(indent)
    if cmd == "bi":
        indent=input()
        leftIndent = float(indent)



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