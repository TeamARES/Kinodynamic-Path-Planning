
import socket

s = socket.socket()
host = socket.gethostname()  #IP Address of the Raspberry pi
port = 8999            #Must be same as that in server.py
#In client.py we use another way to bind host and port together by using connect function()
s.connect((host, port))
print('connected to the host')
mode = 0;   #0-> Propulsion
forwardBackwardSpeed = 0;
leftRightSpeed = 0;
linear_velocity=2;
angular_velocity=3;
width_chassi=4;
radius_wheel=2;
def sendDatatoRaspi():
    global forwardBackwardSpeed, leftRightSpeed;

    stringData = str(mode) + ',' + str(forwardBackwardSpeed) + ',' + str(leftRightSpeed)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def printSpeeds():
    global forwardBackwardSpeed, leftRightSpeed;

    stringData = str(mode) + ',' + str(forwardBackwardSpeed) + ',' + str(leftRightSpeed)
    print("MODE 0 DATA :",stringData)

def generate_commands():
    global forwardBackwardSpeed,linear_velocity,angular_velocity,leftRightSpeed,width_chassi,radius_wheel;
    forwardBackwardSpeed = linear_velocity/radius_wheel
    leftRightSpeed = (angular_velocity*width_chassi)/(2*radius_wheel)
    print("generated forwardBackwardSpeed and leftRightSpeed")


#generate linear velocity and angular velocity from path planning module
#now one more question is left is to how to genrate linear and angular velocity from vx and vy
generate_commands()
printSpeeds()
sendDatatoRaspi()
