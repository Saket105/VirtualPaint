import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[200:300,150:300] = 255,255,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(150,230,0),2)

#for normal rectangle
#cv2.rectangle(img,(0,0),(250,250),(0,0,255),2)

#for filled rectangle
#cv2.rectangle(img,(0,0),(250,250),(0,0,255),cv2.FILLED)

#for circle
cv2.circle(img,(180,180),35,(0,125,180),cv2.FILLED)

#for text
cv2.putText(img,"Hello",(250,250),cv2.FONT_HERSHEY_TRIPLEX,1,(130,125,180),2)

cv2.imshow("img",img)
cv2.waitKey(0)
