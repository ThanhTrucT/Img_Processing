import cv2 as cv
import numpy as np 
from math import sqrt
from random import seed, randint 


def kc(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return round(sqrt((x1-x2)**2 + (y1-y2)**2))

def draw_red_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        center = (250,250)
        radius = kc(center, (x,y))
        color = (0, 0, 255)
        cv.circle(img, center, radius, color, 4)
        
def draw_color_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        seed()
        center = (randint(0,499), randint(0,499))
        radius = kc(center, (x,y))
        color = (randint(0,255), randint(0,255), randint(0,255))
        cv.circle(img, center, radius, color, 4)
    
    
img = np.zeros((500, 500, 3), np.uint8)
cv.namedWindow("img_red")
cv.namedWindow("img_color")
cv.setMouseCallback("img_color", draw_color_circle)
cv.setMouseCallback("img_red", draw_red_circle)

while True:
    cv.imshow("img_red", img)
    cv.imshow("img_color", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cv.destroyAllWindows()