from sqlbuilder.smartsql import Q, T
from sql_string_builder import convertToQueryString
from server.database_access_layer.query_executor import QueryExecutor

class User:
    'An object that represents a single user in lang'

    def __init__(self):
        self.queryExecutor = QueryExecutor()
        pass

    def signUp(self, username, password, firstName, lastName):
        """
        Create a new user (add a new entry to the User table)
        :param username:
        :param password:
        :param firstName:
        :param lastName
        :return: userID if successful? or a boolean indicating success or failure?
        table involved: Identity
        """

        # generate query checking if the username exists
        q1 = convertToQueryString(Q(T.Identity).fields('*').where(T.Identity.username == username).count())
        if self.queryExecutor.executeStringQueryWithResult(q1) > 0:
            print 'username already exists'
            return False

        userId = None # generate userId

        # generate query inserting the new user into Identity table
        # can add more information
        q2 = convertToQueryString(Q(T.Identity).insert({
                    T.Identity.userId: userId,
                    T.Identity.username: username,
                    T.Identity.password: password,
                    T.Identity.firstName: firstName,
                    T.Identity.lastName: lastName}))
        self.queryExecutor.executeStringQueryWithoutResult(q2)

        print 'sign up successfully'
        return True


    def logIn(self, username, password):
        """
        Try to log in a user with the given username and password.
        multiple devices?
        :param username:
        :param password:
        :return: succeed or not. (return userId as well?)
        table involved: User
        """
        # 1. check if the username exists
        q1 = convertToQueryString(Q(T.Identity).fields('*').where(T.Identity.username == username).count())
        if self.queryExecutor.executeStringQueryWithResult(q1) == 0:
            print 'username does not exist'
            return False

        # 2. check if the password is correct
        q2 = convertToQueryString(Q(T.Identity).fields(T.Identity.password).where(T.Identity.username == username))
        if self.queryExecutor.executeStringQueryWithResult(q1) != password:
            print 'password does not match'
            return False

        # 3. check status?
        q3 = convertToQueryString(Q.Identity).fields(T.Identity.status).where(T.Identity.username == username)
        status = self.queryExecutor.executeStringQueryWithResult(q3)

        # 4. change status to active??
        

    def logOut(self):
        """
        Log out the current user.
        :return: succeed or not.
        """
        pass

    def changePassword(self, oldPassword, newPassword):
        """
        Change the password of the given user.
        :param oldPassword:
        :param newPassword:
        :return: succeed or not.
        """
        pass

    def sendFriendRequest(self, user):
        pass

    def getFriends(self):
        pass

    def joinEvent(self, event):
        pass

    def leaveEvent(self, event):
        pass

    def getCurrentEvent(self):
        pass
