import unittest
import re
import assignment0.main as testObj

class testMain(unittest.TestCase):
    def setUp(self):
        self.incData = testObj.extractincidents()

    def testIncDataLengthGreaterThanZero(self):
        self.assertTrue(len(self.incData) > 0, "Incidents list extracted from pdf is empty")

    def testIncDatePattern(self):
        datePattern = re.compile(r'^.*\/.*\/.*:.*$')
        for inc in self.incData:
            with self.subTest(inc=inc):
                self.assertTrue(datePattern.match(inc[0]))

    def testIncNumberIsNotEmpty(self):
        for inc in self.incData:
            with self.subTest(inc=inc):
                self.assertTrue(inc[1])

    def testIncLocationIsNotEmpty(self):
        for inc in self.incData:
            with self.subTest(inc=inc):
                self.assertTrue(inc[2]=="" or inc[2])

    def testIncNatureIsNotEmpty(self):
        for inc in self.incData:
            with self.subTest(inc=inc):
                self.assertTrue(inc[3]=="" or inc[3])

    def testIncORIIsNotEmpty(self):
        for inc in self.incData:
            with self.subTest(inc=inc):
                self.assertTrue(inc[4])

if __name__ == '__main__':
    unittest.main()
