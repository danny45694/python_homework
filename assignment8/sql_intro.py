import sqlite3


def add_publishers(cursor, publisher_id, name, topic):
    try:
        cursor.execute("INSERT INTO publishers (publisher_id, name, topic) VALUES (?,?,?)", 
                       (publisher_id, name, topic))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database")    

def add_magazines(cursor, magazine_id, name, topic):
    try: 
        cursor.execute("INSERT INTO magazines (magazine_id, name, topic) VALUES (?,?,?)", 
                       (magazine_id, name, topic))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database")   

def add_subscribers(cursor, subscribers_id, name, num_of_subscribers, topic):
    try:
        cursor.execute("INSERT INTO subscribers (subscribers_id, name, num_of_subscribers, topic) VALUES (?,?,?)", 
                       (subscribers_id, name, num_of_subscribers, topic))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database")   

def add_subscriptions(cursor, subscriptions_id, name, num_of_subscribers, topic):
    try:
        cursor.execute("INSERT INTO subscriptions (subscriptions_id, name_of_subscription, total_revenue, publisher_id, magazine_id, topic) VALUES (?,?,?)", 
                       (subscriptions_id, name_of_subscription, total_revenue, publisher_id, magazine_id, topic))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database") 

#Connect to a new SQLite database

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1") 
        cursor = conn.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS publishers (
                       publisher_id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
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
                       name TEXT NOT NULL,
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
    conn.commit()
        #print("Database created and connected successfully.") 

    # The "with" statement closes the connection at the end of that block.  You could close it 
    # explicitly with conn.close(), but in this case
    # # the "with" statement takes care of that.


except Exception as e:
    print(f"An unexpected error occurred: {e}")