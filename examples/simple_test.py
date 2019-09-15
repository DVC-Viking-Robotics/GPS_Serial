"""
A simple test of the GPS-Serial library that automatically invokes the threading module.
"""
import time
from gps_serial import GPSserial

# you may want to adjust the port address that is passed to the constructor accordingly.
GPS = GPSserial('/dev/ttyS0')
while True:
    try:
        GPS.get_data() # pass `1` or `true` to print raw data from module
        if GPS.rx_status.startswith('Valid'):
            print('RxStatus:', GPS.rx_status, 'FixType:', GPS.fix)
            print('satelites\' quality:', GPS.sat_quality)
            print('satelites connected:', GPS.sat_connected)
            print('satelites in view:', GPS.sat_view)
            print('Course True North:', GPS.course_true, 'degrees')
            print('Course Magnetic North:', GPS.course_mag, 'degrees')
            print('speed in knots:', GPS.speed_knots, 'speed in kmph:', GPS.speed_kmph)
            print('Altitude:', GPS.altitude, 'meters')
            print('UTC: {}/{}/{} {}:{}:{}'.format(GPS.utc[1], GPS.utc[2], GPS.utc[0], GPS.utc[3], GPS.utc[4], GPS.utc[5]))
            print('lat:', GPS.lat, 'lng:', GPS.lng)
            print('position dilution of precision:', GPS.pdop, 'meters')
            print('horizontal dilution of precision:', GPS.hdop, 'meters')
            print('vertical dilution of precision:', GPS.vdop, 'meters\n')
        else:
            print('Waiting for GPS fix')
        time.sleep(1)
    except KeyboardInterrupt:
        del GPS
        break
