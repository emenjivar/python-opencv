import cv2 as cv

img = cv.imread('resources/photos/cat.jpg')

def rescale(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img_rescaled = rescale(img, scale=0.5)

cv.imshow('Screenshot rescaled', img_rescaled)
cv.waitKey(0)
