import serial
from threading import Thread

class iButton(object):

    def __init__(self, ibutton_address, rfid_address, debug=False):
        # self.ibutton_serial = serial.Serial(ibutton_address)
        self.rfid_serial = serial.Serial(rfid_address)
        self.debug = debug
        self.rfid_thread = Thread(target=read_rfid)
        self.ibutton_thread = Thread(target=read_ibutton)
        self.rfid_thread.start()
        self.ibutton_thread.start()

    def read_ibutton(self):
        if self.debug:
            with open("ibutton.txt") as ibutton_file:
                return ibutton_file.readline().strip()

    def read_serial(self):
        code = ''
        while True:
            byte = self.rfid_serial.read()
            code = code.strip()
            if len(code)==13:
                return code[1:]
            code += byte

    def read(self):
        self.rfid_thread.join()
        self.ibutton_thread.join()
