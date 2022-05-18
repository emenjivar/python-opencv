import cv2 as cv
import numpy as np

width = 500
height = 500
color_channel = 3

blank = np.zeros((width, height, color_channel), dtype='uint8')

# Change the color of canvas [Blue, Green, Red]
red = 51, 77, 225
yellow = 2, 174, 242
blue = 255, 74, 51
black = 0, 0, 0

blank[:] = 51, 77, 225

# Draw squares in each of the corners
# y region, x region
blank[0:100, 0:100] = yellow
blank[0:100, 400:500] = yellow
blank[400:500, 0:100] = yellow
blank[400:500, 400:500] = yellow

# Draw a rectangle
# (x,y)
cv.rectangle(
    img = blank, 
    pt1 = (100,150), 
    pt2 = (250, 200), 
    color = yellow,
    thickness = cv.FILLED # Also a int value
)

# Draw a scalled rentagle on the left corner to the center
cv.rectangle(
    img = blank,
    pt1 = (0,0),
    pt2 = (blank.shape[1]//2, blank.shape[0]//2),
    color = (0, 255, 0),
    thickness = 2
)

# Draw a circle
cv.circle(
    img = blank,
    center = (250, 250), # (x,y) coordinates
    radius = 100,
    color = blue,
    thickness = 2
)

# Draw a line
cv.line(
    img = blank,
    pt1 = (500, 0),
    pt2 = (255, 255),
    color = blue,
    thickness = 2,
    lineType = cv.LINE_AA
)

# Write text
cv.putText(
    img = blank,
    text = "Hello world",
    org = (100, 100),
    color = black,
    fontFace = cv.FONT_HERSHEY_SIMPLEX,
    fontScale = 1.0,
    thickness = 1
)

cv.imshow('Blank', blank)
cv.waitKey(0)
