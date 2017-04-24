# script for create table

import psycopg2

import Lang.settings

import schema
import identity

def main():
    host = Lang.settings.DATABASES['default']['HOST']
    db_name = Lang.settings.DATABASES['default']['NAME']
    admin = Lang.settings.DATABASES['default']['USER']
    password = Lang.settings.DATABASES['default']['PASSWORD']
    conn = connectServer(host, db_name, admin, password)

    tables = createTableList()

    cur = conn.cursor()
    createTable(cur, tables)
    conn.commit()

    # result = cur.fetchone()
    # print result

def connectServer(host, db_name, admin, password):
    conn = psycopg2.connect("host='" + host + "' dbname='" + db_name + "' user='" + admin + "' password='" + password + "'")
    # print "host='" + host + "' dbname='" + db_name + "' user='" + admin + "' password='" + password + "'"
    return conn

def createTable(cur, tables):
    for table in tables:
        quary = "CREATE TABLE "
        build_attribute = "("
        for name, type in schema.Schema(table).attributes:
            build_attribute += name + type
        print build_attribute

def deleteSchema(cur):
    cur.execute("""DELETE SCHEMA""")

def createTableList():
    tables = [identity.Identity()]
    return tables

if __name__ == "__main__":
	main()
