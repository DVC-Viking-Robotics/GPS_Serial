import serial

# open a "channel" (technically I think its called a "handle") to Serial port
# on Windows my arduino registers as "COM3"
# on rasbian the Tx/Rx pins register as '/dev/ttyS0'
ser = serial.Serial('/dev/ttyS0')
while (True):
    try:
        # read all data in stream until '\n'
        x = ser.readline()
        # transform the saved bytearray into a list
        x = list(x)
        # delete first garbage character
        del x[0]
        # transform back into bytearray, then decode into string format
        x = bytes(x).decode('utf-8')
        #ready to print or do whatever you want (like parsing a string)
        if (x.find('GPGLL') != -1):
            N_start = x.find(',')
            N_end = x.find(',', N_start + 1)
            W_start = x.find('N,')
            W_end = x.find(',', W_start + 1)
            print('N', x[N_start:N_end], '; W', x[W_start:W_end])
    except KeyboardInterrupt:
        break

