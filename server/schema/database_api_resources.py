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
        query += "CREATE TABLE public."
        query += table.name + "(\n"
        for var_name in table.attributes:
            type = table.attributes[var_name]
            query += var_name + " " + type + ", \n"
        query += "PRIMARY KEY("
        for key in table.primary_keys:
            query += key + ", "
        query = query[0: len(query) - 2] + "))"

        print "executing...\n" + query + "\n"
        try:
            cur.execute(str(query))
            self.connection.commit()
            print "Created table " + table.name
        except Exception as e:
            self.connection.rollback()
            print "Could not create table " + table.name
            print e.message

    def addForeignKeysToTables(self, tables):
        for table in tables:
            self.addForeignKeysToTable(table)

    def addForeignKeysToTable(self, table):
        for key in table.foreign_keys:
            table_ref = table.foreign_keys[key]
            self.addForeignKeyToTable(table.name, key, table_ref)

    def addForeignKeyToTable(self, table_name, key, table_ref):
        cur = self.connection.cursor()
        query = MutableString()
        query += "ALTER TABLE " + table_name + "\n"
        query += "ADD FOREIGN KEY("
        query += key + ") "
        query += "REFERENCES " + table_ref
        print "executing...\n" + query + "\n"
        try:
            cur.execute(str(query))
            self.connection.commit()
            print "Added foreign keys to " + table_name
        except Exception as e:
            self.connection.rollback()
            print "Could not add foreign keys to " + table_name
            print e.message

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
        try:
            cur.execute(str(query))
            self.connection.commit()
        except Exception as e:
            print e.message

    def createSchema(self, schema):
        cur = self.connection.cursor()
        query = MutableString()
        query += "CREATE SCHEMA "
        query += schema
        try:
            cur.execute(str(query))
            self.connection.commit()
        except Exception as e:
            print e.message

    def executeQuery(self, query):
        cur = self.connection.cursor()
        try:
            cur.execute(query)
            # result = cur.fetchone()
            self.connection.commit()
            # self.printResult(result)
        except Exception as e:
            e.message


    def printResult(self, result):
        print result
