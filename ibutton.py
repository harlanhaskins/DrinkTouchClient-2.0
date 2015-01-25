#iButton Interpretation from Serial Input

import browser
import serial
import json
from User import User

#Serial connection to ibutton reader
ibutton_serial = None
rfid_serial = None


#User object
user = None

def read_config():
    with open('config.json') as config_file:
        return json.load(config_file)

"""
Initializes the serial connection on the first avalaible serial connection.

If no serial connection is avalaible an exception is thrown
"""
def init_serial(ibutton_address, rfid_address):
    # TODO: Read from config file.
    ibutton_serial = serial.Serial(ibutton_address)
    rfid_serial = serial.Serial(rfid_address)

def read_ibutton(debug=False):
    if debug:
        with open("ibutton.txt") as ibutton_file:
            return ibutton_file.readline().strip()

def main():
    config = read_config()
    init_serial(config['ibutton_address'], config['rfid_address'])
    ibutton_id = read_ibutton()
    user = User(ibutton_id)
    browser.open_url("http://webdrink.csh.rit.edu/kiosk/" + user.username)

if __name__ == "__main__":
    main()
