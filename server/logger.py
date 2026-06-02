# FILENAME: logger.py

import os
import sqlite3
from generate_log_id import generate_id

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH  = os.path.join(BASE_DIR, "logs", "logger.db")

def new_log(content, tag_id, tag_name, proj_id, proj_title, timestamp):
    date = timestamp.strftime("%Y-%m-%d")
    time = timestamp.strftime("%H:%M:%S")

    # checker block if log belongs to a tag or a project
    if proj_id is None:
        log_id = generate_id(tag_name, timestamp=timestamp)
    else:
        log_id = generate_id(proj_title,  timestamp=timestamp)


    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Logs (log_id, log_content, tag_id, proj_id, date_created, time_created)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (log_id, content, tag_id, proj_id, date, time))
        conn.commit()

    except Exception as e:
        print(f"Error writing log: {e}")
    
    finally:
        if conn:
            conn.close()