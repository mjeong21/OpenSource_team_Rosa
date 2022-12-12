import cv2
import numpy as np

cascade_src = 'cars.xml'
cap=cv2.VideoCapture('cartest.mp4')
# recognize the car
car_cascade = cv2.CascadeClassifier(cascade_src)
retval, frame=cap.read()

while True:
 
    if (type(frame) == type(None)):
        break
    if not retval:
        break

    # resize the frame
    frame=cv2.resize(frame,None,fx=0.3,fy=0.3,interpolation=cv2.INTER_AREA)
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # Define lower and uppper limits of red
    lower_red=np.array([150, 50, 50])
    upper_red=np.array([180, 255, 255])

    # Mask image to only select reds
    mask=cv2.inRange(hsv,lower_red,upper_red)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # mark the car through rectangle
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    # show only red in the image
    cv2.imshow("RESULT",frame)
    
    # Change image where we found red
    cv2.imshow("RED", res)

    key=cv2.waitKey(0)

    if key==27:
        break

 
if cap.isOpened():
    cap.release()
    
cv2.destroyAllWindows()
