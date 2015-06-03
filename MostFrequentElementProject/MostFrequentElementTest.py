__author__ = 'Luis'

import unittest

from MostFrequentElementProject.MostFrequentElement import MostFrequentElement

class MostFrequentElementTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(MostFrequentElement.find_most_frequent([]), set([]), 'empty')

    def test_one_element(self):
        self.assertEqual(MostFrequentElement.find_most_frequent([1]), set([1]), 'one element')

    def test_one_most_frequent(self):
        self.assertEqual(MostFrequentElement.find_most_frequent([1, 1, 2, 3]), set([1]), 'one most frequent element')

    def test_more_than_one_most_frequent(self):
        self.assertEqual(MostFrequentElement.find_most_frequent([1, 1, 2, 2, 3]), set([1, 2]), 'two most frequent element')

    def test_each_element_one_time(self):
        self.assertEqual(MostFrequentElement.find_most_frequent([1, 2, 3, 4]), set([1, 2, 3, 4]), 'each value repeated one time')

    def test_each_element_one_time_optimized(self):
        self.assertEqual(MostFrequentElement.optimized_most_frequent_element([1, 2, 3, 4]), set([1, 2, 3, 4]), 'each value repeated one time')