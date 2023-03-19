import mysql.connector

"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
This time the script is safe from
MySQL injections!
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
            *
        FROM
            states
        WHERE
            name LIKE BINARY %(name)s
        ORDER BY
            states.id ASC
    """, {
        'name':'%s'
    })

    rows = cur.fetchall()

if rows is not None:
    for row in rows:
        print(row)