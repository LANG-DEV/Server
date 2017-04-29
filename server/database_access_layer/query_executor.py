import psycopg2

import Lang.settings

class QueryExecutor:

    def __init__(self):
        host = Lang.settings.DATABASES['default']['HOST']
        db_name = Lang.settings.DATABASES['default']['NAME']
        admin = Lang.settings.DATABASES['default']['USER']
        password = Lang.settings.DATABASES['default']['PASSWORD']
        self.connection = psycopg2.connect(
            "host='" + host + "' dbname='" + db_name + "' user='" + admin + "' password='" + password + "'")
        print "connected to database " + db_name
        self.connection = None

    # return result as a list
    def executeStringQueryWithResult(self, query):
        cur = self.connection.cursor()
        print "executing...\n" + query + "\n"
        cur.execute(query)
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
        print "executing...\n" + query + "\n"
        cur.execute(query)
        self.connection.commit()
