import cv2 as cv 

cap = cv.VideoCapture(1)

while True:
    ret, frame = cap.read()
    width = cap.get(3)
    height = cap.get(4)
    gray = cv.cvtColor(frame, cv.COLOR_BAYER_BG2BGR)
    
    cv.imshow("Camerawebcam", gray)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()
