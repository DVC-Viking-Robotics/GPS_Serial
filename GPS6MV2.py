import serial
import time

# open a "channel" (technically I think its called a "handle") to Serial port
# on Windows my arduino registers as "COM3"
# on rasbian the Tx/Rx pins register as '/dev/ttyS0'

class GPS():
    def __init__(self, onRaspi = True):
        if onRaspi:
            self.ser = serial.Serial('/dev/ttyS0')
        else:
            self.ser = serial.Serial('COM3')
        self.NS = 0.0
        self.EW = 0.0
        self.UTC = ""
        self.line = ""
        self.speed = []
        self.course = []
        self.sat = []
        self.alt = 0.0
        self.azi = 0.0
        self.elev = 0.0
        self.fix = "no Fix"
        
    def getCoords(self):
        pass
    
    def getTime(self):
        if (self.UTC == ""):
            return "no time"
        else:
            hr = self.UTC[0:2]
            min = self.UTC[3:4]
            sec = self.UTC[5:]
            return hr +":"+ min +":"+ sec

    def parseline(str):
        found = False
        if str.find('GPGLL') != -1:
            N_start = str.find(',') + 1
            N_end = str.find(',', N_start)
            W_start = str.find('N,') + 3
            W_end = str.find(',', W_start)
            UTC_start = str.find(',', W_end + 1) + 1
            UTC_end = str.find(',', UTC_start) - 1
            self.UTC = str[UTC_start:UTC_end]
            self.NS = str[N_start:N_end]
            self.EW = str[W_start:W_end]
        elif (str.find('GPVTG') != -1):
            found = True
            C_T_start = str.find(',') + 1
            C_T_end = str.find(',', C_T_start)
            C_M_start = str.find(',', C_T_end + 1) + 1
            C_M_end = str.find(',', C_M_start)
            S_N_start = str.find(',', C_M_end + 1) + 1
            S_N_end = str.find(',', S_N_start)
            S_G_start = str.find(',', S_N_end + 1) + 1
            S_G_end = str.find(',', S_G_start)
            self.course["true"] = str[C_T_start:C_T_end]
            self.course["mag"] = str[C_M_start:C_M_end]
            self.speed["knots"] = str[S_N_start:S_N_end]
            self.speed["kmps"] = str[S_G_start:S_G_end]
        elif (str.find('GPGGA') != -1):
            Qual_start = str.find(',') + 1
            for i in range(2,6):
                Qual_start = str.find(',', Qual_start) + 1
            Qual_end = str.find(',', Qual_start)
            Sat_end = str.find(',', Qual_end + 1)
            Alt_start = str.find(',', Sat_end + 1) + 1
            Alt_end = str.find(',', Alt_start)
            self.sat["quality"] = str[Qual_start:Qual_end]
            self.sat["connected"] = str[Qual_end + 1:Sat_end]
            self.alt = str[Alt_start:Alt_end]
        elif (str.find('GPGSV') != -1):
            View_start = str.find(',') + 1
            for i in range(2,3):
                View_start = str.find(',', View_start) + 1
            View_end = str.find(',', View_start)
            Elev_start = str.find(',', View_end + 1) + 1
            Elev_start = str.find(',', Elev_start) + 1
            Elev_end = str.find(',', Elev_start)
            Azi_end = str.find(',', Elev_end + 1)
            self.sat["view"] = str[View_start:View_end]
            self.sat["connected"] = str[View_end + 1:Sat_end]
            self.elev = str[Elev_start:Elev_end]
            self.azi = str[Elev_end + 1:Azi_end]
        elif (str.find('GPGSA') != -1):
            typeFix = ["No Fix","2D", "3D"]
            Fix_start = str.find(',') + 1
            Fix_start = str.find(',', Fix_start) + 1
            Fix_end = str.find(',', Fix_start)
            self.fix =typeFix[int(str[Fix_start:Fix_end])]
        elif (str.find('GPRMC') != -1):
            status = {"V":"Warning","A": "Valid"}
            Stat_start = str.find(',') + 1
            Stat_start = str.find(',', Stat_start) + 1
            Stat_end = str.find(',', Stat_start)
            self.fix =typeFix[str[Stat_start:Stat_end]]

        return found

    def getData(self, raw = False):
        found = False
        while(not found):
            self.line = self.ser.readline()
            self.line = list(self.line)
            del self.line[0]
            self.line = bytes(self.line).decode('utf-8')
            if (raw):
                print(self.line)
            found = parseline(self.line)
'''
    def __del__(self):
        del self.ser, self.north, self.west, self.line 
'''
if __name__ == "__main__":
    gps = GPS(False)
    while (True):
        try:
            coords = gps.getData(True)
            print('N', gps.NS, '; W', gps.EW)
        except KeyboardInterrupt:
            del gps
            break