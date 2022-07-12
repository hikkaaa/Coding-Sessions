# import necessary libraries
import cv2
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

width = 1212
height = 700 

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
    success, img = cap.read()
    img[0:125, 0:1212] = header
    img = img[0:700, 0:1212]
    
    cv2.imshow("Video", img)
    
    k = cv2.waitKey(1)
    if k == 27:
        break 







