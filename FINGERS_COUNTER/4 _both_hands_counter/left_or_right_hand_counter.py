# import libraries and required classes
import cv2
from cvzone.HandTrackingModule import HandDetector

# declaring HandDetector with
# some basic requirements
detector = HandDetector(maxHands=1, detectionCon=0.8)

# it detect only one hand from
# video with 0.8 detection confidence
video = cv2.VideoCapture(0)


while True:
	# Capture frame-by-frame
	success, img = video.read()
	img = cv2.flip(img, 1)
	
	# Find the hand with help of detector
	hand = detector.findHands(img, draw=False)
	fing = cv2.imread("0.png")
	if hand:
	
		# Taking the landmarks of hand
		lmlist = hand[0]
		if lmlist:
		
			# Find how many fingers are up
			# This function return list
			fingerup = detector.fingersUp(lmlist)
			
			# Change image based on different conditions
			count = fingerup.count(1)

			if count == 0:
				fing = cv2.imread("0.png")
			if count == 1:
				fing = cv2.imread("1.png")
			if count == 2:
				fing = cv2.imread("2.png")
			if count == 3:
				fing = cv2.imread("3.png")
			if count == 4:
				fing = cv2.imread("4.png")
			if count == 5:
				fing = cv2.imread("5.png")

			cv2.rectangle(img, (20, 225), (170, 425), (255, 0, 255), cv2.FILLED)
			cv2.putText(img, f'{str(count)}', (45, 375), cv2.FONT_HERSHEY_DUPLEX, 6,(104,34,139), 3)
    

	
	# Place the image in main frame
	img[0:200, 0:200] = fing
	# Display the resulting frame
	cv2.imshow("Video", img)
	# click on window and press Esc to exit
	k = cv2.waitKey(1)
	if k == 27:
		break




