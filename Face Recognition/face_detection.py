'''
For this code, I followed the tutorial at this link : https://realpython.com/face-recognition-with-python/

We are going to work with two elements, the OpenCV library and cascades. 
*OpenCV* is the the most famous library for computer vision and uses machine learning algorithms to perform face detection within an image. 
*Cascades* are XML files containing OpenCV data used to detect objects (face, hands, legs, non-human stuff, like a banana). 

'''

import cv2
import sys

# pass the image cascade names as command-line arguments 
imagePath = sys.argv[1]
cascPath = sys.argv[2] #"haarcascade_frontalface_default.xml"

# create Haar Cascade, an object detection algorithm used to identify faces in an image or a real time video.
# source : https://towardsdatascience.com/face-detection-with-haar-cascade-727f68dafd08
faceCascade = cv2.CascadeClassifier(cascPath)

# read image
image = cv2.imread(imagePath)
# convert imgae in grayscale to perform operations
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in image
# detectMultiScale = general function for object detection. It detects faces as we are calling it on the face cascade.
# grayscale image = first option
# scale factor = to compensate faces' different distances from camera
# detection algorithm = uses a moving window to detect objects
# minNeighbors = how many objects are detected near the current one (before it declares the face found)
# minSize = size of each window 
faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(30,30)) #flags=cv2.cv.CV_HAAR_SCALE_IMAGE

# expected output function = list of rectangles in which it believes it found a face
print ("found {0}.faces!".format(len(faces)))

# Draw rectangle around detected faces
# x, y = location of rectangle
# w, h = rectangle width and height
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)

# display image
# wait for user to press a key
cv2.imshow("Faces found", image)
cv2.waitKey(0)