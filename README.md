##Glow LED using Face Detection
###using Python, Open CV and Arduino

A nice but simple set up to turn an LED on or off depending on whether a face is detected in the webcam by interfacing an Arduino with the computer via serial communication

To summarise, the following happens
* Python program constantly captures images from webcam
* Converts image to black and white for easier computations
* Displays image on screen - giving effect of live webcam stream
* Haar detection done using OpenCV Haar Classifier - Draws rectange around face if detected
* If detected, also send some text via serial port
* Meanwhile Arduino is reading serial port - when message received, turns LED off... On if no message received
