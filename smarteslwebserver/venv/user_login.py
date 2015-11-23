import settings  
import sql_lib as sql
from db_accessor import DBAccessor
from jsonable import Jsonable
import uuid



class UserLogin(DBAccessor,Jsonable):

    def __init__(self):
        DBAccessor.__init__(self)


    def loginUser(self,username):
        """Cause a user to be "logged in". Will lookup user and if present,
        create a login session for the user.
        """
        self.cur.execute( sql.get_user_data, (username,) )
        results = self.cur.fetchall()
        self.userName, self.firstName, self.lastName, self.role = results[0]
        self.groups = _getGroups()
        resultLength = len(results)
        if resultLength == 1:
            self.session_id = str(uuid.uuid4())
            return self

        else:
            raise Exception("Invalid username %s!", username)

    def _getGroups(self):
        self.cur.execute( sql.get_groups_for_user, (self.userName,) )
        return self.cur.fetchall()[0]


