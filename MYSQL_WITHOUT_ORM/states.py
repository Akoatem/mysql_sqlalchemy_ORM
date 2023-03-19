import mysql.connector

"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""
if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
conn = mysql.connector.connect(host="localhost",
                               port=3306,
                               user="root",
                               passwd="Monica123@#",
                               database="hbtn_0e_0_usa",
                               charset="utf8"
                               )
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")

rows = cur.fetchall()

for row in rows:
    print(row)
    cur.close()
    conn.close()