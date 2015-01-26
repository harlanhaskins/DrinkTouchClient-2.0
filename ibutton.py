import serial

class iButton(object):

    def __init__(self, ibutton_address, rfid_address, debug=False):
        # self.ibutton_serial = serial.Serial(ibutton_address)
        self.rfid_serial = serial.Serial(rfid_address)
        self.debug = debug

    def read(self):
        global rfid_serial
        if self.debug:
            with open("ibutton.txt") as ibutton_file:
                return ibutton_file.readline().strip()
        return self.rfid_serial.read(20)

