import cv2

img = cv2.imread("Resources/bmw.jpg")
print(img.shape)

imgr = cv2.resize(img,(700,600))

imgcropped = img[0:200,200:500]
#cv2.imshow("img",img)
cv2.imshow("img r",imgr)
cv2.imshow("img crop",imgcropped)
cv2.waitKey(0)