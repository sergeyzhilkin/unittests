import unittest
import mymodule

class TestMyModule(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(mymodule.foo(), 'foo')
    
    def test_bar(self):
        self.assertEqual(mymodule.bar(), 'bar')


class TestUserStorage(unittest.TestCase):
    
    def test_add_duplicates(self):
        us = mymodule.UserStorage()
        us.add('petya')
        us.add('petya')
        self.assertEqual(['petya', 'petya'], us.list())

    def test_clear(self):
        us = mymodule.UserStorage()
        us.add('petya')
        us.add('kolya')
        us.add('masha')
        self.assertEqual(['petya', 'kolya', 'masha'], us.list())
        us.clear()
        self.assertEqual([], us.list())

    def test_exists(self):
        us = mymodule.UserStorage()
        self.assertFalse(us.exists('petya'))
        us.add('petya')
        self.assertTrue(us.exists('petya'))

if __name__ == '__main__':
    unittest.main()
