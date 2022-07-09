import cv2
import mediapipe as mp
import math
import time 

# class that will be used for detecting
class PoseDetector:
    # int basic parameters that make pose function 
    def __init__(self, mode=False, upBody=False, smooth=True, DetectionCon=0.5, TrackCon=0.5):
        # put self before each parameter to allow access to method and attributes
        # and to allow each object to posses itw own methods and attributes
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.DetectionCon = DetectionCon
        self.TrackCon = TrackCon
        
        # parameters for mediapipe initialization
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self, self.mode, self.upBody, 
                                    self.smooth, self.DetectionCon, self.TrackCon)
        self.mpDraw = mp.solutions.drawing_utils
    
    # method to locate pose    
    def findPose(self, image, draw=True):
        # convert image from BRG to RGB as mediapipe only works with RGB images
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # identify pose in RGB image
        self.results = self.pose.process(imageRGB)
        
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(image, self.results.pose_landmarks,
                                        self.mpPose.POSE_CONNECTIONS)
        return image
    
    # method to find x and y coordinates of each pose_landmarks
    def positionFinder(self, image, draw):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy]) 
            if draw == True:  
                cv2.circle(image, (cx, cy), 10, (255, 0, 255), cv2.FILLED)            
                self.mpDraw.draw_landmarks(image, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        
        return self.lmList 
    # method to calculate angle 
    def findAngle(self, img, p1, p2, p3, draw=True):
        # Get the landmarks
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]
        # Calculate the Angle
        # math.atan2() = return the arc tangent of y/x in radians
        # math.degrees() = converts randians in degrees
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                            math.atan2(y1 - y2, x1 - x2))
        
        if angle < 0:
            angle += 360
        # print(angle)
        # Draw
        # draw angle in image 
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
            cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        return angle

def main():
    cap = cv2.VideoCapture(0)
    detector = PoseDetector()
    pTime = 0

    while True:
        success,image = cap.read()
        image = detector.findPose(image)
        lmList = detector.positionFinder(image, draw=True)
        if len(lmList) != 0:
            print(lmList)
        
        # cv2.namedWindow("Video", cv2.WINDOW_NORMAL)   
        # cv2.resizeWindow("Video", 1200, 1200)
        
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