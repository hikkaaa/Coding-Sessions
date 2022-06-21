"""
Tutorial : https://www.youtube.com/watch?v=01sAkU_NvOY
Nice explanation : https://www.section.io/engineering-education/creating-a-hand-tracking-module/

HAND TRACKING is characterized by two modules: the palm detection module and the hand landmarks.
Palm detection = works on complete image and provides a cropped image of the hand. From there, the Hand Landmarks module finds
21 different landmarks on this cropped image. To train this landmark they manually annotated 30.000 images of different hands.  
"""

# import libraries
from cgitb import handler
import cv2
import mediapipe as mp
import time

# create video object
cap = cv2.VideoCapture(0)

# we need these three objects to be able to manipulate input with mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    # take image input from webcam
    success, img = cap.read()
    # convert image from BRG to RGB as mediapipe only works with RGB images
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # identify hands in RGB image
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    # check if hand is detected 
    if results.multi_hand_landmarks:
        # for loop that enables to work with one hand per time 
        for handLms in results.multi_hand_landmarks:
            # for loop to get hand landmark information (coordinates x and y) and id of each point 
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                # use img.shape function to get height, width and channel of image 
                h, w, c = img.shape
                # get central position of hand points
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                # circle hand points detected
                cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)

            # draw hand landmarks and connections between them on image input 
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    # display output (real-time video) to user 
    cv2.imshow("Image", img)
    # click on window and press Esc to exit
    k = cv2.waitKey(1)
    if k == 27:
        break
