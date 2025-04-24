from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

#wheels
right_wheel = Motor(Port.F)
left_wheel = Motor(Port.B, Direction.COUNTERCLOCKWISE)
roombot = DriveBase(left_wheel, right_wheel, 62.4, 108)
# roombot.straight(500)
#bearing
bear = Motor(Port.A, Direction.COUNTERCLOCKWISE, gears=(28, 140))
#active arm
arm = Motor(Port.E, Direction.COUNTERCLOCKWISE)
# arm.run_time(1000, 2500?)

#color sensor
sensor = ColorSensor(Port.D)
#other defenitions
roombot.use_gyro(True)


def turn_bear(angle, speed=100, wait=True):
    bear.run_angle(speed, angle, wait=wait)

def abs_bear(angle, speed=100, then=Stop.HOLD):
    start_angle = (bear.angle() + 360) % 360  # 208
    print(start_angle)
    deg_to_turn = (angle - start_angle) % 360  # 242
    print(deg_to_turn)
    if then == Stop.NONE:
        if deg_to_turn >= 180:
            bear.run_angle(speed, deg_to_turn - 360)
        else:
            bear.run_angle(speed, deg_to_turn)
        return
    if deg_to_turn >= 180:
        bear.run_angle(speed, deg_to_turn - 360)
    else:
        bear.run_angle(speed, deg_to_turn)

def no_wall_turn(angle, speed=70):
    """speed: deg/s"""
    robot_distance = angle - hub.imu.heading()
    direction = 1 if robot_distance % 360 < 180 else -1
    # sigma = - 10 if angle > 0 else  10
    sigma = 0

    robot_acceleration = roombot.settings()[3]
    motor_acceleration = bear.control.limits()[1]
    bear.control.limits(acceleration=robot_acceleration)

    roombot.settings(turn_rate=speed)
    bear.run_angle(speed, -robot_distance - sigma, wait=False)
    roombot.turn((robot_distance), wait=True)

    bear.control.limits(acceleration=motor_acceleration)

def wall_turn(angle, speed = 70):
    roombot.settings(turn_rate=speed)
    roombot.turn(angle, wait=False)
    bear.run_angle(speed, -angle)
    wait(200)
# no_wall_turn(100)
# roombot.curve(500, 20)
# roombot.straight(600)
# bear.run_time(1000, 100000)
# arm.run_time(-400, 5000)
# no_wall_turn(-600)
# roombot.straight(2000, wait=False)
# turn_bear(1000, wait=False)
# arm.run_time(1000, 3000)
# turn_bear(500)
def run1():
    roombot.settings(300, straight_acceleration=550, turn_rate=150)
    arm.run_time(1000,1000,wait=False)
    roombot.straight(300)
    roombot.turn(45)
    roombot.straight(100)
    arm.run_time(-500,2000)
    right_wheel.run_angle(500,-500)
    roombot.straight(-70)
    turn_bear(-60)
    roombot.straight(-270)
    roombot.straight(30)
    turn_bear(70)
    roombot.turn(90)
    no_wall_turn(-200)
    roombot.straight(-100)
    arm.run_time(500,1500, wait=False)
    roombot.straight(1000)
    
    # turn_bear(700)
    # no_wall_turn(-45)
    # roombot.turn(-45)
    # roombot.straight
    # turn_bear(180)



# roombot.straight(500)
# run1()
roombot.straight(500)
turn_bear(90)
turn_bear(10)
abs_bear(0)

# bear.dc(100)
# no_wall_turn(360)
# roombot.straight(1000)
# wall_turn(360)
# turn_bear(360, 900)
# left_wheel.s
# no_wall_turn(-360)
