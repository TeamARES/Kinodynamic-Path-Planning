from a_star_final import *
from motor_control import *
import math
import socket

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

#socket
s = socket.socket()
print("Enter IP os raspi")
#check here if data is being sent as a string
ip=input()
host = socket.gethostname()  #IP Address of the Raspberry pi
port = 9999
s.connect((host, port))
print('connected to the host')
mode = 0;   #0-> Propulsion
forwardBackwardSpeed = 0;
leftRightSpeed = 0;
width_chassi=4;
radius_wheel=2;

path_planning(x_in, y_in, vx, vy, gx, gy, vgx, vgy, ox, oy)
