import unittest

from indexer import indexer


class The(unittest.TestCase):
    def test_dog(self):
        s = 'dogcatcatcodecatdog'
        words = ["cat", "dog"]
        self.assertEqual({0, 13}, indexer(string=s, words=words))

    def test_bar(self):
        s = 'barfoobazbitbyte'
        words = ["cat", "dog"]
        self.assertEqual(set(), indexer(string=s, words=words))
