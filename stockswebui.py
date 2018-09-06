#web ui stuff

import cherrypy
import stocks

class GetStockSymbol(object):
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    @cherrypy.expose
    def index(self):
        return """<html>
            <head></head>
            <body>
                <form method="get" action="price">
                    <input type="text" value="EON_X" name="symbol" />
                    <input type="date" value="2018-09-03" name="date">
                    <button type="submit">Lookup Price</button>
                </form>
            </body>
        </html>"""

    @cherrypy.expose
    def price(self, symbol="WAC_X", date="2018-09-03"):
        data_price = stocks.getPriceWeb(symbol, date)
        return "Closing Price for " + symbol + " on " + date + " was " + str(data_price)

    @cherrypy.expose
    def shutdown(self):
        cherrypy.engine.exit()
        return "shutting down web app"
        exit(9)


def launchWebsite():
    cherrypy.quickstart(GetStockSymbol())
    return True

print(__name__)

if __name__ == '__main__':
    cherrypy.quickstart(GetStockSymbol())

