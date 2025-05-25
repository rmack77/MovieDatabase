import sqlite3

# Add a movie to the database
def add_movie(filename, title, format_choice):
    """Add a movie to the database."""
    try:
        with sqlite3.connect(filename) as conn:
            conn.execute(
                "INSERT INTO movies (title, format) VALUES (?, ?)",
                (title, format_choice)
            )
            conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
    finally:
        conn.close()
    
# List all movies in the database
def list_movies(filename):
    """Retrieve all movies from the database."""
    try:
        with sqlite3.connect(filename) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM movies ORDER BY title")
            rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
    finally:
        conn.close()
