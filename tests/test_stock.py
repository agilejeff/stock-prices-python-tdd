import unittest
import stocks

class TestGetPrice(unittest.TestCase):

    def test_assert_equitySymbol_requires_nonblankstring(self):
        self.assertIsNotNone(stocks.equitySymbol())

    def test_equitySymbol_uses_provided_code(self):
        self.assertEqual('EON_X', stocks.equitySymbol("EON_X"))












