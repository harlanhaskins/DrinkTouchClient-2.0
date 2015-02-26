import serial

class RFID(object):

    def __init__(self, address, output):
        self.serial = serial.Serial(address)
        self.output = output
        self._closing = False
        self.reset_code()

    def read(self):
        while not self.code_is_valid() or self._closing:
            self._code += self.serial.read()
        with open(self.output, 'w') as output_file:
            output_file.write(self.formatted_code())
        self.reset_code()
        self.serial.close()
        self.read()

    def stop(self):
        self._closing = True
        self.reset_code()

    def reset_code(self):
        self._code = ""

    def code_is_valid(self):
        return len(self._code) == 14

    def formatted_code(self):
        return self._code[1:]

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="The serial port to read RFID")
    parser.add_argument("output", help="The file to output RFID cards.")
    args = parser.parse_args()
    rfid = RFID(args.input, args.output)
    rfid.read()
