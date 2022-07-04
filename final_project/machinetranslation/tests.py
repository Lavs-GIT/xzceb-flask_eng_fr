import unittest

from translator import english_to_french, french_to_english

class TestEnglish_To_French(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(""), "null") # test input is null
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test hello translates to bonjour

class TestFrench_To_English(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(""), "null") # test input is null
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test hello translates to bonjour

unittest.main()