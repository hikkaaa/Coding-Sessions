import cv2
import time
import os

cap = cv2.VideoCapture(0)

# import our images
# to store them we will use os
# os.listdir to list all the elements in that directory
folderPath = "COUNT"
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

while True:
    
    success, img = cap.read()
    
    img[0:200, 0:200] = overlayList[0]
    
    # display output (real-time video) to user
    cv2.imshow("Video", img)
    # click on window and press Esc to exit
    k = cv2.waitKey(1)
    if k == 27:
        break