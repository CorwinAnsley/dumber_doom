
import requests
import random
import math
portvariable = 6001
connect = "http://localhost:%s/api/player" % portvariable

r = requests.get("http://localhost:%s/api/player" % portvariable)


#turn to specified angle in correct direction
def turn_to_angle(angle):
    r = requests.get("http://localhost:%s/api/player" % portvariable)
    start_angle = r.json()["angle"]
    if angle == 0 or angle == 360:
        rand = random.uniform(0, 1)
        if rand == 1:
            angle = 1
        else:
            angle = 359

    if angle < 0:
        angle += 360

    delta_angle = angle - start_angle
    inc = 3

    if delta_angle < 0:
        delta_angle += 360

    if delta_angle > 90:
        requests.post(connect + "/turn", json={"type": "right", "target_angle": angle})
    else:
        for i in range(int(delta_angle / inc)+1):
            requests.post(connect + "/actions", json={'type': 'turn-left', 'amount': inc})
        requests.post(connect + "/turn", json={"type": "left", "target_angle": angle})

# turn to specified angle in correct direction as quickly as possible
def turn_to_angle_fast(angle):
    r = requests.get("http://localhost:%s/api/player" % portvariable)
    start_angle = r.json()["angle"]
    if angle == 0 or angle == 360:
        rand = random.uniform(0, 1)
        if rand == 1:
            angle = 1
        else:
            angle = 359

    if angle < 0:
        angle += 360

    delta_angle = angle - start_angle

    if delta_angle < 0:
        delta_angle += 360

    inc = 3
    if delta_angle > 180:
        for i in range(int(delta_angle / inc)):
            requests.post(connect + "/actions", json={'type': 'turn-right', 'amount': inc})
        turn_to_angle(angle)
    else:
        for i in range(int(delta_angle / inc)):
            requests.post(connect + "/actions", json={'type': 'turn-left', 'amount': inc})
        turn_to_angle(angle)


#finds angle between player and given point
def find_angle(x, y):
    r = requests.get("http://localhost:%s/api/player" % portvariable)
    dx = x - r.json()["position"]["x"]
    dy = y - r.json()["position"]["y"]
    angle_rad = math.atan2(dy,dx)
    angle = (angle_rad*(180/math.pi))
    return angle

def aim_point(x, y):
    angle = find_angle(x,y)
    turn_to_angle(angle)
def aim_point_fast(x, y):
    angle = find_angle(x,y)
    turn_to_angle_fast(angle)


#turn_to_angle(0)
#aim_point(-1400,13)
