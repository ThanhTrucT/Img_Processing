import cv2 as cv
import numpy as np 

img = np.zeros((300, 400, 3),np.uint8)
cv.namedWindow('image')

def donothing(x):
    pass
#Tao thanh keo 
cv.createTrackbar('B', "image", 0,255, donothing)
cv.createTrackbar('G', "image", 0,255, donothing)
cv.createTrackbar('R', "image", 0,255, donothing)

cv.createTrackbar('EN', 'image', 0, 1, donothing)
while True:
    cv.imshow("Image", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
    b = cv.getTrackbarPos('B', "image")
    g = cv.getTrackbarPos('G', "image")
    r = cv.getTrackbarPos('R', "image")
    en = cv.getTrackbarPos('EN', "image")
    if en == 1:
        img[:] = [b, g, r]
    else:
        img[:] = 0
cv.destroyAllWindows()