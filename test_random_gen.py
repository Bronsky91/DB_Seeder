import unittest
import redtail

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

    def test_basic_contact_card(self):
        phone = random_gen.basic_phone(1)
        address = random_gen.basic_address(2)
        email = random_gen.basic_internet(1, 'Fred', 'Jr')

if __name__ == '__main__':
    unittest.main()
