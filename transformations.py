import cv2 as cv
import numpy as np

img = cv.imread('resources/photos/park.jpg')

# Param x: + value move to right, - value move to left
# Param y: + value move to up, - value move to down
def translate(img, x, y):
    transMatrix = np.float32([
        [1,0,x],
        [0,1,y]
    ])
    
    width = img.shape[1]
    height = img.shape[0]
    dimentions = (width, height)
    return cv.warpAffine(
        src = img,
        M = transMatrix,
        dsize = dimentions
    )

translated_image = translate(img, 100, 100)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        # Rotate from the center
        rotPoint = (width//2, height//2)
    
    rotMatrix = cv.getRotationMatrix2D(
        center = rotPoint,
        angle = angle,
        scale = 1.0
    )
    dimentions = (width, height)
    return cv.warpAffine(
        src = img,
        M = rotMatrix,
        dsize = dimentions
    )

rotated_image = rotate(translated_image, 45)

# Flip image
flipCode = 0 # 0 -> vertical, 1 horizontal, -1 vertical and horizontal
flip = cv.flip(
    src = img,
    flipCode = flipCode
)

cv.imshow('Translated image', translated_image)
cv.imshow('Rotated image', rotated_image)
cv.imshow('Flipped image', flip)

cv.waitKey(0)
