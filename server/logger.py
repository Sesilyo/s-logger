# FILENAME: logger.py

import sqlite3
from generate_log_id import generate_id


def new_log(content, tag_id, proj_id, timestamp):
    
    # checker block if log belongs to a tag or a project
    if tag_id is None:
        log_id = generate_log_id(proj_id, timestamp=timestamp)
    else:
        log_id = generate_log_id(tag_id,  timestamp=timestamp)


    try:
        conn = sqlite3.connect("logs/logger.db")
        cursor = conn.cursor()
        cursor.execute("""
        
        """)

    except Exception as e:
        print(f"Error writing log: {e}")
    
    finally:
        conn.close()