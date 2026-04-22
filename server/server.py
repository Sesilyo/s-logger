# FILENAME : server.py
# Bridges web UI to the compiled C logger binary

from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import json

PORT = 8080

class LogHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        pass

    def do_GET(self):
        pass

if __name__ == "__main__":
    print(f"S-LOGGER middleman running port {PORT}")
    HTTPServer(("", PORT), LogHandler).serve_forever()