"""superviser_code controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Supervisor

# create the Robot instance.
robot = Supervisor()

# get the time step of the current world.
timestep = int(32)

xOffset = -0.05
yOffset = 0.0
zOffset = 0.29

p3Node = robot.getFromDef('P3')
p3Translation = p3Node.getField('translation')

GBallNode = robot.getFromDef('GBall')
GBallTranslation = GBallNode.getField('translation')

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    p3Loc = p3Translation.getSFVec3f()
    
    ballX = xOffset + p3Loc[0]
    ballY = yOffset + p3Loc[1]
    ballZ = zOffset + p3Loc[2]
    
    GBallTranslation.setSFVec3f([ballX, ballY, ballZ])
    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)

# Enter here exit cleanup code.
