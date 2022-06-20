import cv2

# create face cascade 
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# set video source to default webcam (at index 0)
# you can also provide a file name here , the program will read in video file BUT you have to install ffmpeg (not easy :( !)
video_capture = cv2.VideoCapture(0)

# capture video
# read() = reads one frame from video source (webcame in our case). It returns:
# actual video frame read and a return code (that tells if we run out of frames, does not matter in this case)
while True:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30, 30)
    )

    # draw rectangle around afces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    # display resulting frame
    cv2.imshow('VIDEO', frame)
    
    # click on the window and press Esc to exit
    k = cv2.waitKey(1)
    if k == 27:
        break
    

video_capture.release()
cv2.destroyAllWindows()




