import unittest
import os
from Scraper import Scraper

class TestModel(unittest.TestCase):

    def test_scraper(self):
        sc = Scraper()
        sc.scrape()

        self.assertTrue(os.path.isfile('spoilers.json'))
        self.assertTrue(os.path.isfile('not_spoilers.json'))

        self.assertTrue(os.path.isfile('credentials.json'))

    def test_model(self):
        pass

if __name__ == '__main__':
    unittest.main()