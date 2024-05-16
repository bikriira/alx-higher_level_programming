#!/usr/bin/python3
"""
This script retrieves and prints all states
    where name = value passes through command line.
"""
import MySQLdb
import sys


def selector():
    """
    Lists all states where name = value passes through command line.

    The database credentials (username, password, and database name)
    should be passed as command line arguments (in that order):

    Example usage:
        ./2-my_filter_states.py root "" hbtn_0e_0_usa

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
                          WHERE BINARY name = '{}'
                          ORDER BY id ASC""".format(sys.argv[4]))
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
