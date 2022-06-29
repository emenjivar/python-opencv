# This script has a purpose detekt when camera light is on
# This works really great in low light enviroments
# But when there is a lot of natural light, the script tends to get confused
import cv2 as cv
import numpy as np

def put_text(img, text, coordinates,color):
    cv.putText(
        img=img,
        text=text,
        org=coordinates,
        color=color,
        fontFace=cv.FONT_HERSHEY_SIMPLEX,
        fontScale=0.4,
        thickness=1
    )

def put_data_text(
    img, 
    dark, 
    light, 
    delta, 
    width,
    height,
    color=(255,255,255)
):
    x_coordinate = 10
    fixed_y_coordinate = height - 10
    cv.rectangle(
            img=img,
            pt1=(0, height-30),
            pt2=(width, height),
            color=(0,0,0),
            thickness=-1
    )

    label_light = "On" if light != 0.0 else "Off"

    put_text(
        img = img,
        text=f'Light {label_light}',
        coordinates=(x_coordinate, fixed_y_coordinate),
        color=color
    )

    x_coordinate += 100
    put_text(
        img = img, 
        text=f'Light: {light}',
        coordinates=(x_coordinate, fixed_y_coordinate),
        color=color
    )

    x_coordinate += 150
    put_text(
        img = img, 
        text=f'Dark: {dark}',
        coordinates=(x_coordinate, fixed_y_coordinate),
        color=color
    )

    x_coordinate += 150
    put_text(
        img = img, 
        text=f'Delta: {delta}',
        coordinates=(x_coordinate, fixed_y_coordinate),
        color=color
    )   

middle = 128
vid = cv.VideoCapture(0)

first_frame = True
height=0
width=0
historical_delta = 0
light_color = (0,255,0) # Green

while(True):

    ret, frame = vid.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_smoth = cv.blur(frame_gray, (11,11), 0)

    ret, frame_threshold = cv.threshold(
        src=frame_smoth, 
        thresh=250, 
        maxval=255, 
        type=cv.THRESH_BINARY
    )

    hist = cv.calcHist(
        images=[frame_threshold],
        channels=[0],
        mask=None,
        # Number of bins user for compute the histogram
        histSize=[256],
        ranges=[0,256]
    )

    displayed_frame = frame_threshold
    
    # threshold histogram store black/white pixels
    # that is why i access the first and last element of the array (0=black, 255=white)
    dark = hist[0][0]
    light = hist[255][0]
    delta = light - dark

    if (first_frame):
        height,width = frame.shape[:2]
        first_frame = False

    # Debug frame text
    put_data_text(
        img = displayed_frame,
        dark=dark,
        light=light,
        delta=delta,
        width=width,
        height=height
    )
    # Final output colors
    put_data_text(
        img = frame,
        dark=dark,
        light=light,
        delta=delta,
        width=width,
        height=height,
        color=light_color
    )

    cv.imshow('Frame', frame)
    cv.imshow('Final output', displayed_frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break;

vid.release()
cv.destroyAllWindows()
