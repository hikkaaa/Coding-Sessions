# import libraries
import cv2
import mediapipe as mp
import time

# Class that will be used for tracking
class face_meshTracker():
    # init basic parameters that make face_mesh function 
    def __init__(self, staticMode=False, maxFaces=1, refine_landmarks=False, minDetectionCon=0.5, minTrackCon=0.5):

        self.staticMode = staticMode
        self.maxFaces = maxFaces 
        self.refine_landmarks = refine_landmarks
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon
        
        # initialize mediapipe 
        
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces, self.refine_landmarks, self.minDetectionCon, self.minTrackCon)
        self.mpDraw = mp.solutions.drawing_utils
        # DrawingSpec() allows us to customize how mediapipe draws detected face landmarks 
        self.DrawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)
    
    # method to locate face mesh    
    def facemeshFinder(self, img, draw=True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS,
                        self.DrawSpec, self.DrawSpec)
                face = []
                for id,lm in enumerate(faceLms.landmark):
                #print(lm)
                    ih, iw, ic = img.shape
                    x,y = int(lm.x*iw), int(lm.y*ih)
                    # circle hand points detected
                    cv2.circle(img, (x, y), 1, (255, 0, 255), cv2.FILLED)


                    face.append([x,y])
                faces.append(face)
        return img, faces
    
# define main method to identify and track face mesh
def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    tracker = face_meshTracker(maxFaces=2)
    while True:
        success, img = cap.read()
        img, faces = tracker.facemeshFinder(img)
        if len(faces)!= 0:
            print(faces[0])
        
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
        
        cv2.imshow('Video', img)
        k = cv2.waitKey(1)
        if k == 27:
            break

# execute main method to identify and track
if __name__ == '__main__':
    main()
    
    
