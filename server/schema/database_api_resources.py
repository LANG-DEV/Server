from UserString import MutableString
import psycopg2


class DatabaseAPIResources():
    def __init__(self, connection):
        self.connection = connection

    def createTables(self, tables):
        for table in tables:
            self.createTable(table)

    def createTable(self, table):
        cur = self.connection.cursor()
        query = MutableString()
        query += "CREATE TABLE "
        query += table.name + "(\n"
        for var_name in table.attributes:
            type = table.attributes[var_name]
            query += var_name + " " + type + ", \n"
        query += "PRIMARY KEY("
        for key in table.primary_keys:
            query += key + ", "
        query = query[0: len(query) - 3] + "))"

        print "executing...\n" + query + "\n"
        try:
            cur.execute(str(query))
            self.connection.commit()
            print "Created table " + table.name
        except Exception as e:
            print "Could not create table " + table.name
            print e.message

    def addForeignKeysToTables(self, tables):
        for table in tables:
            self.addForeignKeysToTable(table)

    def addForeignKeysToTable(self, table):
        query = MutableString()
        query += "ALTER TABLE " + table.name + "\n"
        query += "ADD FOREIGN KEY("
        for key in table.foreign_keys:
            table_ref = table.foreign_keys[key]
            query += key + " "
            query += "REFERENCES " + table_ref + ", "
        query = query[0: len(query) - 3] + ")\n"
        print "executing...\n" + query + "\n"
        try:
            cur.execute(str(query))
            self.connection.commit()
            print "Added foreign keys to " + table.name
        except:
            print "Could not add foreign keys to " + table.name

    def queryTable(self, table_name):
        cur = self.connection.cursor()
        query = MutableString()
        query += "SELECT * FROM " + table_name
        print "executing " + query
        try :
            cur.execute(str(query))
            result = cur.fetchone()
            for i in range(len(result[0])):
                for j in range(len(result[i][0])):
                    print result[i][j]
            self.connection.commit()
        except:
            print "Could not execute query."

    def deleteSchema(self, schema):
        cur = self.connection.cursor()
        query = MutableString()
        query += "DROP SCHEMA "
        query += schema
        query += " CASCADE"
        cur.execute(str(query))
        self.connection.commit()
