#iButton Interpretation from Serial Input

import browser
import serial
import User

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




def main():
    #ibuttonId = ser.readline()
    ibuttonId = "123"
    user = User.user(ibuttonId)
    browser.open_url("http://google.com/"+user.username)

if __name__ == "__main__":
    main()
