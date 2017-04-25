import connect_server_script
from server.schema import database_api_resources

def main():
    conn = connect_server_script.main()
    resources = database_api_resources.DatabaseAPIResources(conn)
    resources.deleteSchema("public")
    # resources.executeQuery("select * from board")

if __name__ == "__main__":
    main()
