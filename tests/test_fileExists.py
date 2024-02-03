import unittest
import os

class TestFileExistence(unittest.TestCase):

    def test_db_exists(self):
        file_path = './resources/normanpd.db'
        self.assertTrue(os.path.exists(file_path), f"File '{file_path}' does not exist.")

    def test_incidentPdf_exists(self):
        file_path = './tmp/Incident_Report.pdf'
        self.assertTrue(os.path.exists(file_path), f"File '{file_path}' does not exist.")

if __name__ == '__main__':
    unittest.main()
