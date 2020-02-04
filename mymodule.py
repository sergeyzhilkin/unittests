def foo():
    return 'foo'


def bar():
    return 'bar'


class UserStorage:
    def __init__(self):
     self.storage_list=[]

    """Class represents some user storage"""
    def add(self, username):
        """Adds user to the storage
           :param username - name of the user
        """
        self.storage_list.append(username)
        #raise NotImplementedError()

    def exists(self, username):
        """Checks if user exists in the storage
           :param username - name of the user
        """
        if username in self.storage_list:
         return True
        else:
         return False
        #raise NotImplementedError()

    def clear(self):
        self.storage_list=[]
        """Deletes all users from the storage"""
        #raise NotImplementedError()

    def list(self):
        """Returns the list of all users in the storage"""
        return self.storage_list
        #raise NotImplementedError()
