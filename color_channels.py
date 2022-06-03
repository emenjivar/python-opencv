import cv2 as cv
import numpy as np

img = cv.imread('resources/photos/park.jpg')
# cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# Split image in blue, green and red color spaces
b,g,r = cv.split(img)
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

# If I display [b, g or r], the output will be on grayscale
# Blank color meains hight concentration of the color
# Dark color means low concentration of the color
# But, we can change the output and print instead, 
# An image with the respective chanel color, i mean, not it gray scale
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

# Merge the channels
# The output is exactly the same original image
merge = cv.merge([b, g, r])
cv.imshow('Merged channels', merge)

cv.waitKey(0)
