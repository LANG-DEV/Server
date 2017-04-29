from sqlbuilder.smartsql import Q, T
from sql_string_builder import convertToQueryString
from server.database_access_layer.query_executor import QueryExecutor
import uuid

class User:
    'An object that represents a single user in lang'

    def __init__(self):
        self.queryExecutor = QueryExecutor()

    def signUp(self, username, password, firstName, lastName):
        """
        Create a new user (add a new entry to the User table)
        :param username:
        :param password:
        :param firstName:
        :param lastName
        :return: (currently T/F indicating succeed or not)
        table involved: Identity
        """

        # generate query checking if the username exists
        q1 = convertToQueryString(Q(T.Identity).fields('*').where(T.Identity.username == username).count())
        if self.queryExecutor.executeStringQueryWithResult(q1)[1][0] > 0:
            print 'username already exists'
            return False

        userId = uuid.uuid4().hex  # generate userId

        # generate query inserting the new user into Identity table
        # can add more information
        q2 = convertToQueryString(Q(T.Identity).insert({
                    T.Identity.userId: userId,
                    T.Identity.username: username,
                    T.Identity.password: password,
                    T.Identity.firstName: firstName,
                    T.Identity.lastName: lastName,
                    T.Identity.status: 'offline'}))
        self.queryExecutor.executeStringQueryWithoutResult(q2)

        print 'sign up successfully'
        return True

    def logIn(self, username, password):
        """
        Try to log in a user with the given username and password.
        multiple devices?
        :param username:
        :param password:
        :return: (currently T/F indicating succeed or not)
        table involved: User
        """
        # 1. check if the username exists
        q1 = convertToQueryString(Q(T.Identity).fields('*').where(T.Identity.username == username).count())
        if self.queryExecutor.executeStringQueryWithResult(q1)[1][0] == 0:
            print 'username does not exist'
            return False

        # 2. check if the password is correct
        q2 = convertToQueryString(Q(T.Identity).fields(T.Identity.password).where(T.Identity.username == username))
        if self.queryExecutor.executeStringQueryWithResult(q2)[1][0] != password:
            print 'password does not match'
            return False

        # 3. check status?
        q3 = convertToQueryString(Q(T.Identity).fields(T.Identity.status).where(T.Identity.username == username))
        status = self.queryExecutor.executeStringQueryWithResult(q3)[1][0]
        if status != 'offline':
            # TODO: logout previous login automatically?
            print 'already in lang!'
            return True

        # 4. change status to preLang
        q4 = convertToQueryString(Q(T.Identity).
                                  where(T.Identity.username == username).
                                  update({T.Identity.status: 'preLang'}))
        self.queryExecutor.executeStringQueryWithoutResult(q4)

        print 'logged in successfully'
        return True

    def logOut(self, username):
        """
        Log out the current user.
        :return: succeed or not.
        """
        # 1. check if the username exists
        q1 = convertToQueryString(Q(T.Identity).fields('*').where(T.Identity.username == username).count())
        if self.queryExecutor.executeStringQueryWithResult(q1)[1][0] == 0:
            print 'username does not exist'
            return False

        # 2. check status?
        q2 = convertToQueryString(Q(T.Identity).fields(T.Identity.status).where(T.Identity.username == username))
        status = self.queryExecutor.executeStringQueryWithResult(q2)[1][0]
        if status == 'offline':
            print 'already offline!'
            return True

        # 3. change status
        q3 = convertToQueryString(Q(T.Identity).
                                  where(T.Identity.username == username).
                                  update({T.Identity.status: 'offline'}))
        self.queryExecutor.executeStringQueryWithoutResult(q3)

        print 'logged out successfully'
        return True

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
