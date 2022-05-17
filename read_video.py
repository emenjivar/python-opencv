import cv2 as cv

video = cv.VideoCapture('resources/videos/dog.mp4')

def rescale(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimentions = (width, height)
    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = video.read()

    if not isTrue:
        break;

    reescaled = rescale(frame, scale=0.5)
    cv.imshow('Video', reescaled)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break;

video.release()
cv.destroyAllWindows()
