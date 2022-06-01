import cv2 as cv

img = cv.imread('resources/photos/park.jpg')

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray scale', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV scale', hsv)

# BRG to lab
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB  scale', lab)

cv.waitKey(0)
