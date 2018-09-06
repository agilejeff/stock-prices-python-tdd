#web ui stuff

import cherrypy
import stocks

class GetStockSymbol(object):
    @cherrypy.expose
    def index(self):
        return """<html>
            <head></head>
            <body>
                <form method="get" action="price">
                    <input type="text" value="EON_X" name="symbol" />
                    <button type="submit">Lookup Price</button>
                </form>
            </body>
        </html>"""

    @cherrypy.expose
    def price(self, symbol="WAC_X"):
        data_price = stocks.getPriceWeb(symbol)
        return "Closing Price for " + symbol + " on Sep 3 was " + str(data_price)


def launchWebsite():
    cherrypy.quickstart(GetStockSymbol())
    return True
