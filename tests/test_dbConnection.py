import unittest
import sqlite3

class Test(unittest.TestCase):
    def test_db(self):
        con = sqlite3.connect('../resources/normanpd.db')
        self.assertIsNot(con, 0)

if __name__ == '__main__':
    unittest.main()