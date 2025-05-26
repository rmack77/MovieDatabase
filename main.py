import sqlite3
from database import initialize_database
from movie_repository import list_movies, add_movie, delete_movie
from export import export_csv

DATABASE_NAME = "movies.db"
CSV_FILE_NAME = "movies.csv"
FORMATS = {
    0: "DVD",
    1: "Blu-ray",
    2: "4K",
    3: "Digital"
}

def main():
    """Main function to initialize the database and create tables."""
    initialize_database(DATABASE_NAME)
    start_interface()
    

def start_interface():
    try:
        continue_program = True
        while(continue_program):
            command = input("(L)List, (A)Add, (D)Delete, (C)Export to CSV, (X)Exit:")

            if(command.lower() == 'a'):
                title = input("What is the TITLE:")
                if not title:
                    print("Title cannot be empty.")
                    continue
                format_choice = input("What is the FORMAT (0: DVD, 1: Blu-ray, 2: 4K, 3: Digital):")
                if format_choice not in ['0', '1', '2', '3']:
                    print("Invalid format choice. Please enter 0, 1, 2, or 3.")
                    continue
                result = add_movie(DATABASE_NAME, title, format_choice)
                if (result):
                    print(f"Added movie: {title} with format {format_choice}")

            if(command.lower() == 'l'):
                print("Listing all movies...")
                rows = list_movies(DATABASE_NAME)
                display_list(rows)

            if(command.lower() == 'c'):
                print("Exporting to CSV...")
                export_csv(DATABASE_NAME, CSV_FILE_NAME)
                print(f"Export to CSV complete")

            if(command.lower() == 'd'):
                print("Listing all movies...")
                rows = list_movies(DATABASE_NAME)
                display_list(rows)
                id = input("What is the ID to delete:")
                if not id.isdigit():
                    print("ID must be a number.")
                    continue
                result = delete_movie(DATABASE_NAME, id)
                if (result):
                    print(f"Deleted movie: {id}")

            if(command.lower() == 'x' or command.lower() == 'e'):
                print("Quitting the program...")
                continue_program = False
 
    except ValueError as e:
        print(f"Error: {e}")


# Function to display the list of movies
def display_list(rows):
    for row in rows:
        print(f"{row[1]} (ID: {row[0]}, {row[2]})")
 

if __name__ == "__main__":
    main()
