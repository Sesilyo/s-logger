# FILENAME: search.py

import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "logs", "logger.db")

def get_logs():
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""
            SELECT log_id, log_content, tag_id, proj_id, date_created, time_created
            FROM Logs
            ORDER BY date_created ASC, time_created ASC
        """)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]

    except Exception as e:
        print(f"Error writing log: {e}")
        return []
    
    finally:
        if conn:
            conn.close()