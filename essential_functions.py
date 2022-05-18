import cv2 as cv

img = cv.imread('resources/photos/park.jpg')

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray scale', gray)

# Blur
blur = cv.GaussianBlur(
    src = img, 
    ksize = (3,3), # Increate this values to increate the blur 
    sigmaX = cv.BORDER_DEFAULT
)
cv.imshow('Blur', blur)

# Edge cascade
canny = cv.Canny(
    image = blur,
    threshold1 = 125,
    threshold2 = 175
)
cv.imshow('Image edges', canny)

# Dilating the image
# i'm not pretty sure about the usefulness of thi function
# just let's follow the tutorial by now
dilated = cv.dilate(
    src = canny,
    kernel = (7,7),
    iterations = 3
)
cv.imshow('Dilated image', dilated)

# Eroding the image
# I guess this revert dilate action
# Displaying almost the exact canny image
eroded = cv.erode(
    src = dilated,
    kernel = (7,7),
    iterations = 3
)
cv.imshow('Eroded image', eroded)

# Resize image
resized = cv.resize(
        src = img, 
        dsize = (500, 500), 
        interpolation = cv.INTER_AREA
)
cv.imshow('Resized image', resized)

# Cropping, don't need cv method
cropped = img[50:200, 200:400]
cv.imshow('Cropped image', cropped)

cv.waitKey(0)
