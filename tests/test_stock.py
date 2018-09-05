import unittest
import stocks

class TestGetPrice(unittest.TestCase):

    def test_assert_equitySymbol_requires_nonblankstring(self):
        self.assertIsNotNone(stocks.equitySymbol())



    def test_equitySymbol_uses_provided_code(self):
        self.assertEqual('EON_X', stocks.equitySymbol("EON_X"))
        self.assertEqual('WAC_X', stocks.equitySymbol())

    def test_price_is_number_greater0(self):
        price = stocks.getPriceWeb("EON_X")
        self.assertGreater(price, 0)

    def test_price_lookup_known(self):
        dateforPrice = '2018-09-03'
        price = stocks.getPriceWeb("EON_X", dateforPrice)
        self.assertEqual(price, 9.2)











