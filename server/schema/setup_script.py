import psycopg2

import Lang.settings
from server.schema import identity, board, chat_room, group, image, location, message, option, poll, relation, user_in_group, vote
from server.schema.database_api_resources import DatabaseAPIResources


def main():
    host = Lang.settings.DATABASES['default']['HOST']
    db_name = Lang.settings.DATABASES['default']['NAME']
    admin = Lang.settings.DATABASES['default']['USER']
    password = Lang.settings.DATABASES['default']['PASSWORD']
    conn = connectServer(host, db_name, admin, password)

    resource = DatabaseAPIResources(conn)

    tables = createTableList()
    resource.createTables(tables)
    resource.queryTable(tables[0].name)

    # resource.deleteSchema("lang_test")

def connectServer(host, db_name, admin, password):
    try:
        conn = psycopg2.connect("host='" + host + "' dbname='" + db_name + "' user='" + admin + "' password='" + password + "'")
        print "connected to database " + db_name
    except:
        print "could not connect to database " + db_name
    # print "host='" + host + "' dbname='" + db_name + "' user='" + admin + "' password='" + password + "'"
    return conn

def createTableList():
    tables = [board.Board(), chat_room.ChatRoom(), group.Group(), image.Image(), location.Location(), message.Message(),
              option.Option(), poll.Poll(), relation.Relation(), user_in_group.UserInGroup(), vote.Vote()]
    return tables

if __name__ == "__main__":
    main()
