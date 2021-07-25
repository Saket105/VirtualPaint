import cv2
print("package imported")

################read image###################

# img = cv2.imread("Resources/lena.png")
#
# cv2.imshow("Output",img)
# cv2.waitKey(0)

################read image###################


################ read web cam ###############

cap = cv2.VideoCapture(0)
cap.set(0,640)
cap.set(1,480)
cap.set(10,10)
while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

################ read web cam ###############


################ read video ###############

# frameWidth = 640
# frameHeight = 480
#
# cap = cv2.VideoCapture("Resources/test_video.mp4")
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

################ read video ###############