import sqlite3
import csv

# This script exports data from a SQLite database to a CSV file.
def export_csv(database_file, csv_file):
    """
    Exports the contents of a SQLite database to a CSV file.

    :param database_file: Path to the SQLite database file.
    :param csv_file: Path to the output CSV file.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()

        # Execute a query to select all data from the first table
        cursor.execute("SELECT movie.id, movie.title, format.formatname FROM movie JOIN format ON movie.formatid=format.formatid ORDER BY id")

        # Fetch all rows from the executed query
        rows = cursor.fetchall()

        # Get column names from the cursor description
        column_names = [description[0] for description in cursor.description]

        # Write to CSV file
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(column_names)  # Write header
            writer.writerows(rows)  # Write data

        print(f"Data exported successfully to {csv_file}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
