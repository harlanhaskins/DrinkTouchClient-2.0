import serial
import threading

class RFID(object):

    def __init__(self, address, output, debug=False):
        self.serial = serial.Serial(address)
        self._thread = threading.Thread(target=self.read)
        self._lock = threading.Lock()
        self.debug = debug
        self.output = output
        self._closing = False
        self.reset_code()

    def read(self):
        while not self.code_is_valid() or self._closing:
            with self._lock:
                self._code += self.serial.read()
        with open(self.output, 'w') as output_file:
            output_file.write(self.formatted_code())
        self.reset_code()
        self.read()

    def start(self):
        self._thread.start()

    def stop(self):
        self._closing = True
        self.reset_code()

    def reset_code(self):
        with self._lock:
            self._code = ""

    def code_is_valid(self):
        return len(self._code) == 14

    def formatted_code(self):
        return self._code[1:]

