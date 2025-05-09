from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.tools import hub_menu

hub = PrimeHub()


# colors

Color.BLACK = Color(180, 19, 5)  # run1
Color.YELLOW = Color(51, 75, 62)  # run3
Color.PURPLE = Color(340, 86, 26)  # run2

run_colors = (Color.BLACK, Color.YELLOW, Color.PURPLE, Color.WHITE)

# wheels
right_wheel = Motor(Port.F)
left_wheel = Motor(Port.B, Direction.COUNTERCLOCKWISE)
roombot = DriveBase(left_wheel, right_wheel, 62.4, 108)

# bearing
bear = Motor(Port.A, Direction.COUNTERCLOCKWISE, gears=(28, 140))

# active arm
arm = Motor(Port.E, Direction.COUNTERCLOCKWISE)
# color sensor
sensor = ColorSensor(Port.D)
# other defenitions
roombot.use_gyro(True)


def turn_bear(angle, speed=100, wait=True):
    bear.run_angle(speed, angle, wait=wait)


def abs_bear(angle, speed=100, then=Stop.HOLD, wait=True):
    start_angle = (bear.angle() + 360) % 360  # 208
    print(start_angle)
    deg_to_turn = (angle - start_angle) % 360  # 242
    print(deg_to_turn)
    if then == Stop.NONE:
        if deg_to_turn >= 180:
            turn_bear(speed, deg_to_turn - 360, wait=wait)
        else:
            turn_bear(speed, deg_to_turn, wait=wait)
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


def wall_turn(angle, speed=90):
    roombot.settings(turn_rate=speed)
    roombot.turn(angle, wait=False)
    bear.run_angle(speed, -angle)
    wait(200)


def turn_to(angle, then=Stop.HOLD):
    print(hub.imu.heading())
    start_angle = (hub.imu.heading() + 360) % 360  # 208
    print(start_angle)
    deg_to_turn = (angle - start_angle) % 360  # 242
    print(deg_to_turn)
    if then == Stop.NONE:
        if deg_to_turn >= 180:
            roombot.turn(deg_to_turn - 360)
        else:
            roombot.turn(deg_to_turn)
        return
    if deg_to_turn >= 180:
        roombot.turn(deg_to_turn - 360)
    else:
        roombot.turn(deg_to_turn)


def straight_time(speed, time):
    timer = StopWatch()
    last = roombot.settings()[0]
    roombot.settings(speed)

    while timer.time() < time:
        if speed > 0:
            roombot.straight(1000, wait=False)
        else:
            roombot.straight(-1000, wait=False)
    roombot.stop()

    roombot.settings(last)


# while "1+1 = 3":
#     print(sensor.hsv())
def run1():
    hub.imu.reset_heading(0)
    # setup/sttings
    roombot.settings(350, straight_acceleration=500, turn_rate=150)
    arm.run_time(1000, 1000, wait=False)
    # Change the cruise routes
    roombot.straight(290)
    roombot.turn(45)
    roombot.straight(60)
    arm.run_time(-500, 2000)
    # Colliding with the unknown creature
    roombot.straight(-220)
    no_wall_turn(140)
    roombot.settings(500)
    roombot.straight(-400)
    roombot.settings(350)
    roombot.straight(250)
    turn_to(90)
    roombot.straight(15)
    turn_to(180)
    turn_bear(90)
    # Collecting things
    # roombot.straight(-20)
    # right_wheel.run_angle(500, -500)
    # turn_to(180)
    roombot.settings(straight_acceleration=130)
    roombot.straight(-650)
    roombot.settings(straight_acceleration=500)
    roombot.straight(160)
    turn_to(-90)
    roombot.settings(100)
    straight_time(-130, 2500)
    # driving
    roombot.settings(300)
    arm.run_angle(1000, 90, wait=False)
    roombot.settings(turn_rate=70)
    turn_to(-90)
    roombot.settings(turn_rate=150)
    roombot.straight(400, wait=False)
    wait(1000)
    # turn_bear(-35)
    wait(200)
    turn_to(-87)
    roombot.straight(1000)
    # turn_bear(35)
    turn_to(-90)
    wall_turn(-93.5)
    roombot.straight(-160)
    arm.run_time(-500, 2000, wait=False)
    roombot.straight(110)
    roombot.curve(60, -60, wait=False)
    wall_turn(90)
    roombot.turn(-40)
    roombot.settings(450)
    roombot.straight(100, then=Stop.NONE)
    roombot.curve(500, -45, then=Stop.NONE)
    roombot.curve(300, 45, then=Stop.NONE)
    roombot.straight(300)


