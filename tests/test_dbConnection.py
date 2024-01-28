import unittest
import sqlite3

class TestSQLiteConnection(unittest.TestCase):
    def test_database_connection(self):
        db_path = './resources/normanpd.db'
        
        try:
            # Attempt to connect to the SQLite database
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()

            # Perform a simple query to check the database connection
            cursor.execute("SELECT 1")

            # Check if the query was successful
            result = cursor.fetchone()
            self.assertEqual(result[0], 1, "Failed to connect to the database or execute query")

        except sqlite3.Error as e:
            self.fail(f"Error connecting to the database: {e}")

        finally:
            # Close the database connection in the 'finally' block to ensure it is closed even if an exception occurs
            if connection:
                connection.close()

if __name__ == '__main__':
    unittest.main()
