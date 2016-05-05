#A small project to read SMS from you USB dongle
#A project by Shaggs 05/05/2016
import serial
import time
import re
port = serial.Serial('COM14', 460800, timeout=5) #set COM port
port.write('AT+CMGF=1\r\n')      #set text mode
port.write('AT+CSCS="UCS2"\r\n') #set encoding to UCS2
port.write('AT+CMGL="ALL"\r\n')  #get all messages
 
def __decode(str):
    ustr = u''
    str = str.strip().replace('"', '')
    for i in range(len(str)):
        if not i % 4:
            ustr += unichr(int(str[i:i+4], 16))
    return ustr
 
gotmsg = False
 
while(1):
    line = port.readline()
    if line.startswith('+CMGL'):
        info = line.split(',')
        number = (str(__decode(info[2])))
        date = info[4].replace('"', '')
        dates = '/'.join(date.split('/')[::-1])
        time = info[5].replace('+38"', '')
        message = __decode(port.readline())
        print number + ' ' + dates + ' ' + time + str(message) + '\n'
        gotmsg = True
    if gotmsg and line.startswith('OK'): break