def run2():
    hub.imu.reset_heading(0)
    roombot.settings(220, straight_acceleration=350, turn_rate=150)
    roombot.straight(100)
    wall_turn(20)
    roombot.straight(475)
    wall_turn(70)
    straight_time(100, 3000)
    roombot.straight(-150)
    wall_turn(90)
    roombot.straight(-140)
    roombot.settings(turn_rate=70)
    turn_to(87)
    roombot.settings(turn_rate=150)
    roombot.straight(-300)
    roombot.straight(20)
    turn_to(120)
    roombot.straight(-400)
    roombot.straight(120)
    turn_to(180)
    roombot.straight(10000)


def run3():
    hub.imu.reset_heading(0)
    roombot.settings(220, straight_acceleration=350, turn_rate=150)
    roombot.straight(-500)
    roombot.curve(-400, -32)
    roombot.settings()
    turn_to(0)
    roombot.straight(-700)
    roombot.settings(120)
    roombot.straight(400)
    roombot.settings(350)
    roombot.curve(-500, 30)
    roombot.straight(-100)
    roombot.curve(-500, -30)
    roombot.straight(-700)
    roombot.curve(-500, -45)

    # hub.imu.reset_heading(45)
    # straight_speed = 350
    # straight_acceleration = 300
    # turn_rate = 100
    # roombot.settings(straight_speed, straight_acceleration, turn_rate)
    # roombot.straight(150)
    # turn_to(90)
    # roombot.straight(940, wait=False)
    # turn_bear(45)
    # wait(3500)
    # roombot.settings(600, 200)
    # roombot.curve(-400, -30)
    # roombot.settings(straight_speed, straight_acceleration, turn_rate)
    # turn_bear(90)
    # roombot.settings(500, 500)
    # roombot.straight(450, then=Stop.NONE)
    # roombot.curve(400, 60)
# arm.run_time(-2000, 600)


def run4():
    
    roombot.straight(100, then=Stop.NONE)
    roombot.curve(500,-55)
    roombot.straight(320)
    roombot.curve(400, -20)
    roombot.turn(15)
    straight_time(300, 2000)
    arm.run_time(-5000, 3000)
    # turn_bear(45)
    roombot.curve(-300, -90)


# turn_bear(700)
# no_wall_turn(-45)
# roombot.turn(-45)
# roombot.straight
# turn_bear(180)


# roombot.straight(500)
def cycle(iterable):
    iterator = iter(iterable)
    while True:
        try:
            yield next(iterator)
        except StopIteration:
            iterator = iter(iterable)


sensor.detectable_colors(run_colors)
color_cycle = cycle(run_colors)
color_map = {
    Color.BLACK: "3",
    Color.YELLOW: "4",
    Color.PURPLE: "2",
    Color.WHITE: "S",
}

while sensor.color() != next(color_cycle):
    pass

menu = [color_map[sensor.color()]]
for i in range(len(run_colors) - 1):
    menu.append(color_map[next(color_cycle)])


selected = hub_menu(*menu)  # pylint: disable=E1111

if selected == "S":
    run1()

elif selected == "2":
    run2()

elif selected == "3":
    run3()

elif selected == "4":
    run4()

print(selected)
