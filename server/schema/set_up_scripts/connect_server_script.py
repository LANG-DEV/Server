import psycopg2

import Lang.settings

def main():
    host = Lang.settings.DATABASES['default']['HOST']
    db_name = Lang.settings.DATABASES['default']['NAME']
    admin = Lang.settings.DATABASES['default']['USER']
    password = Lang.settings.DATABASES['default']['PASSWORD']
    conn = connectServer(host, db_name, admin, password)
    return conn

def connectServer(host, db_name, admin, password):
    try:
        conn = psycopg2.connect("host='" + host + "' dbname='" + db_name + "' user='" + admin + "' password='" + password + "'")
        print "connected to database " + db_name
    except:
        print "could not connect to database " + db_name
    # print "host='" + host + "' dbname='" + db_name + "' user='" + admin + "' password='" + password + "'"
    return conn

if __name__ == "__main__":
    main()
