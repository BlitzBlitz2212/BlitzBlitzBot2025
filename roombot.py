from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

#wheels
right_wheel = Motor(Port.A)
left_wheel = Motor(Port.E, Direction.COUNTERCLOCKWISE)
roombot = DriveBase(left_wheel, right_wheel, 62.4, 108)

#bearing
bear = Motor(Port.C, gears=[12, 140])

#active arm
arm = Motor(Port.D)

#color sensor
sensor = ColorSensor(Port.B)

#other defenitions
roombot.use_gyro(True)

def turn_bear(angle, speed=100, wait=True):
    sigma = - 10 if angle >= 0 else 10
    bear.run_angle(speed, angle + sigma, wait=wait)

def no_wall_turn(angle, speed=70):
    """speed: deg/s"""
    robot_distance = angle - hub.imu.heading()
    direction = 1 if robot_distance % 360 < 180 else -1
    sigma = - 10 if angle > 0 else  10

    robot_acceleration = roombot.settings()[3]
    motor_acceleration = bear.control.limits()[1]
    bear.control.limits(acceleration=robot_acceleration)

    roombot.settings(turn_rate=speed)
    bear.run_angle(speed, -robot_distance - sigma, wait=False)
    roombot.turn((robot_distance), wait=True)

    bear.control.limits(acceleration=motor_acceleration)


def run1():
    roombot.settings(straight_acceleration=600)
    roombot.straight(295)
    no_wall_turn(50)
    roombot.straight(130)
    arm.run_time(-400, 800)
    roombot.straight(-20)
    no_wall_turn(100)
    roombot.settings(300)
    roombot.straight(-70)
    roombot.settings(200)
    no_wall_turn(200)
    classmethod.straight(-200)


run1()
# wall_turn(360)
# turn_bear(360)
# no_wall_turn(-360)
