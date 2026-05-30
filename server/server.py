# FILENAME : server.py

from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import json
import os

PORT = 8080

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB_DIR = os.path.join(BASE_DIR, "web")

# Multipurpose Internet Mail Extension
MIME_TYPES = {
    '.html' :   'text/html',
    '.css'  :   'text/css',
    '.js'   :   'text/javascript',
    'png'   :   'image/png',
    '.ico'  :   'image/x-icon'
}

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

        ext = os.path.splitext(file_path)[1]
        mime = MIME_TYPES.get(ext, 'text/plain')

        try:
            with open(file_path, 'rb') as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-Type', mime)
            self.end_headers()
            self.wfile.write(content)
        except:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes("File NOT FOUND", 'utf-8'))


def start_server():
    print(f"S-LOGGER middleman running port {PORT}")
    HTTPServer(("", PORT), LogHandler).serve_forever()