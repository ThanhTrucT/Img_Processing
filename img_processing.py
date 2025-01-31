import cv2 as cv

img = cv.imread("cat.jpg", cv.IMREAD_GRAYSCALE)
cv.imshow("Cuaso1", img)

k = cv.waitKey(0) & 0xFF
if k == 27:
    cv.destroyAllWindows
elif k == ord('s'):
    cv.imwrite("Gray_img.jpg", img)
cv.destroyAllWindows
    
    
