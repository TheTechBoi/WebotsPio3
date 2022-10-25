"""mahmut_klavye_kontrol controller."""

#Yeşil küreli robot

from controller import Robot, Keyboard, Motor

robot = Robot()
keyboard = Keyboard()

timestep = int(robot.getBasicTimeStep())

keyboard.enable(timestep)

leftMotor = robot.getDevice('left wheel')
rightMotor = robot.getDevice('right wheel')

leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0)
rightMotor.setVelocity(0)

lSpeed = 0.0
rSpeed = 0.0

dSpeed = 1

isAuto = False

so = []
soValues = []
soNames = [
    'so0', 'so1', 'so2', 'so3',
    'so4', 'so5', 'so6', 'so7',
    'so8', 'so9', 'so10', 'so11',
    'so12', 'so13', 'so14', 'so15'
]

for i in range(16):
    so.append(robot.getDevice(soNames[i]))
    so[i].enable(timestep)
   

#w87 a65 s83 d68

def tele(key):
    if(key==87):
        lSpeed = dSpeed
        rSpeed = dSpeed
    elif(key==65):
        lSpeed = -dSpeed
        rSpeed = dSpeed
    elif(key==83):
        lSpeed = -dSpeed
        rSpeed = -dSpeed
    elif(key==68):
        lSpeed = dSpeed
        rSpeed = -dSpeed
    else:
        lSpeed = 0
        rSpeed = 0
            
    leftMotor.setVelocity(lSpeed)
    rightMotor.setVelocity(rSpeed)
    
def auto():
    pass

lastKey = 0

while robot.step(timestep) != -1:
    key = keyboard.getKey()
    #print(key)
    
    if(key==67!=lastKey): #67 -> c     
        isAuto = not isAuto

    if(isAuto):
        auto()
    else:
        tele(key)
        
    lastKey = key

