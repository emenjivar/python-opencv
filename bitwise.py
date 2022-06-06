import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(
    img = blank.copy(),
    pt1 = (30, 30),
    pt2 = (370, 370),
    color = 255, # White
    thickness = -1 # Fill
)

circle = cv.circle(
    img = blank.copy(),
    center = (200, 200),
    radius = 200,
    color = 255,
    thickness = -1
)

# bitwise AND 
# This is the intersection of the two images
bitwise_and = cv.bitwise_and(rectangle, circle)

# bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)

# bitwise XOR
# Not intersecting region
bitwise_xor = cv.bitwise_xor(rectangle, circle)

# bitwise NOT
# invert binary color
bitwise_not = cv.bitwise_not(bitwise_and)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)
cv.imshow('Bitwise and', bitwise_and)
cv.imshow('Bitwite or', bitwise_or)
cv.imshow('Bitwise xor', bitwise_xor)
cv.imshow('Bitwise not', bitwise_not)

cv.waitKey(0)
