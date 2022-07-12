# import necessary libraries
import cv2
from matplotlib.pyplot import draw
import numpy as np
import handtracking_module as htm 
import os 
import time

# import images 
folderPath = "paint_tools"
# to store them we will use os
# os.listdir to list all the elements in that directory
myList = os.listdir(folderPath)
# print (myList)
overlayList = []


# specify a high level of detection confidence as parameter because we want the painting to be precise
detector = htm.handTracker(detectionCon=0.85)
# uint8 = 8-bit unsigned integer (from 0 to 255)
# create painting canvas
imgCanvas = np.zeros((700, 1212, 3), np.uint8)
###########################
DrawColor = (0,0,0)
BrushThickness = 15
EraserThickness = 100
xp, yp = 0,0
###########################

# we need to import the images to overlay them at the top (in the next steps)
for imagePath in myList:
    image = cv2.imread(f'{folderPath}/{imagePath}')
    overlayList.append(image)
# print (len(overlayList))
# set default overlay image (initial tool bar)
header = overlayList[0] 

# get video input from webcam
cap = cv2.VideoCapture(0)
# set width and height (1212 x 720)
cap.set(3, 1212) 
cap.set(4, 700)   

while True:
    # import video input from webcam
    success, img = cap.read()
    # flip image so that we you draw on your right side it draws on the right side of the window as well
    img = cv2.flip(img, 1)
    # detect hand and find hand landmarks
    img = detector.handsFinder(img)
    lmList = detector.positionFinder(img, draw=False)
    
    if len(lmList) != 0:
        # print(lmList)
        
        # define index finger tip, index finger landmark is 8
        x1, y1 = lmList[8][1:]
        # define middle finger tip, middle finger landmark is 8
        x2, y2 = lmList[12][1:]

    
        # check which fingers are up
        fingers = detector.fingersUp()
        
        # SELECTION MODE
        # 2 fingers up = selection mode
        if fingers[0] and fingers[1]:
            xp, yp = 0,0
            print("SELECTION MODE")
            # check if we are at the top of the image 
            # to change header based on fingers location
            
            # if we are in the header 
            if y1 < 124:
                # selecting first color 
                if 160 < x1 < 380:
                    header = overlayList[1]
                    DrawColor = (170,58,236)
                # selecting second color
                elif 395 < x1 < 615:
                    header = overlayList[2]
                    DrawColor = (255, 0, 0)
                # selecting third color
                elif 625 < x1 < 845:
                    header = overlayList[3]
                    DrawColor = (0,238,0)
                # selecting eraser 
                elif 855 < x1 < 1075: 
                    header = overlayList[4]
                    DrawColor = (0,0,0)
            cv2.rectangle(img, (x1, y1-15), (x2, y2+35), DrawColor, cv2.FILLED)
                    
            
            
            
        # Index finger up = draw mode 
        if fingers[0] and fingers[1]==False:
            cv2.circle(img, (x1, y1), 20, DrawColor, cv2.FILLED)
            print("DRAW MODE")
            # xp and yp are the previous coordinates (set at the beginning equal to 0 by default)
            if xp == 0 and yp == 0:
                xp, yp = x1, y1
            if DrawColor == (0,0,0):
                cv2.line(img, (xp, yp), (x1, y1), DrawColor, EraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), DrawColor, EraserThickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), DrawColor, BrushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), DrawColor, BrushThickness)
            # update coordinates to draw the line 
            xp, yp = x1, y1
    
    
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInverse = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInverse = cv2.cvtColor(imgInverse, cv2.COLOR_GRAY2BGR)
    imgInverse = np.resize(imgInverse, (720, 1280, 3))
    img = np.resize(img, (720, 1280, 3))
    img = cv2.bitwise_and(img, imgInverse)  
    imgCanvas = np.resize(imgCanvas, (720, 1280, 3))  
    img = cv2.bitwise_or(img, imgCanvas)
    
    
    # setting the header image
    img[0:124, 0:1212] = header
    # crop window (idk why the margins were a bit messed up :) )
    img = img[0:700, 0:1212]
    # add and blend together webcam window and painting canvas
    # img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)
    
    cv2.imshow("Video", img)
    #cv2.imshow("Video1", imgCanvas)
    
    k = cv2.waitKey(1)
    if k == 27:
        break 







