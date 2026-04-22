# FILENAME: newLog.py

import sqlite3



def generate_log_id(prefix_name, timestamp):
    # prefix_name is the tag name or the project name

    # uses the first three letters of the tag/project
    # converts to uppercase
    prefix = prefix_name[:3].upper()

    # partitions the timestamp into denominations
    # Y year, m month, d day
    # H hour, M minute, S seconds
    date_suffix = timestamp.strftime("%Y%m%d%H%M%S")

    return f"{prefix}{date_suffix}"



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