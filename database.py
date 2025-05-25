import sqlite3

# Movie Database Initialization Script
def initialize_database(filename):
    print("Initializing the Movie Database...")
    does_file_exists = file_exists(filename)

    if (not does_file_exists):
        print("Database file does not exist. Creating a new database...")
        create_database(filename)
    else:
        print("Database file already exists. Checking version...")

    dbversion = get_database_version(filename)
    print(f"Current database version: {dbversion}")

    perform_version_migration(filename, dbversion)


# Checks to see if a file exists
def file_exists(filename):
    """Check if a file exists."""
    try:
        with open(filename, 'r'):
            return True
    except FileNotFoundError:
        return False


# Initialize the database with tables
def create_database(filename):
    """Initialize the database with some sample data."""
    conn = sqlite3.connect(filename)
    conn.execute('''
    CREATE TABLE IF NOT EXISTS movie
    (
          id INTEGER PRIMARY KEY
        , title TEXT
        , format INTEGER -- 0: DVD, 1: Blu-ray, 2: 4K, 3: Digital
    ) ''')
    conn.execute('''
    CREATE TABLE IF NOT EXISTS dbversion
    (
          version TEXT
    ) ''')
    conn.execute('''INSERT INTO dbversion (version) VALUES ('1.01')''')
    # Commit the changes and close the connection
    conn.commit()
    conn.close()


# Perform version migration if necessary
def perform_version_migration(filename, start_version):
    """Perform version migration if necessary."""
    if (start_version == '1.01'):
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        if start_version == '1.01':
            print("Migrating from version 1.01 to 1.02...")
            # Version 1.01 had a table named movies, will be renamed to movie
            cursor.execute('''
                ALTER TABLE movies
                    RENAME TO movie;
            ''')
            cursor.execute('''UPDATE dbversion SET version = '1.02' WHERE version = '1.01' ''')
            conn.commit()
            print("Migration to version 1.02 completed.")
        conn.close()
        start_version = '1.02'


# Get the current database version
def get_database_version(filename):
    """Get the current database version."""
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    
    cursor.execute('SELECT version FROM dbversion')
    version = cursor.fetchone()
    
    if version:
        return version[0]
    else:
        return None
