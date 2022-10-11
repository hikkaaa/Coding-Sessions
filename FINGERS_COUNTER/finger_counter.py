# https://www.webucator.com/article/python-color-constants-module/ python color palette
# https://www.oreilly.com/library/view/mastering-opencv-4/9781789344912/16b55e96-1027-4765-85d8-ced8fa071473.xhtml opencv fonts

import cv2
import time
import os
import handtracking_module as htm 

cap = cv2.VideoCapture(0)

pTime = 0
cTime = 0

detector = htm.handTracker(detectionCon= 0.75)

# import our images
# to store them we will use os
# os.listdir to list all the elements in that directory
folderPath = "FINGERS_COUNTER\COUNT"
myList = os.listdir(folderPath)
# now overlay this image over main image
overlayList = []
# loop through our list
# for image path in list we want to download the image
for imgPath in myList:
    # here we use f strings https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/
    img = cv2.imread(f'{folderPath}/{imgPath}')
    overlayList.append(img)
print (len(overlayList))

# list of tips of each finger
tipIds = [4, 8, 12, 16, 20]

while True:
    
    success, img = cap.read()
    img = detector.handsFinder(img)
    # create a list of landmarks that we detect 
    lmList = detector.positionFinder(img)
    
    # we are trying to get the tip of our fingers and based on that tip we can state whether our fingers are open or closed
    # https://google.github.io/mediapipe/solutions/hands.html
    # we can see that the tips of our fingers are landmarks 4, 8, 12, 16, 20
    # we need to check if these are below other landmarks (for 4, check if it is above landmark 2)
    if len(lmList) != 0:
        
        # initialize a list that will indicate how many fingers are open
        fingers = []
        
        # for loop to iterate over finger tips (from index to pinky finger)
        for id in range(1,5):
        # because we are using the open cv orientation, upper means lower value 
        # [2] = we are working on the y-axis (upper or lower value)
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else: 
                fingers.append(0)
        # for the thumb it is different since the tip never goes below the other landmarks of the finger
        # the solution is to observe if the thumb tip is at the left of the below landmark
        # in this case, we would say that the thumb is closed
    
        # [1] = working on x-axis (right or left value)
        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else: 
            fingers.append(0)
            
        #print(fingers)
        
        # count how many fingers we get
        # when a finger is open = 1
        # when a finger is closed = 0
        # count number of 1's in the list of fingers
        totalFingers = fingers.count(1)
        print(totalFingers)
        
    
    
        img[0:200, 0:200] = overlayList[totalFingers]
        
        cv2.rectangle(img, (20, 225), (170, 425), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, f'{str(totalFingers)}', (45, 375), cv2.FONT_HERSHEY_DUPLEX, 6,(104,34,139), 3)
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)
    
    # display output (real-time video) to user
    cv2.imshow("Video", img)
    # click on window and press Esc to exit
    k = cv2.waitKey(1)
    if k == 27:
        break