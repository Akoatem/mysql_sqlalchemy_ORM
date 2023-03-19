import mysql.connector

"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

conn = mysql.connector.connect(host="localhost",
                               port=3306,
                               user="root",
                               passwd="Monica123@#",
                               database="hbtn_0e_0_usa",
                               charset="utf8"
                               )
with conn.cursor() as cur:
    cur.execute("""
        SELECT
            cities.id, cities.name, states.name
        FROM
            cities
        JOIN
            states
        ON
            cities.state_id = states.id
        ORDER BY
            cities.id ASC
    """)

    rows = cur.fetchall()

if rows is not None:
    for row in rows:
        print(row)