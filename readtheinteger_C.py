import time
class Main:

    def __init__(self):
        print "Sundar"
        self.get_values();
##        self.thrust = 0
##        self.yawrate = 0
##        self.roll = 0.0
##        self.pitch = 0.0
    def get_values(self):
        lines1 = []
        while 1:
            time.sleep(0.5)
            thrust = 0
            yaw = 0
            pitch = 0.0
            roll = 0.0

            
            f = open('testfile.txt', 'r')
            lines = f.readlines()
            for thing in lines:
                lines1.append(int(thing.replace('\n', '')))
            if type(lines1[0]) == int:
                thrust = lines[0]
                print thrust + "thrust"
            else:
                pass
            if type(lines1[1]) == int:
                yawrate = lines[1]
                print yawrate + "yawrate"
            else:
                pass
            if type(lines1[2]) == int:
                pitch = lines[2] 
                print pitch + "pirtch"
            else:
                pass
            if type(lines1[3]) == int:
                roll = lines[3]
                print roll + "roll"
            else:
                pass
            print lines1
            
            lines1 = []
            f.close()
Main()
