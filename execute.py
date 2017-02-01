import time
from threading import Thread
 
import cflib.crtp
from cflib.crazyflie import Crazyflie
 
 
class Main:
 
    # Initial values, you can use these to set trim etc.
    roll = 0.0
    pitch = 0.0
    yawrate = 0
    thrust = 10001
 
    def __init__(self):
        self.crazyflie = Crazyflie()
        cflib.crtp.init_drivers()
 
        # You may need to update this value if your Crazyradio uses a different frequency.
        self.crazyflie.open_link("radio://0/10/250K")
 
        self.crazyflie.connectSetupFinished.add_callback(self.connectSetupFinished)
 
    def connectSetupFinished(self, linkURI):
        # Keep the commands alive so the firmware kill-switch doesn't kick in.
        Thread(target=self.pulse_command).start()
 
        while 1:
            time.sleep(0.1)
            #self.thrust = int(raw_input("Set thrust (10001-60000):"))
            f = open('testfile1.txt', 'r')
            lines = f.readlines()
            lines1 = []
            for thing in lines:
                lines1.append(int(thing.replace('\n', '')))
            try:
                self.thrust = lines1[0]
                print(self.thrust) 
            except:
                print("lines is not there")
                pass
##            if type(lines1[1]) == int:
##                yawrate = lines1[1]
##                print yawrate
##            else:
##                pass
##            if type(lines1[2]) == int:
##                pitch = 0.0 
##                print pitch 
##            else:
##                pass
##            if type(lines1[3]) == int:
##                roll = 0.0
##                print roll 
##            else:
##                pass
            print(lines1)
            
            lines1 = []
            f.close()
            if self.thrust == 0:
                self.crazyflie.close_link()
                break
            elif self.thrust <= 10000:
                self.thrust = 10001
            elif self.thrust > 60000:
                self.thrust = 60000
 
    def pulse_command(self):
        if type(self.thrust) == int :
            self.crazyflie.commander.send_setpoint(self.roll, self.pitch, self.yawrate, self.thrust)
        else:
            print("thrust is not an integer")
        time.sleep(0.1)
 
        # ..and go again!
        self.pulse_command()
 
Main()
