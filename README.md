# Vehicle Detection of Specific Color with Haar Cascades

### It does not simply recognize the vehicle but recognizes and shows the vehicle of a specific color.

### The reason why we made this program:
When watching the movie, there is a scene where the suspect flees in a car.
At this time, we can see a scene in which the vehicle is inquired and tracked through the CCTV on the road.
After watching these scenes, we thought about creating a program that can detect a specific vehicle.
Of course, the program we made is being used in a more advanced form, still, it was meaningful to make a program based on what we learned during the semester.


### Requirements
1. python (3.7.4)
2. numpy (1.21.6)
3. opencv (4.6.0)
4. cars.xml

### File
python rosa.py

### How to Run It?
If you press any button except the ESC key, the video plays.
If you want to stop running the program, you can press ESC key.

### Result and Limitation

##### Result
When you run the program, it prints two different videos.
The first video called RESULT recognizes the car and show it through a rectangle.
Another image called RED detects and outputs only red in the original image.

##### Limitation
There were some slight deviations in the process of recognizing the vehicle in the original image.
In addition, even in the process of detecting only red in the image, not only red in the vehicle was detected, but all red in the image was detected.
