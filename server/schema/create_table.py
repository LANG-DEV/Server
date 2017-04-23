# Script to connect to database and create table

import psycopg2
import Lang.settings

try:
    conn = psycopg2.connect("dbname='lang_test' user='lang_admin' host='lang-test.crd09uw5ryqx.us-west-2.rds.amazonaws.com' password='Pm*j7o49VD'")
    print "Connected to the database"
except:
    print "Unable to connect to the database"

cur = conn.cursor()

# cur.execute("""CREATE TABLE test(id INT PRIMARY KEY,
#                                  name VARCHAR)""")

# cur.execute("""INSERT INTO test VALUES(1234, 'Tong')""")

cur.execute("""SELECT * FROM test""")

conn.commit()

rows = cur.fetchall()
for row in rows:
    for col in row:
        print col,
    print
