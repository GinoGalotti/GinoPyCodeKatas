__author__ = 'Luis'

import unittest

from StringMesserProject.StringMesser import StringMesser

class MostFrequentElementTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(StringMesser.char_concat(""), '', "Should work for empty string")

    def test_one_element(self):
        self.assertEqual(StringMesser.char_concat("1"), '', "Should work for 1 character string")

    def test_even_element(self):
        self.assertEqual(StringMesser.char_concat("abc def"),"af1be2cd3","Should work for example test")

    def test_odd_element(self):
        self.assertEqual(StringMesser.char_concat("CodeWars"),'Cs1or2da3eW4',"Should work for 'CodeWars'")

    def test_even_element_optimized(self):
        self.assertEqual(StringMesser.char_concat_optimized("abc def"),"af1be2cd3","Should work for example test")

    def test_odd_element_optimized(self):
        self.assertEqual(StringMesser.char_concat_optimized("CodeWars"),'Cs1or2da3eW4',"Should work for 'CodeWars'")
