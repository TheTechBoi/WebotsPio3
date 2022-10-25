"""mahmut_takip controller."""

#Kameralı robot

from controller import Robot, Camera, Motor, Keyboard
import cv2
import numpy as np

robot = Robot()

timestep = int(robot.getBasicTimeStep())

kP_angle = 0.01
kP_distance = 0.16

keyboard = Keyboard()
keyboard.enable(timestep)

cam = robot.getDevice('CAM')
cam.enable(timestep)

camMotor = robot.getDevice('CAM_motor')
camMotor.setPosition(float('inf'))
camMotor.setVelocity(0.0)

leftMotor = robot.getDevice('left wheel')
rightMotor = robot.getDevice('right wheel')

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0)
rightMotor.setVelocity(0)

lSpeed = 0.0
rSpeed = 0.0    

lastRadiusError = 0.0

def camBallAlligner():
    
    img = cam.getImageArray()
    img = np.asarray(img, dtype=np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    img = cv2.flip(img, 1)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(img, np.array([50, 200, 46]), np.array([100, 255, 255]))
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    largest_contour = max(contours, key=cv2.contourArea)
    largest_contour_center = cv2.moments(largest_contour)
    center_x = int(largest_contour_center['m10'] / largest_contour_center['m00'])

    ((x, y), radius) = cv2.minEnclosingCircle(largest_contour) 

    angleError = cam.getWidth() / 2 - center_x
    radiusError = 180 - radius
    
    forwardSpeed = (radiusError * kP_distance)
    turnSpeed   = (angleError * kP_angle)
    
    lSpeed = forwardSpeed - turnSpeed
    rSpeed = forwardSpeed + turnSpeed
    
    if(lSpeed >= 12.3):
        lSpeed = 12.3
        
    elif(lSpeed <= -12.3):
        lSpeed = -12.3
        
        
    if(rSpeed >= 12.3):
        rSpeed = 12.3
     
    elif(rSpeed <= -12.3):
        rSpeed <= -12.3
        
        
    leftMotor.setVelocity(lSpeed)
    rightMotor.setVelocity(rSpeed)
        

def camKeyboardControl():

    key = keyboard.getKey() #<314 >316
    
    if(key==314):
        camMotor.setVelocity(1)
    elif(key==316):
        camMotor.setVelocity(-1)
    else:
        camMotor.setVelocity(0.0)

while robot.step(timestep) != -1:

    #camKeyboardControl()
        
    camBallAlligner()
    
    #cv2.imshow("preview", mask)
    #cv2.waitKey(timestep)