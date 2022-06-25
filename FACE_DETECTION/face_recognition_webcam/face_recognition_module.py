import cv2 
import time

class FaceDetector:
    # int basic parameters for face detection
    def __init__(self, faceCascade=None):
        
        self.faceCascade = faceCascade
        self.faceCascade = cv2.CascadeClassifier('FACE_DETECTION/face_recognition_webcam/haarcascade_frontalface_default.xml')
        
    
    # method to detect  from image
    def findFace(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        self.faces = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (30, 30)
        )

        # draw rectangle around faces
        for (x, y, w, h) in self.faces:
            cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
        return image 

def main():
    cap = cv2.VideoCapture(0)
    detector = FaceDetector()
    pTime = 0

    while True:
        success,image = cap.read()
        image = detector.findFace(image)
        # get current time 
        cTime = time.time()
        # get frames per second
        fps = 1 / (cTime - pTime)
        # set previous time as current time before calculating frames per second again 
        pTime = cTime
        
        # create text box to display frames per second 
        cv2.putText(image, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
        # display video to user
        cv2.imshow("Video",image)
        # click on  window and press Esc to exit
        k = cv2.waitKey(1)
        if k == 27:
            break
        
# execute main method to identify and track
if __name__ == "__main__":
    main()
    