# FILENAME : server.py

from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import json
import os

PORT = 8080

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB_DIR = os.path.join(BASE_DIR, "web")

class LogHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        pass

    # get path of index.html
    # index.html is the entry point
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        
        file_path = os.path.join(WEB_DIR, self.path[1:])
        print(f"Looking for: {file_path}")

        try:
            file_to_open = open(file_path).read()
            file_path = os.path.join(WEB_DIR, self.path[1:])
            file_to_open = open(file_path).read()
            self.send_response(200)
        except:
            file_to_open = "File NOT FOUND"
            self.send_response(404)
        
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

def start_server():
    print(f"S-LOGGER middleman running port {PORT}")
    HTTPServer(("", PORT), LogHandler).serve_forever()