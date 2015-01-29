#TODO: Implement daemon
import json
import argparse
import spynner
from ibutton import iButton

browser = spynner.Browser(debug_level=spynner.DEBUG)
browser.create_webview()
browser.webview.showFullScreen()

def read_config():
    with open('config.json') as config_file:
        return json.load(config_file)

def main(debug=False, verbose=False):
    config = read_config()
    browser.load("https://webdrink.csh.rit.edu/touchscreen/?machine_id=%d" %
            config['machine_id'])
    ibutton = iButton(config['ibutton_address'], config['rfid_address'],
                      debug=debug)
    print("reading...")
    ibutton_id = ibutton.read()
    print("found ibutton: %s" % ibutton_id)
    browser.runjs("alert('Logged in as %s')" % user.username)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", help="read input from ibutton.txt",
                        action="store_true")
    parser.add_argument("-v", "--verbose", help="prints verbose logs",
                        action="store_true")
    args = parser.parse_args()
    main(debug=args.debug, verbose=args.verbose)
