"""
Tutorial : https://www.youtube.com/watch?v=01sAkU_NvOY
Nice explanation : https://www.section.io/engineering-education/creating-a-hand-tracking-module/
Documentation for mediapipe: https://google.github.io/mediapipe/solutions/hands.html
"""
import cv2
import mediapipe as mp

# class that will be used for tracking
class handTracker():
    # init basic parameters that make hands function (look at mediapipe documentation above) work
    def __init__(self, mode=False, maxHands=4, detectionCon=0.5,modelComplexity=1,trackCon=0.5):
        # put self before each parameter to allow access to methods and attributes  and to allow each object
        # to possess its own methods and attributes
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        # parameters for mediapipe initialization
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
    
    # method to locate hands
    def handsFinder(self,image,draw=True):
        # convert image from BRG to RGB as mediapipe only works with RGB images
        imageRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        # identify hands in RGB image
        self.results = self.hands.process(imageRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
        return image
    
    # method to find x and y coordinates of each of the 21 hand landmarks
    def positionFinder(self,image, draw=True):
        self.lmlist = []
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                        h,w,c = image.shape
                        cx,cy = int(lm.x*w), int(lm.y*h)
                        if draw == True:
                            cv2.circle(image,(cx,cy), 5, (255,0,255), cv2.FILLED)
                        self.lmlist.append([id,cx,cy])
            

        return self.lmlist
    
    def fingersUp(self):
        # initialize a list that will indicate how many fingers are open
        fingers = []
        
        # for loop to iterate over finger tips (from index to pinky finger)
        for id in range(1,5):
        # because we are using the open cv orientation, upper means lower value 
        # [2] = we are working on the y-axis (upper or lower value)
            if self.lmlist[self.tipIds[id]][2] < self.lmlist[self.tipIds[id]-2][2]:
                fingers.append(1)
            else: 
                fingers.append(0)
                
        # for the thumb it is different since the tip never goes below the other landmarks of the finger
        # the solution is to observe if the thumb tip is at the left of the below landmark
        # in this case, we would say that the thumb is closed
        # [1] = working on x-axis (right or left value)
        if self.lmlist[self.tipIds[0]][1] < self.lmlist[self.tipIds[0]-1][1]:
            fingers.append(1)
        else: 
            fingers.append(0)
            
        return fingers 
        
# define main method to identify and track hands
def main():
    cap = cv2.VideoCapture(0)
    tracker = handTracker()

    while True:
        success,image = cap.read()
        image = tracker.handsFinder(image)
        lmList = tracker.positionFinder(image)
        if len(lmList) != 0:
            print(lmList)
        
        cv2.namedWindow("Video", cv2.WINDOW_NORMAL)   
        cv2.resizeWindow("Video", 1800, 1000)

        cv2.imshow("Video",image)
        k = cv2.waitKey(1)
        if k == 27:
            break

# execute main method to identify and track
if __name__ == "__main__":
    main()
    
    