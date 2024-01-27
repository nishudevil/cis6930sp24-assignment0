import unittest
import assignment0.main as testObj
class testMain(unittest.TestCase):
    def testExtractIncidentsDataLength(self):
        self.assertTrue(len(testObj.extractincidents())>0,"Extract incidents list from pdf is empty")
    
if __name__ == '__main__':
    unittest.main()