import cv2 as cv
import numpy as np 

img = np.zeros((600, 600, 3), np.uint8)

#Ve duong thang 
img = cv.line(img, (300,0), (300, 600), (255, 0, 0), cv.LINE_AA)


#Ve duong tron
img = cv.circle(img, (300,300), 100, (0,255,0), 3)

#Ve hinh chu nhat 
img = cv.rectangle(img, (0, 150), (100, 450), (0, 0, 255), 4)
img = cv.rectangle(img, (500, 150), (600, 450), (0, 250, 0), 4)

#Ve hinh elip
img = cv.ellipse(img, (200, 200), (50, 25), 45, 0, 360, (0,255,255),4)

#Ve hinh da giac 
pts = np.array([[0,300], [200, 200], [350, 400], [360, 500],[30, 300]], np.int32)
img = cv.polylines(img, [pts], False, (255,255,255), 4)

#Them text vao anh 
img = cv.putText(img, "Hereeven", (10, 150), cv.FONT_HERSHEY_SIMPLEX, 5, (255,255,0))
cv.imshow("Anh", img)

cv.waitKey(0)
cv.destroyAllWindows()
