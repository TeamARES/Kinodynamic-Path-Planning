from a_star_final import *
from motor_control import *
import math

print("Lets start working")

print("Enter starting position coordinates")
d = input().split()
print(d)
x_in = int(d[0])
print(x_in)
y_in = int(d[1])
print(y_in)

print("Enter goal coordinates")
d = input().split()
gx = int(d[0])
gy = int(d[1])

print("Enter starting x velocity")
vx = int(input())
print("Enter starting y velocity")
vy = int(input())
print("Enter goal x velocity")
vgx = int(input())
print("Enter goal y velocity")
vgy = int(input())

print("Depth Map updated at starting position?")
depth_map_status = input()
while depth_map_status == 0:
    depth_map_status = input()
ox = []
oy = []
ox, oy = revise_obstacle_coordinates(ox, oy)

path_planning(x_in, y_in, vx, vy, gx, gy, vgx, vgy, ox, oy)