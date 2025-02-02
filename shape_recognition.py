import cv2 as cv
import numpy as np 

frame = cv.imread("1.png", 1)
img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

thres = cv.threshold(img, 0, 255, cv.THRESH_BINARY)

contours = cv.findContours(thres, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#for cnt in contours:
