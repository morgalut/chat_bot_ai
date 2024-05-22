# C:\Users\Mor\Desktop\curss2\p8\my_bot_project\my_chatbot\app\utils\database_utils.py

import sqlite3
import traceback
import json

def initialize_database():
    try:
        conn = sqlite3.connect('C:/Users/Mor/Desktop/curss2/p8/my_bot_project/my_chatbot/search_results.db')
        c = conn.cursor()
        # Create table if it does not exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY,
                search_title TEXT,
                category TEXT
            )
        ''')
        # Check if 'category' column exists
        c.execute("PRAGMA table_info(results)")
        columns = [col[1] for col in c.fetchall()]
        if 'category' not in columns:
            c.execute('ALTER TABLE results ADD COLUMN category TEXT')
        conn.commit()
        conn.close()
    except Exception as e:
        log_error(e, 'initialize_database')

def store_results(results, category):
    try:
        conn = sqlite3.connect('C:/Users/Mor/Desktop/curss2/p8/my_bot_project/my_chatbot/search_results.db')
        c = conn.cursor()
        for result in results:
            c.execute('''
                INSERT INTO results (search_title, category) VALUES (?, ?)
            ''', (result, category))
        conn.commit()
        conn.close()
    except Exception as e:
        log_error(e, 'store_results')

def log_error(exception, func_name):
    error_log = {
        'error': str(exception),
        'function': func_name,
        'traceback': traceback.format_exc()
    }
    with open('error_log.json', 'a') as f:
        json.dump(error_log, f)
        f.write('\n')
