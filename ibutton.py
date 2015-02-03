import serial
import threading

class Reader(object):

    def __init__(self, address, target, debug=False):
        self.serial = serial.Serial(address)
        self._callback = target
        self._thread = threading.Thread(target=read)
        self._lock = threading.Lock()
        self.debug = debug
        self._closing = False

    def read(self):
        while not self.code_is_valid() or self._closing:
            with self._lock:
                self._code += self.serial.read()
        self._callback(self.formatted_code())

    def start(self):
        self._thread.start()

    def stop(self):
        self._closing = True
        self.reset_code()

    def reset_code():
        with self._lock:
            self._code = ""

    def formatted_code(self):
        return self._code # subclasses override

    def code_is_valid(self):
        return False # subclasses override

class iButton(Reader):

    def code_is_valid(self):
        return len(self._code) == 16

class RFID(Reader):

    def code_is_valid(self):
        return len(self._code) == 14

    def formatted_code(self):
        return self._code[1:]

