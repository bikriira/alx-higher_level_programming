"""
    Resource: https://www.mikusa.com/python-mysql-docs/index.html
    How to connect as root user in Ubuntu Mysql: https://bobcares.com/blog/error-1698-mysql/
"""
import MySQLdb


db = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")
cur = db.cursor()

songs = ('Purple Haze', 'All Along the Watch Tower', 'Foxy Lady')
for song in songs:
    cur.execute("INSERT INTO song (title) VALUES (%s)", (song,))
    print("Auto Increment ID: %s" % cur.lastrowid)


# Print results in comma delimited format
cur.execute("SELECT * FROM song")
rows = cur.fetchall()
for row in rows:
        print(f"ID {row[0]}: {row[1]},")


cur.execute("SELECT * FROM song WHERE id = %s", (cur.lastrowid,))
data = cur.fetchone()
print("Using fetchone()")
print ("ID {}: {}".format(data[0], data[1]))


try:
    cur.execute("SELECT * FROM songm")
    rows = cur.fetchall()
except MySQLdb.Error as e:
    try:
        print ("MySQL Error [{}]: {}".format(e.args[0], e.args[1]))
    except IndexError:
        print ("MySQL Error: {}".format(str(e)))
# Print results in comma delimited format
rows = cur.fetchall()
for row in rows:
        print(f"ID {row[0]}: {row[1]},")

# For the execution to take real efect in the actual DB use "db.commit()",
# otherwise the changes are limited to the script ecxecution life time
cur.close()
db.close()
