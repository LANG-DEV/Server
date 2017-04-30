import connect_server_script
from server.schema import database_api_resources

def main():
    conn = connect_server_script.main()
    resources = database_api_resources.DatabaseAPIResources(conn)
    resources.createSchema("public")

if __name__ == "__main__":
    main()
