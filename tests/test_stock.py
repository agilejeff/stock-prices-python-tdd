import unittest
import stocks

class TestGetPrice(unittest.TestCase):

    def test_assert_equitySymbol_requires_nonblankstring(self):
        self.assertIsNotNone(stocks.equitySymbol())



    def test_equitySymbol_uses_provided_code(self):
        self.assertEqual('EON_X', stocks.equitySymbol("EON_X"))
        self.assertEqual('WAC_X', stocks.equitySymbol())

    def test_price_is_number_greater0(self):
        price = stocks.priceLookup("EON_X")
        self.assertGreater(price, 0)










