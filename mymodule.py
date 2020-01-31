def foo():
    return 'foo'


def bar():
    return 'bar'


class UserStorage:
    """Class represents some user storage"""
    def add(self, username):
        """Adds user to the storage
           :param username - name of the user
        """
        raise NotImplementedError()

    def exists(self, username):
        """Checks if user exists in the storage
           :param username - name of the user
        """
        raise NotImplementedError()

    def clear(self):
        """Deletes all users from the storage"""
        raise NotImplementedError()

    def list(self):
        """Returns the list of all users in the storage"""
        raise NotImplementedError()
