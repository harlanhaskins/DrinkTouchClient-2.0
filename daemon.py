import argparse
import spynner
import serial
import time
import json
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from threading import Thread, Lock

daemon = None

input_dev = "/dev/ttyAMA0"
output = "/tmp/ibutton"

ibutton_file = open(output, "w")
rfid_serial = serial.Serial(input_dev)

rfid_string = ""


class Daemon(FileSystemEventHandler):

    def __init__(self, config):
        self.config = config
        self._js_to_run = None
        self._js_lock = Lock()
        self._closing = False
        self.browser = spynner.Browser()
        self.observer = Observer()
        output_file = config['output_file']
        self.output_filename = os.path.basename(output_file)
        self.output_dir = os.path.dirname(output_file)
        self.observer.schedule(self, self.output_dir)

    def loop(self):
        try:
            self.start()
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.observer.start()
        self.init_browser()
        self.browse()

    def on_modify(self, event):
        print(event.src_path)
        if not self.output_filename in event.srcpath:
            return
        with open(event.src_path) as ibutton_file:
            ibutton = ibutton_file.readline()
            self.did_read_code(ibutton)

    def init_browser(self):
        self.browser.create_webview()
        self.browser.show()
        # self.browser.webview.showFullScreen()
        self.browser.load(config['machine_url'])

    def stop(self):
        self._closing = True
        self.browser.hide()
        self.observer.stop()

    def did_read_code(self, code):
        self.set_js("app.loadiButton(\"%s\");" % code)

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


def read():
    global rfid_string
    for read_id in rfid_serial.read():
        rfid_string += read_id
        print rfid_string
        if len(rfid_string) == 14:
            print "Valid ID:" + rfid_string
            rfid_string = ""
            rfid_serial.flush()
            break


if __name__ == "__main__":
    config = read_config()
    daemon = Daemon(config)
    daemon.loop()

