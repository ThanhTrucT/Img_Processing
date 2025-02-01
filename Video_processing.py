import cv2 as cv

cap = cv.VideoCapture('uit.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if ret == False:
        break
    cv.imshow("Video", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cv.release()
cv.destroyAllWindows()
