import unittest
import stocks

class TestGetPrice(unittest.TestCase):

    def test_assert_equitySymbol_requires_nonblankstring(self):
        self.assertIsNotNone(stocks.equitySymbol())






