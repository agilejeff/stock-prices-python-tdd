# python file for code
import urllib.request
import json




# Determine stock symbol

def equitySymbol(targetSymbol="WAC_X"):
    equityLookupSymbol = targetSymbol
    return equityLookupSymbol



def getPriceWeb(symbol="WAC_X", lookupDate = "2018-09-03"):
    priceUrlBase = 'https://www.quandl.com/api/v3/datasets/FSE/' + symbol + '.json?'
    apiKey = 'api_key=qxkJ2yNa3k5tUpnZPzAh'
    dateRange = '&start_date=' + lookupDate + '&end_date=' + lookupDate
    priceUrl = priceUrlBase + apiKey + dateRange
    response = urllib.request.urlopen(priceUrl)
    data = json.load(response)
    price = data['dataset']['data'][0][4]
    return price




# https://www.quandl.com/api/v3/datasets/FSE/EON_X.json?api_key=qxkJ2yNa3k5tUpnZPzAh&start_date=1970-01-01&end_date=1970-01-01