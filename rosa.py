import cv2 as cv
import numpy as np

cascade_src = 'cars.xml'
cap=cv.VideoCapture('cartest.mp4')
retval, frame=cap.read()
car_cascade = cv.CascadeClassifier(cascade_src)
frame=cv.resize(frame,None,fx=0.3,fy=0.3,interpolation=cv.INTER_AREA)

while True:
    retval, frame=cap.read()
    if not retval:
        break

    # Resize the frame
    frame=cv.resize(frame,None,fx=0.3,fy=0.3,interpolation=cv.INTER_AREA)
    
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    # Define lower and uppper limits of red
    lower_red=np.array([150, 50, 50])
    upper_red=np.array([180, 255, 255])

    # Mask image to only select reds
    mask=cv.inRange(hsv,lower_red,upper_red)

    res = cv.bitwise_and(frame, frame, mask=mask)

    # Show only red in the image
    cv.imshow("RED", res)
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    
    # Mark the car through rectangle
    for (x,y,w,h) in cars:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    # Change image where we found red
    cv.imshow("RESULT",frame)

    key=cv.waitKey(0)
    if key==27:
        break

if cap.isOpened():
    cap.release()
    
cv.destroyAllWindows()
