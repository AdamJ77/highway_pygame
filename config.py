import pygame as pg
import math


# GAME
WIDTH, HEIGHT = 1900, 1000
WIN = pg.display.set_mode((WIDTH, HEIGHT))  # maybe add pg.FULLSCREEN ?
DRIVING_AREA_SIZE = (HEIGHT//5 - 50, HEIGHT - 160)

# BLANK HIGHWAY AREA (TO TEST RECT)
AREA_SURFACE = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)

# PLAYER
PLAYER_IMAGE = pg.transform.rotate(pg.image.load("images/player_car_new.png"), -90)
PLAYER_WIDTH, PLAYER_HEIGHT = PLAYER_IMAGE.get_width(), PLAYER_IMAGE.get_height()

SPEED_PLAYER = 0
MAX_SPEED_PLAYER = 20
ACELERATION = 0.5
SPEED_CAR_SIDEWAYS = 5
FRICTION_DECEL = 0.5     # decelaration caused by friction and no acceleration
BRAKE_DECEL = 10

ANGLE_ROTATE = 3
ROTATION_BACK_SPEED_ANGLE = 2
MAX_ANGLE = 45

MAX_ANGLE_TRAFFIC_CHANGE_LINE = 30

#BRAKE LIGHTS
BRAKE_LIGHTS = pg.transform.rotate(pg.image.load("images/lights_on.png"), -90)


# BACKGROUND
HIGHWAY_IMAGE = pg.transform.scale(pg.image.load("images/highway2.png"), (WIDTH, HEIGHT))
HIGHWAY_IMAGE_WIDTH = HIGHWAY_IMAGE.get_width()
# BACKGROUND SCROLL CONFIG
bg_tiles = math.ceil((WIDTH / HIGHWAY_IMAGE_WIDTH)) + 2    # maybe 1
SCROLL_SPEED = 5


# LAMP SCROLL
# LAMP_WIDTH = 35
# LAMP_HEIGHT = 173
# DISTANCE_BETWEEN_LAMPS = 500

LAMPS_IMAGE = pg.image.load("images/row_lamps.png")
LAMPS_WIDTH = LAMPS_IMAGE.get_width()
lamp_tiles = math.ceil((WIDTH / LAMPS_WIDTH)) + 2


# CARS
CAR_IMAGE_RED = pg.transform.rotate(pg.image.load("images/car1.png"), 90)
CAR_IMAGE_GREEN = pg.transform.rotate(pg.image.load("images/car2.png"), 90)
CAR_IMAGE_PURPLE = pg.transform.rotate(pg.image.load("images/car3.png"), 90)
CAR_WIDTH = CAR_IMAGE_RED.get_width()
CAR_HEIGHT = CAR_IMAGE_RED.get_height()

# MUSCLE CAR
MUSCLE_CAR_IMAGE_YELLOW = pg.transform.rotate(pg.image.load("images/car4.png"), -90)
MUSCLE_CAR_WIDTH = MUSCLE_CAR_IMAGE_YELLOW.get_width()
MUSCLE_CAR_HEIGHT = MUSCLE_CAR_IMAGE_YELLOW.get_height()

# SEDAN CAR
SEDAN_CAR_IMAGE_BROWN = pg.transform.rotate(pg.image.load("images/car5.png"), -90)
SEDAN_CAR_WIDTH = SEDAN_CAR_IMAGE_BROWN.get_width()
SEDAN_CAR_HEIGHT = SEDAN_CAR_IMAGE_BROWN.get_height()

# TRUCK
TRUCK_WIDTH, TRUCK_HEIGHT = 161, 534
TRUCK_IMAGE = pg.transform.rotate(pg.transform.scale(pg.image.load("images/truck.png"), (TRUCK_WIDTH, TRUCK_HEIGHT)), -90)
TRUCK_WIDTH = TRUCK_IMAGE.get_width()
TRUCK_HEIGHT = TRUCK_IMAGE.get_height()

# POLICE
POLICE_CAR_IMAGE = pg.transform.rotate(pg.image.load("images/police_car.png"), -90)
POLICE_CAR_IMAGE_LIGHTS_R = pg.transform.rotate(pg.image.load("images/police_car_lights_r.png"), -90)
POLICE_CAR_IMAGE_LIGHTS_B = pg.transform.rotate(pg.image.load("images/police_car_lights_b.png"), -90)
POLICE_CAR_WIDTH = POLICE_CAR_IMAGE.get_width()
POLICE_CAR_HEIGHT = POLICE_CAR_IMAGE.get_height()

FREQUENCY_OF_POLICE_LIGHTS = 10
TIME_OF_TURN = 10

# OTHER OBJECTS

#SPAWN LOCATIONS
SPAWN_LOC_1 = (HIGHWAY_IMAGE_WIDTH - CAR_WIDTH, DRIVING_AREA_SIZE[0] + 80)
SPAWN_LOC_2 = (HIGHWAY_IMAGE_WIDTH - CAR_WIDTH, DRIVING_AREA_SIZE[0] + 300)
SPAWN_LOC_3 = (HIGHWAY_IMAGE_WIDTH - CAR_WIDTH, DRIVING_AREA_SIZE[0] + 520)
SPAWN_LOCATIONS = [SPAWN_LOC_1, SPAWN_LOC_2, SPAWN_LOC_3]
