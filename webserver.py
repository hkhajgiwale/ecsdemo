# >>> try:
# ...     client.head_object(Bucket='dev-client-logs-s3', Key='trigger1')
# ... except botocore.exceptions.ClientError, fault:
# ...     print fault.message


# 'Not Found' in fault.message

# THIS ONLY WORKS WITH PYTHON3.7 and higher

import time
import logging
import traceback
import os
import sys
import threading
import time
import random
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = os.environ.get('PORT', 8080)
VER = os.environ.get('VER', 'VER not set')
HOST = "0.0.0.0"

load_cpu = False

def cpu_load_thread():
    log.info('Cpu load started.')    
    while True:
        if not load_cpu:
            break
        for i in range(1000 * 1000 * 1): # 1Mil loops take about 1.1 seconds
            x = random.randint(0, 1000)
            y = x*x
    log.info('Cpu load ended.')

class Handler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        paths = {
            '/': self._default,
            '/ping': self._ping,
            '/toggle_cpu': self._toggle_cpu,
        }

        if self.path in paths:
            try:
                code, content = paths[self.path]()
                self._respond(code, content)
            except Exception as fault:
                tb = traceback.format_exc()
                self._respond(500, tb)
        else:
            self._respond(500, 'Path not found: %s' % (self.path,))

    def _default(self):
        code = 200
        content = 'load_cpu: %s' % (load_cpu,)
        return code, content

    def _ping(self):
        code = 200
        content = 'pong'
        return code, content

    def _toggle_cpu(self):
        global load_cpu
        load_cpu = not load_cpu

        if load_cpu:
            t = threading.Thread(target=cpu_load_thread)
            t.start()

        code = 200
        content = 'load_cpu: %s' % (load_cpu,)
        return code, content

    def _respond(self, status_code, content):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        content = content + '\n\n%s' % (VER,)
        c = bytes(content, 'UTF-8')
        self.wfile.write(c)

def init_logger():
    log = logging.getLogger(__name__)
    out_hdlr = logging.StreamHandler(sys.stdout)
    out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    out_hdlr.setLevel(logging.INFO)
    log.addHandler(out_hdlr)
    log.setLevel(logging.INFO)
    __builtins__.log = log

    # Once init_logger is called, you can do:    
    # log.debug("NO")
    # log.error("THIS IS AN ERROR")

def main():
    init_logger()
    httpd = ThreadingHTTPServer((HOST, int(PORT)), Handler)
    log.info('Started webserver - %s:%s', HOST, PORT)
    httpd.serve_forever()
    httpd.server_close()
    log.info('Server stopped. Exiting - %s:%s', HOST, PORT)

if __name__ == '__main__':
    main()