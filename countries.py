import sqlite3


def connection():
    connect = None
    try:
        connect = sqlite3.connect('hw.db')
        return connect
    except sqlite3.Error as e:
        print(e)
    return connect


def create_table_countries(connect):
    create_table_countries = """
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(255) NOT NULL
    );
    """
    try:
        cursor = connect.cursor()
        cursor.execute(create_table_countries)
        connect.commit()
    except sqlite3.Error as e:
        print(e)


def add_countries(connect):
    cursor = connect.cursor()
    countries = [
        ('Russia',),
        ('United States',),
        ('China',)
    ]
    insert_query = "INSERT INTO countries (title) VALUES (?)"
    try:
        cursor.executemany(insert_query, countries)
        connect.commit()
    except sqlite3.Error as e:
        print(e)


def create_table_cities(connect):
    create_table_cities = """
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area FLOAT NOT NULL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id) 
    );
    """
    try:
        cursor = connect.cursor()
        cursor.execute(create_table_cities)
        connect.commit()
    except sqlite3.Error as e:
        print(e)


def add_cities(connect):
    cursor = connect.cursor()
    cities = [
        ('Moscow', 2511, 1),
        ('Saint Petersburg', 1439, 1),
        ('New York', 783.8, 2),
        ('Los Angeles', 1302, 2),
        ('Beijing', 16411, 3),
        ('Shanghai', 6340.5, 3),
        ('Shenzhen', 1997.47, 3)
    ]
    insert_query = "INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)"
    try:
        cursor.executemany(insert_query, cities)
        connect.commit()
    except sqlite3.Error as e:
        print(e)


def create_table_students(connect):
    create_table_students = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(id) 
    );
    """
    try:
        cursor = connect.cursor()
        cursor.execute(create_table_students)
        connect.commit()
    except sqlite3.Error as e:
        print(e)


def add_students(connect):
    cursor = connect.cursor()
    students = [
        ('John', 'Doe', 3),
        ('Jane', 'Smith', 3),
        ('Alice', 'Johnson', 1),
        ('Bob', 'Brown', 4),
        ('Charlie', 'Davis', 5),
        ('David', 'Wilson', 6),
        ('Eva', 'Moore', 7),
        ('Frank', 'Taylor', 2),
        ('Grace', 'Anderson', 2),
        ('Hannah', 'Thomas', 4),
        ('Ivy', 'Jackson', 5),
        ('Jack', 'White', 6),
        ('Karen', 'Harris', 7),
        ('Mia', 'Lee', 3)
    ]
    insert_query = "INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)"
    try:
        cursor.executemany(insert_query, students)
        connect.commit()
    except sqlite3.Error as e:
        print(e)


connect = connection()
if connect:
    create_table_countries(connect)
    add_countries(connect)
    create_table_cities(connect)
    add_cities(connect)
    create_table_students(connect)
    add_students(connect)
    connect.close()
