import json
import argparse
import spynner
import time
from ibutton import iButton
from threading import Thread, Lock

daemon = None

class Daemon():

    def __init__(self, config, debug=False):
        self.config = config
        self.debug = debug
        self._js_to_run = None
        self._js_lock = Lock()
        self._closing = False
        self.ibutton = iButton(self.config['ibutton_address'],
                        debug=self.config.debug)
        self.rfid = RFID(self.config['rfid_address'],
                        debug=self.config.debug)
        self.browser = spynner.Browser()

    def loop():
        try:
            self.browser.create_webview()
            self.browser.webview.showFullScreen()
            self.browser.load(config['machine_url'])
            self.ibutton.start()
            self.rfid.start()
            self.browse()
        except KeyboardInterrupt:
            self.stop()

    def stop():
        self._closing = True
        p.close()
        self.browser.hide()
        self.ibutton.stop()
        self.rfid.stop()

    def _run_js(self):
        with js_lock:
            browser.runjs(js_to_run)
            js_to_run = None

    def browse(self):
        while not self._closing:
            if self.js_to_run:
                self._run_js()
            browser._events_loop()

    def set_js(self, js):
        with js_lock:
            self.js_to_run = js

    def start_reading(self):
        while(True):
            print("reading...")

def read_config(cls):
    with open('config.json') as config_file:
        return json.load(config_file)

def did_read_code(code):
    daemon.set_js("app.loadiButton(\"%s\");" % code)
    iButton

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", help="read input from ibutton.txt",
                        action="store_true")
    parser.add_argument("-v", "--verbose", help="prints verbose logs",
                        action="store_true")
    args = parser.parse_args()
    config = read_config()
    daemon = Daemon(config, debug=args.debug)

