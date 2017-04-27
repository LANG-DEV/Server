from UserString import MutableString

import psycopg2

import Lang.settings

class QueryExecutor:

    def __init__(self):
        host = Lang.settings.DATABASES['default']['HOST']
        db_name = Lang.settings.DATABASES['default']['NAME']
        admin = Lang.settings.DATABASES['default']['USER']
        password = Lang.settings.DATABASES['default']['PASSWORD']
        try:
            self.connection = psycopg2.connect(
                "host='" + host + "' dbname='" + db_name + "' user='" + admin + "' password='" + password + "'")
            print "connected to database " + db_name
        except Exception as e:
            self.connection = None
            print e.message

    # return result as a list
    def executeStringQueryWithResult(self, query):
        cur = self.connection.cursor()
        cur.execute(query)
        print "executing...\n" + query + "\n"
        colnames = [desc[0] for desc in cur.description]
        resultList = []
        resultList.append(colnames)
        for row in cur:
            entry = list(row)
            resultList.append(entry)
        self.connection.commit()
        return resultList

    def executeStringQueryWithoutResult(self, query):
        cur = self.connection.cursor()
        cur.execute(query)
        print "executing...\n" + query + "\n"
        self.connection.commit()
