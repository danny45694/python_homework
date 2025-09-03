import sqlite3

# ---------------- ADD FUNCTIONS ----------------
def add_publisher(cursor, publisher_id, name):
    try:
        cursor.execute(
            "INSERT INTO publishers (publisher_id, name) VALUES (?, ?)", 
            (publisher_id, name)
        )
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database")    


def add_magazine(cursor, magazine_id, name, publisher_id, topic):
    try: 
        cursor.execute(
            "INSERT INTO magazines (magazine_id, name, publisher_id, topic) VALUES (?,?,?,?)", 
            (magazine_id, name, publisher_id, topic)
        )
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database")   


def add_subscriber(cursor, subscriber_id, name, address):
    try:
        cursor.execute(
            "INSERT INTO subscribers (subscriber_id, name, address) VALUES (?,?,?)", 
            (subscriber_id, name, address)
        )
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database")   


def add_subscription(cursor, subscription_id, subscriber_id, magazine_id):
    try:
        cursor.execute(
            "INSERT INTO subscriptions (subscription_id, subscriber_id, magazine_id) VALUES (?,?,?)", 
            (subscription_id, subscriber_id, magazine_id)
        )
    except sqlite3.IntegrityError:
        print(f"Subscription {subscription_id} is already in the database") 


# ---------------- DB SETUP ----------------
try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1") 
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                publisher_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                magazine_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                topic TEXT,
                FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                subscriber_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                address TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                subscription_id INTEGER PRIMARY KEY,
                subscriber_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
                FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id),
                UNIQUE(subscriber_id, magazine_id)
            )
        """)

        # ---------------- DATA ----------------
        add_publisher(cursor, 1, "O'Reilly")
        add_publisher(cursor, 2, "McGraw-Hill")
        add_publisher(cursor, 3, "Men's Health")

        add_magazine(cursor, 1, "Wired", 1, "Tech")
        add_magazine(cursor, 2, "Women's Health", 3, "Health")
        add_magazine(cursor, 3, "Fortune", 2, "Business")

        add_subscriber(cursor, 1, "Daniel Diaz", "Santa Monica, CA")
        add_subscriber(cursor, 2, "John Smith", "Los Angeles, CA")
        add_subscriber(cursor, 3, "Jane Doe", "Long Beach, CA")

        add_subscription(cursor, 1, 1, 1)  # Daniel -> Wired
        add_subscription(cursor, 2, 2, 3)  # John -> Fortune
        add_subscription(cursor, 3, 3, 2)  # Jane -> Women's Health

        conn.commit()

except Exception as e:
    print(f"An unexpected error occurred: {e}")


all_info_subscribers = ("SELECT * FROM subscribers")
retrieve_magazines = ("SELECT * FROM magazines ORDER BY name DESC")

join_task = ("""
               SELECT magazine.magazine_id, magazine.name,AS magazine_name, magazine.topic 
               FROM magazines 
               JOIN publishers p ON magazine.publisher_id = publisher.publisher.id 
               WHERE publisher.name = ?;
               
               """)

cursor.execute(all_info_subscribers)
cursor.execute(retrieve_magazines)
cursor.execute(join_task("O'Reilly"))
results = cursor.fetchall()

for row in results:
    print(row)