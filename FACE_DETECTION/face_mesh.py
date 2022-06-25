# Tutorial : https://www.youtube.com/watch?v=01sAkU_NvOY

# import libraries
import cv2
import mediapipe as mp
import time

# create video object
cap = cv2.VideoCapture(0)

# initialize mediapipe
# draw detected face landmarks on image 
mpDraw = mp.solutions.drawing_utils
# DrawingSpec() allows us to customize how mediapipe draws detected face landmarks 
DrawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=3)

pTime = 0
cTime = 0

while True:
    # take image input from webcam
    success, img = cap.read()
    # convert image from BRG to RGB as mediapipe only works with RGB images
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # identify face mesh in RGB image
    results = faceMesh.process(imgRGB)
    
    # check if face mesh is detected
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            # if you find tutorials where they use mpFaceMesh.FACE_CONNECTIONS
            # be aware that the latest python version uses mpFaceMesh.FACEMESH_CONTOURS
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS, 
                                DrawSpec, DrawSpec)
            # for loop to get hand landmark information (coordinates x and y) and id of each point
            for id, lm in enumerate(faceLms.landmark):
                # use img() function to get height, width and channel of image
                h, w, c = img.shape
                # get central position points
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                # circle hand points detected
                cv2.circle(img, (cx, cy), 1, (255, 0, 255), cv2.FILLED)
                    
            
    
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