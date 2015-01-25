#iButton Interpretation from Serial Input

import browser
import serial
from User import User

#Serial connection to ibutton reader
ser = None

#User object
user = None


"""
Initializes the serial connection on the first avalaible serial connection.

If no serial connection is avalaible an exception is thrown
"""
def init_serial():
    pass

def read_ibutton():
    # TODO: Replace with reading from serial.
    with open("ibutton.txt") as ibutton_file:
        return ibutton_file.readline().strip()

def main():
    ibutton_id = read_ibutton()
    user = User(ibutton_id)
    browser.open_url("http://webdrink.csh.rit.edu/kiosk/" + user.username)

if __name__ == "__main__":
    main()
