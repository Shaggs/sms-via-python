# A Small scrpit to send a SMS via python using a USB dongle.
# Tested on a Huawei K3520 that was once locked to Vodaphone but then one day got unlocked OPPS!!

import serial
import time
	 class TextMessage:
    def __init__(self, recipient="incert number here" , message="insert message" % (when.ctime(), msg, unit)):
        self.recipient = recipient
        self.content = message

    def setRecipient(self, number):
        self.recipient = number

    def setContent(self, message):
        self.content = message

    def connectPhone(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 460800, timeout=5) #for mine this was ttyUSB0 but could be ttyUSB1 etc
        time.sleep(1)

    def sendMessage(self):
        self.ser.write('ATZ\r')
        time.sleep(1)
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('''AT+CMGS="''' + self.recipient + '''"\r''')
        time.sleep(1)
        self.ser.write(self.content + "\r")
        time.sleep(1)
        self.ser.write(chr(26))
        time.sleep(1)

    def disconnectPhone(self):
        self.ser.close()

sms = TextMessage()
sms.connectPhone()
sms.sendMessage()
sms.disconnectPhone()