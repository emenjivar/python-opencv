# We smoth an image when it has a lot of noise
# caused by light problems or another causes

import cv2 as cv

img = cv.imread('resources/photos/cats.jpg')

# Average
average = cv.blur(img, (5,5))
cv.imshow('Average', average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (5,5), 0)
cv.imshow('Gauss', gauss)

# Median
# It's the same as average, but find the median of surroinding pixels
# It's more efective introducing noise than gauss
median = cv.medianBlur(img, 5)
cv.imshow('Median', median)

# Bilateral
# Is the most efective blurring 
# This method apply bluring and retain edges
bilateral = cv.bilateralFilter(img, 5, sigmaColor = 30, sigmaSpace = 30)
cv.imshow('Bilateral', bilateral)

cv.imshow('Cats', img)

cv.waitKey(0)
