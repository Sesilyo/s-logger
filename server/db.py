# FILENAME: db.py
# Database initialization

import sqlite3

# const
DB_PATH = "logs/logger.db"

def init_db():
    # initialize connection
    conn = sqlite3.connect(DB_PATH)

    # initialize cursor
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS Tags (
            tag_id      TEXT PRIMARY KEY,
            tag_name    TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS Projects (
            proj_id         TEXT PRIMARY KEY,
            proj_title      TEXT NOT NULL,
            is_pinned       INTEGER DEFAULT 0,
            date_created    TEXT NOT NULL,
            time_created    TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS Logs (
            log_id  TEXT PRIMARY KEY,
            log_content     TEXT NOT NULL,
            tag_id          TEXT,
            proj_id         TEXT,
            is_pinned       INTEGER DEFAULT 0,
            date_created    TEXT NOT NULL,
            time_created    TEXT NOT NULL,

            FOREIGN KEY (tag_id) REFERENCES Tags(tag_id),
            FOREIGN KEY (proj_id) REFERENCES Projects(proj_id)
            
        );
    """)

    # write/saves explicitly
    conn.commit()

    # close connection
    conn.close()