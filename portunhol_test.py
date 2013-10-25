# -*- coding: utf-8 -*-

import unittest
from portunhol import Portunholator

class SimplisticTest(unittest.TestCase):

    def test(self):
    	portunholator = Portunholator()

    	portunhol = portunholator.portunholate("Isso é um teste")

        self.assertEqual(portunhol, "Isso é un teste")

if __name__ == '__main__':
    unittest.main()