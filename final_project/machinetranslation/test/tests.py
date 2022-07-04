import unittest

from translator import english_to_french, french_to_english

class TestEnglish_To_French(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(""), "null") # test input is null
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test hello translates to bonjour
        self.assertNotEqual(english_to_french("Good"), "Mal") # test good doesnot translate to mal

class TestFrench_To_English(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(""), "null") # test input is null
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test bonjor translates to hello
        self.assertNotEqual(english_to_french("Mal"), "Good") # test mal  doesnot translate to good

unittest.main()