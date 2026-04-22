# FILENAME : server.py

from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import json

PORT = 8080

class LogHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        pass

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "index.html not found"
            self.send_response(404)
        
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

def start_server():
    print(f"S-LOGGER middleman running port {PORT}")
    HTTPServer(("", PORT), LogHandler).serve_forever()