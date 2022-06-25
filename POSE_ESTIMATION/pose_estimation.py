import cv2
import mediapipe as mp
import time

# create video object
cap = cv2.VideoCapture('POSE_ESTIMATION/POSE_VIDEOS/4.mp4')

# initialize mediapipe
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

# previous time
pTime = 0
# current time 
cTime = 0

while True:
    # take image input from video
    success, img = cap.read()

    # get current time 
    cTime = time.time()
    # get frames per second
    fps = 1 / (cTime - pTime)
    # set previous time as current time before calculating frames per second again 
    pTime = cTime

    # convert image from BRG to RGB as mediapipe only works with RGB images
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # identify pose in RGB image
    results = pose.process(imgRGB)
    
    # check if pose is estimated
    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            print(id, cx, cy)
            cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        
    # create text box to display frames per second 
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)   
    cv2.resizeWindow("Video", 1200, 1200)
    # display output (real-time video) to user 
    cv2.imshow("Video", img)
    # click on window and press Esc to exit
    k = cv2.waitKey(1)
    if k == 27:
        break