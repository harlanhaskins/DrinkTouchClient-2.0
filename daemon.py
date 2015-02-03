import json
import argparse
import spynner
import time
from rfid import RFID
from threading import Thread, Lock

daemon = None

class Daemon():

    def __init__(self, config, debug=False):
        self.config = config
        self.debug = debug
        self._js_to_run = None
        self._js_lock = Lock()
        self._closing = False
        self.rfid = RFID(self.config['rfid_address'],
                         self.config['output_file'],
                         debug=self.debug)
        self.browser = spynner.Browser()

    def loop(self):
        try:
            self.browser.create_webview()
            self.browser.webview.showFullScreen()
            self.browser.load(config['machine_url'])
            self.rfid.start()
            self.browse()
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self._closing = True
        p.close()
        self.browser.hide()
        self.rfid.stop()

    def did_read_code(self, code):
        self.set_js("app.loadiButton(\"%s\");" % code)
        self.rfid.reset_code()

    def _run_js(self):
        with self._js_lock:
            self.browser.runjs(self._js_to_run)
            self._js_to_run = None

    def browse(self):
        while not self._closing:
            if self._js_to_run:
                self._run_js()
            self.browser._events_loop()

    def set_js(self, js):
        with self._js_lock:
            self._js_to_run = js

def read_config():
    with open('config.json') as config_file:
        return json.load(config_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", help="read input from ibutton.txt",
                        action="store_true")
    parser.add_argument("-v", "--verbose", help="prints verbose logs",
                        action="store_true")
    args = parser.parse_args()
    config = read_config()
    daemon = Daemon(config, debug=args.debug)
    daemon.loop()

