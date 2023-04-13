# Face-Recognition-Gender-and-Age-Prediction-App
This project consists of a Python script that analyzes an image and extracts the age, gender, and emotion of a person, and a real-time face verification system that checks if the person in front of a webcam matches the one in the uploaded image. The purpose of this system is to assist police and surveillance operations by quickly identifying potential suspects or persons of interest.

Requirements:
The following libraries must be installed to run the system:

OpenCV (pip install opencv-python)
Pandas (pip install pandas)
DeepFace (pip install deepface)

Usage:
Insert an image in the project folder, change the name of the image with "img.jpg" or change the image name in the code.
Run the Python script "facial_recognition.py".
The script will output the age, gender, and emotion of the person in the uploaded image, and display the real-time face verification system.
When a person is in front of the webcam, the system will display "MATCH!" if the person matches the uploaded image, or "NO MATCH!" otherwise.
Press "q" to exit the real-time face verification system.

Possible improvements:
Add support for multiple uploaded images.
Implement a database to store a list of known suspects and persons of interest.
Integrate the system with a notification system to alert authorities when a match is found.
