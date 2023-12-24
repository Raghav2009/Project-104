import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(20,120),cv2.FONT_HERSHEY_PLAIN,4,(0,255,0),2)
cv2.putText(img,"Mercury",(85,240),cv2.FONT_HERSHEY_PLAIN,1.5,(225,205,0),2)
cv2.putText(img,"Venus",(175,190),cv2.FONT_HERSHEY_PLAIN,1.25,(0,205,100),2)
cv2.putText(img,"Earth",(265,240),cv2.FONT_HERSHEY_PLAIN,1.15,(25,25,225),2)
cv2.putText(img,"Mars",(355,190),cv2.FONT_HERSHEY_PLAIN,1.28,(0,225,225),2)
cv2.putText(img,"Jupiter",(475,240),cv2.FONT_HERSHEY_PLAIN,1.6,(255,0,24),2)
cv2.putText(img,"Saturn",(685,190),cv2.FONT_HERSHEY_PLAIN,1.6,(150,200,0),2)
cv2.putText(img,"Uranus",(965,240),cv2.FONT_HERSHEY_PLAIN,1.7,(140,0,140),2)
cv2.putText(img,"Neptune",(1150,190),cv2.FONT_HERSHEY_PLAIN,1.7,(0,255,0),2)

cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.imwrite("solar-system.jpg",img)