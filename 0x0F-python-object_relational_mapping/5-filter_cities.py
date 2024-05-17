#!/usr/bin/python3
"""
This script takes in the name of a state as one of command line
    argumenant argument and lists all cities of that state.

The database credentials (username, password, and database name, state)
should be passed as command line arguments (in that order):

Example usage:
   5-filter_cities.py root "" hbtn_0e_0_usa Texas
"""
import MySQLdb
import sys


def main():
    """
    Lists all cities with their coresponding states(Uses Joins).

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
        cursor.execute("""
                        SELECT cities.name
                        FROM cities
                            WHERE
                                (
                                    SELECT id FROM states
                                        WHERE BINARY name = %s
                                ) = cities.state_id
                       """, (sys.argv[4],))
        results = cursor.fetchall()

        # Print each result in fromatted way
        print(", ".join(map(lambda results_elem: results_elem[0], results)))

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        # Ensure the cursor and connection are properly closed
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    main()
