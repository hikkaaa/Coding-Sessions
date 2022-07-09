# import necessary libraries
# https://google.github.io/mediapipe/solutions/pose.html useful to see landmarks' numbers 
import cv2
import numpy as np
import pose_estimation_module as pem

# create video object
cap = cv2.VideoCapture(0)
detector = pem.PoseDetector(DetectionCon=0.4)

# this variable stores number of curls
count = 0
# direction 0 = up (from 0% to 100%)
# direction 1 = down (from 100% to 0%)
# complete curl = from 0% to 100% and from 100% to 0% 
# complete curl --> count += 1 
dir = 0

while True:
    # take image input from video
    success, img = cap.read()
    # img = cv2.resize(img, (900, 1280))
    # find pose
    img = detector.findPose(img, False)
    # get landmarks list 
    lmList = detector.positionFinder(img, False)
    
    # we need to calculate the angle between the landmarks relevant to perform curls
    # these landmarks are: [11, 13, 15] for left arm and [12, 14, 16] for right arm
    if lmList != 0:
        angle_right = detector.findAngle(img, 12, 14, 16)
        # angle_left = detector.findAngle(img, 11, 13, 15)
        
        per_right = np.interp(angle_right, (200, 330), (0, 100))
        # per_left = np.interp(angle_left, (200, 330), (0, 100))
        print(angle_right, per_right)
        
        # check for dumbbell curls 
        if per_right == 100:
            # if we are going up 
            if dir == 0:
                count += 0.5
                dir = 1
        if per_right == 0:
            # if we are going down
            if dir == 1:
                count += 0.5 
                dir = 0 
        
        #print(count)
        cv2.putText(img, str(int(count)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 255), 5)
        
        
    
    
    cv2.imshow("Video",img)
    k =cv2.waitKey(1)
    if k == 27:
        break 
    
    



