import sqlite3
from database import initialize_database
from movie_repository import list_movies, add_movie

DATABASE_NAME = "movies.db"

def main():
    """Main function to initialize the database and create tables."""
    initialize_database(DATABASE_NAME)
    start_interface()
    

def start_interface():
    try:
        continue_program = True
        while(continue_program):
            command = input("(L)List, (A)Add, (D)Delete, (X)Exit:")

            if(command.lower() == 'a'):
                title = input("What is the TITLE:")
                format_choice = input("What is the FORMAT (0: DVD, 1: Blu-ray, 2: 4K, 3: Digital):")
                result = add_movie(DATABASE_NAME, title, format_choice)
                if (result):
                    print(f"Added movie: {title} with format {format_choice}")

            if(command.lower() == 'l'):
                print("Listing all movies...")
                rows = list_movies(DATABASE_NAME)
                for row in rows:
                    print(row)

            if(command.lower() == 'd'):
                print("Listing all movies...")
                conn = sqlite3.connect(DATABASE_NAME)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM movies ORDER BY title")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                ID = input("What is the ID to delete:")
                conn.execute("DELETE FROM movies WHERE id = ?", (ID))
                conn.commit()
                conn.close()

            if(command.lower() == 'x'):
                print("Quitting the program...")
                continue_program = False
 
    except ValueError as e:
        print(f"Error: {e}")


# This script generates a random password based on user-defined criteria.
if __name__ == "__main__":
    main()
