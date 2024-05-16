#!/usr/bin/python3
import MySQLdb
import sys


def selector():
    """
        Lists all states from the database passed through the command line.

        The database credentials (username, password, and database name)
        should be passed as command line arguments(NB: in that order):

        Example usage:
            ./0-select_states.py root "" hbtn_0e_0_usa
    """
    try:
        # Connect to the database
        conn = MySQLdb.connect(
            host="localhost", port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3]
            )

        cursor = conn.cursor()

        # Execute the query to fetch all states ordered by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        results = cursor.fetchall()

        # Print each row in the results
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        # Ensure the cursor and connection are properly closed
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    selector()
