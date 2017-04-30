import psycopg2

import connect_server_script
from server.schema import identity, board, chat_room, group, image, location, message, option, poll, relation, user_in_group, vote
from server.schema.database_api_resources import DatabaseAPIResources


def main():
    conn = connect_server_script.main()
    resource = DatabaseAPIResources(conn)
    tables = createTableList()

    # create tables
    resource.createTables(tables)
    # resource.queryTable(tables[0].name)

    # add foreign keys
    resource.addForeignKeysToTables(tables)

def createTableList():
    tables = [board.Board(), chat_room.ChatRoom(), group.Group(), image.Image(), location.Location(), message.Message(),
              option.Option(), poll.Poll(), relation.Relation(), user_in_group.UserInGroup(), vote.Vote(), identity.Identity()]
    # tables = [chat_room.ChatRoom()]
    return tables

if __name__ == "__main__":
    main()
