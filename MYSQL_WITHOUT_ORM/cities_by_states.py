import mysql.connector

"""
This script  takes in the name of a state
as an argument and lists all cities of that
state, using the database `hbtn_0e_4_usa`.
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
            cities.id, cities.name
        FROM
            cities
        JOIN
            states
        ON
            cities.state_id = states.id
        WHERE
            states.name LIKE BINARY %(state_name)s
        ORDER BY
            cities.id ASC
    """, {
        'state_name':'%s'
    })

    rows = cur.fetchall()

if rows is not None:
    print(", ".join([row[1] for row in rows]))
