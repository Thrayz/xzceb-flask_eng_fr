import unittest
from translator import english_to_french, french_to_english

class TestTranslateEnFr(unittest.TestCase):
    def test_english_to_french(self):
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Bonjour"), "Hello")

class TestTranslateFrEn(unittest.TestCase):
    def test_french_to_english(self):
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Hello"), "Bonjour")

unittest.main()