# Automatic-Door-Lock-System-Using-Face-Recognition

* The project has been made to make door more protective.

* User can use their face to unlock the door

* It can be used smoothly

* The code has been made using Python language and C Language in Arduino

* Arduino has been used for show the Demo of the Door.

<h1>REQUIRED COMPONENT</h1>
1.ARDUINO UNO

![Logo](https://github.com/Thamaraiselvan942/Face-Recognition-Using-Door-Lock-System/blob/main/Components%20used/1.jpeg)

2.SERVO MOTOR

![Logo](https://github.com/Thamaraiselvan942/Face-Recognition-Using-Door-Lock-System/blob/main/Components%20used/2.jpg)


<h1>REQUIRED LIBRARAY</h1>

1.Open-Cv

2.Pyserial

3.Pyttsx3

4.numpy

**CIRCUIT DIAGRAM**

* The circuit Diagram is given below .The Servo Motor Signal Pin will be Connected to the arduino Pwm Pin Number 9.
    The 5V pin will be connected to Arduino 5v pin and Ground pin will be connected to Arduino Ground pin.
    Arduino must be connected to Pc through arduino Cable. 
   
   ![Logo](/circuitdiagram.JPG)
 **FUNCTIONAL PREVIEW**
 
 * At first the python code will be write on any of the python IDE than arduino code will be uploaded to arduino Uno board using 
 arduino IDE and then Run the  1st python code it will collect the sample pictures and then run 2nd code  and it will start the webcam and take pictures , if the picture match with database upto 83% then it will send a character to the arduino through serial communication and arduino will move the servo motor for 5 seconds based on the character found.


