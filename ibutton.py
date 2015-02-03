import serial
import threading

class Reader(object):

    def __init__(self, address, delegate, debug=False):
        self.serial = serial.Serial(address)
        self.delegate = delegate
        self._thread = threading.Thread(target=self.read)
        self._lock = threading.Lock()
        self.debug = debug
        self._closing = False
        self.reset_code()

    def read(self):
        while not self.code_is_valid() or self._closing:
            with self._lock:
                self._code += self.serial.read()
        self.delegate.did_read_code(self.formatted_code())
        self.read()

    def start(self):
        self._thread.start()

    def stop(self):
        self._closing = True
        self.reset_code()

    def reset_code(self):
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

