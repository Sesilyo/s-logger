# FILENAME: main.py

from db import init_db
from server import start_server

if __name__ == "__main__":
    init_db()
    start_server()