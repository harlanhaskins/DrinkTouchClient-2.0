#TODO: Implement daemon
import json
import argparse
import browser
import ibutton
from User import User

#User object
user = None

def read_config():
    with open('config.json') as config_file:
        return json.load(config_file)

def main(debug=False, verbose=False):
    config = read_config()
    if not debug:
        init_serial(config['ibutton_address'], config['rfid_address'])
    ibutton_id = read_ibutton(debug=debug)
    user = User(ibutton_id)
    browser.open_url("http://webdrink.csh.rit.edu/kiosk/" + user.username)

main()
