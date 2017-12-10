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
        train_size = [0.95, 0.94, 0.93, 0.92, 0.91, 0.9, 0.89, 0.88, 0.87, 0.86, 0.85, 0.84, 0.83, 0.82, 0.81, 0.80, 0.79, 0.78, 0.77, 0.76, 0.2, 0.1, 0.0]
        accuracy = [0.87552742616, 0.861917326297, 0.864355689525, 0.86345646438, 0.854545454545, 0.873878627968, 0.873860911271, 0.857897052354, 0.853024766545, 0.860859728507, 0.852568613652, 0.866710656549, 0.865527950311, 0.86862170088, 0.858888888889, 0.866420274551, 0.8662644545, 0.852447216891, 0.861372504017, 0.856797184338, 0.6, 0.4, 0.0]

        for curr_accuracy in accuracy:
            self.assertTrue(curr_accuracy >= 0.8)


if __name__ == '__main__':
    unittest.main()