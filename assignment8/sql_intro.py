import sqlite3

#Connect to a new SQLite database

try:
    with sqlite3.connect("../db/magazines.db") as conn: 
        cursor = conn.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS publishers (
                       publisher_id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL UNIQUE,
                       topic TEXT
                       )
                       """)
        
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS magazines (
                       magazine_id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL UNIQUE,
                       topic TEXT
                       )
                       """)
        
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS subscribers (
                       subscribers_id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL UNIQUE,
                       num_of_subscribers INTEGER,
                       topic TEXT
                       )
                       """)
        
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS subscriptions (
                       subscription_id INTEGER PRIMARY KEY,
                       name_of_subscription TEXT NOT NULL UNIQUE,
                       total_revenue INTEGER,
                       publisher_id TEXT NOT NULL UNIQUE,
                       magazine_id TEXT NOT NULL UNIQUE,
                       FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id),
                       FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
                       )
                       """)

        #print("Database created and connected successfully.") 

    # The "with" statement closes the connection at the end of that block.  You could close it 
    # explicitly with conn.close(), but in this case
    # # the "with" statement takes care of that.
except Exception as e:
    print(f"An unexpected error occurred: {e}")