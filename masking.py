import cv2 as cv
import numpy as np

img = cv.imread('resources/photos/cats.jpg')

# Dimentions of the mask has to be the same size as the image
blank = np.zeros(img.shape[:2], dtype='uint8')

radius = 50
mask_one = cv.circle(
        img = blank.copy(), 
        center = (170, 180), 
        radius=80, 
        color = 255, 
        thickness = -1
)
mask_two = cv.circle(blank.copy(), (350, 200), radius, 255, -1)
mask_three = cv.circle(blank.copy(), (460, 170), radius, 255, -1)

merged_mask = cv.bitwise_or(
        cv.bitwise_or(mask_one, mask_two),
        mask_three
)

masked = cv.bitwise_and(img, img, mask=merged_mask)
cv.imshow('Mask', masked)

cv.waitKey(0)
