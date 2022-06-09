import cv2 as cv
import numpy as np

img = cv.imread('resources/photos/cats.jpg')

# Dimentions of the mask has to be the same size as the image
blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] //2), 100, 255, -1)
masked = cv.bitwise_and(img, img, mask=mask)

cv.imshow('Mask', masked)

cv.waitKey(0)
