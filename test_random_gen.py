import unittest

import random_gen

class TestRandom(unittest.TestCase):
    def test_tax_id(self):
        tax_id = random_gen.tax_id()
        self.assertIsInstance(tax_id, str)
        self.assertEqual(len(tax_id), 9)


    def test_street_address(self):
        sa = random_gen.street_address()
        self.assertIsInstance(sa, str)


    def test_zip_length(self):
        zip = random_gen.zip()
        self.assertIsInstance(zip, str)
        self.assertEqual(len(zip), 5)


if __name__ == '__main__':
    unittest.main()
