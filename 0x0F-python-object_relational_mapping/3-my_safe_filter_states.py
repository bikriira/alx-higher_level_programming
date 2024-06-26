#!/usr/bin/python3
"""
This script retrieves and prints all states
    where name = value passes through command line.
    BUT AVOID SQLInjection

The database credentials (username, password, and database name)
should be passed as command line arguments (in that order):
Example usage:
    3-my_safe_filter_states.py root "" hbtn_0e_0_usa
"""
import MySQLdb
import sys


def selector():
    """
    Lists all states where name = value passes through command line.
        BUT AVOID SQLInjection

    Raises:
        MySQLdb.Error: An error occurred while interacting with the database.
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
        cursor.execute("""SELECT *
                          FROM states
                          WHERE BINARY name = %s
                          ORDER BY id ASC""", (sys.argv[4],))
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
