import json
import argparse
import spynner
import time
from ibutton import iButton
from threading import Thread, Lock

browser = spynner.Browser()
browser.create_webview()
browser.show()
# browser.webview.showFullScreen()

js_to_run = None
js_lock = Lock()

def read_config():
    with open('config.json') as config_file:
        return json.load(config_file)

def main(debug=False, verbose=False):
    config = read_config()
    browser.load("https://webdrink.csh.rit.edu/touchscreen/?machine_id=%d" %
            config['machine_id'])
    p = Thread(target=start_reading, args=(config, browser, debug,))
    p.start()
    browse()

def browse():
    global js_to_run
    while True:
        if js_to_run:
            with js_lock:
                print("running %s" % js_to_run)
                browser.runjs(js_to_run)
                js_to_run = None
        browser._events_loop()

def run_js(js):
    global js_to_run
    with js_lock:
        js_to_run = js

def start_reading(config, browser, debug):
    while(True):
        ibutton = iButton(config['ibutton_address'], config['rfid_address'],
                        debug=debug)
        print("reading...")
        ibutton_id = ibutton.read()
        print("found ibutton: '%s'" % ibutton_id)
        run_js("app.loadiButton(\"%s\");" % ibutton_id)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", help="read input from ibutton.txt",
                        action="store_true")
    parser.add_argument("-v", "--verbose", help="prints verbose logs",
                        action="store_true")
    args = parser.parse_args()
    main(debug=args.debug, verbose=args.verbose)
