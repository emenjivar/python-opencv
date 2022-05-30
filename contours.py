import cv2 as cv
import numpy as np

img = cv.imread('resources/photos/cats.jpg')

# Process image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)

# Process image using the simplest and new method
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

# contours is a list with the corner ot the contours
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# Draw contours
blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)

print(len(contours))

cv.imshow('Cats', thresh)
cv.imshow('Contours', blank)
cv.waitKey(0)
