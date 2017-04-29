from user import User
import server.schema.set_up_scripts.create_schema_script as createSchema
import server.schema.set_up_scripts.create_table_script as createTable
import server.schema.set_up_scripts.drop_schema_script as dropSchema

def main():
    # set up
    dropSchema.main()
    createSchema.main()
    createTable.main()

    # testing
    testUser()

    # wrap up
    dropSchema.main()


def testUser():
    user = User()

    # signUp
    if not user.signUp('jrguo', 'password', 'jiarui', 'guo'):
        print 'ERROR: should be able to sign up jrguo!'

    if user.signUp('jrguo', 'password', 'jiarui', 'guo'):
        print 'ERROR: jrguo already exists!'

    if not user.signUp('jrjrjr', 'jrjrjrjrjr', 'jr', 'jrjr'):
        print 'ERROR: should be able to sign up jrjrjr!'

    # logIn
    if user.logIn('jrguo', 'papapa'):
        print 'ERROR: jrguo\'s password is incorrect!'

    if user.logIn('shent3', 'zoewithbigtong'):
        print 'ERROR: user shent does not exists!'

    if not user.logIn('jrguo', 'password'):
        print 'ERROR: jrguo should be able to log in!'

    if not user.logIn('jrjrjr', 'jrjrjrjrjr'):
        print 'ERROR: jrjrjr should be able to log in!'

    if not user.logIn('jrguo', 'password'):
        # TODO: might change later
        print 'ERROR: should be true, although jrguo is active currently'

    # logOut
    if user.logOut('zoe'):
        print 'ERROR: user zoe does not exist!'

    if not user.logOut('jrguo'):
        print 'ERROR: jrguo should be able to log out successfully!'

    if not user.logOut('jrguo'):
        # TODO: might change later
        print 'ERROR: should be true, although jrguo has already logged out!'

    if not user.logOut('jrjrjr'):
        print 'ERROR: jrjrjr should be able to log out successfully!'

main()