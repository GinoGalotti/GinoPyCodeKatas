__author__ = 'Luis'

import unittest

from random import randint

from WarriorGameProject.Warrior import Warrior

NAME_LIST=['Hattori Hanzo','Sasuke Sarutobi','Jubei Kibagami','Kotaro Fuma']

class MostFrequentElementTest(unittest.TestCase):

    def setUp(self):
        name = NAME_LIST[randint(0,3)]
        self.ninja = Warrior(name)
        self.assertEqual(self.ninja.name,name,"Making the 'name' variable visible will help you complete this kata")
        new_name = NAME_LIST[randint(0,3)]
        while new_name == name:
            new_name = NAME_LIST[randint(0,3)]

        self.samurai = Warrior(new_name)
        self.assertEqual(self.samurai.name,new_name,"Making the 'name' variable visible will help you complete this kata")

    def test_one_strike(self):
        strike_intensity = 3
        self.samurai.strike(self.ninja, strike_intensity)
        self.assertEqual(self.ninja.health, 70, "This strike should do 30 dmg to the ninja")

    def test_both_strikes(self):
        strike_intensity = 3
        self.samurai.strike(self.ninja, strike_intensity)
        self.ninja.strike(self.samurai, strike_intensity)
        self.assertEqual(self.ninja.health, 70, "This strike should do 30 dmg to the ninja")
        self.assertEqual(self.samurai.health, 70, "This strike should do 30 dmg to the samurai")

    def test_do_two_strikes(self):
        strike_intensity = 4
        self.samurai.strike(self.ninja, strike_intensity)
        self.samurai.strike(self.ninja, strike_intensity)
        self.assertEqual(self.ninja.health, 20, "This strike should do 30 dmg to the ninja")

    def test_kill_the_ninja(self):
        strike_intensity = 5
        self.samurai.strike(self.ninja, strike_intensity)
        self.samurai.strike(self.ninja, strike_intensity)
        self.assertEqual(self.ninja.health, 0, "This strike should do 30 dmg to the ninja")

    def test_cannot_overkill(self):
        strike_intensity = 5
        self.samurai.strike(self.ninja, strike_intensity)
        self.samurai.strike(self.ninja, strike_intensity)
        self.samurai.strike(self.ninja, strike_intensity)
        self.assertEqual(self.ninja.health, 0, "This strike should do 30 dmg to the ninja")
