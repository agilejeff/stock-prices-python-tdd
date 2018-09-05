import stockswebui
import unittest

class StocksWebUITests(unittest.TestCase):
    def test_webpage_module_launches_no_error(self):
        result = stockswebui.launchWebsite()
        self.assertTrue(result)