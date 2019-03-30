import serial
import time

# open a "channel" (technically I think its called a "handle") to Serial port
# on Windows my arduino registers as "COM3"
# on rasbian the Tx/Rx pins register as '/dev/ttyS0'

class GPS():
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyS0')
        self.NS = 0.0
        self.EW = 0.0
        self.UTC = ""
        self.line = ""

    def getCoords(self):
        pass
    
    def parseline(str):
        found = False
        if str.find('GPGLL') != -1:
            found = True
        N_start = str.find(',') + 1
        N_end = str.find(',', N_start)
        W_start = str.find('N,') + 3
        W_end = str.find(',', W_start)
        UTC_start = str.find(',', W_end + 1) + 1
        UTC_end = str.find(',', UTC_start) - 1
        self.UTC = str[UTC_start:UTC_end]
        self.NS = str[N_start:N_end]
        self.EW = str[W_start:W_end]
        return found

    def getData(raw = False):
        found = False
        while(not found):
            self.line = self.ser.readline()
            self.line = list(self.line)
            del self.line[0]
            self.line = bytes(self.line).decode('utf-8')
            if (raw):
                print(self.line)
            found = parseline(self.line)

    def __del__(self):
        del self.ser, self.north, self.west, self.line 

if __name__ == "__main__":
    gps = GPS()
    while (True):
        try:
            coords = gps.getData()
            print('N', gps.NS, '; W', gps.EW)
        except KeyboardInterrupt:
            del gps
            break