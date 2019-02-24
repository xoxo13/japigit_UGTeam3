import urllib.request
import json

API_KEY = 'M5P3OSS1A8WN5RLJ'

def getStockData(symbol):
    baseURL = 'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols='
    ending = '&apikey=' + API_KEY
    fullURL = baseURL + symbol + ending
    print()
    print('Sending URL:', fullURL)

    # opening URL
    connection = urllib.request.urlopen(fullURL)

    # read and convert to a string
    respString = connection.read().decode()

    print('Response is: ', respString)
    respDict = json.loads(respString)  # JSON to a Python dictionary
    print('Response as a dict is:', respDict)
    stockList = respDict['Stock Quotes']
    stockDict = stockList[0]
    price = stockDict['2. price']

    return price

def main():
    while True:
        print()
        userSymbol = input('Enter a stock symbol (or press ENTER to quit): ')
        if userSymbol == '':
            break
        thisStockPrice = getStockData(userSymbol)

        print()
        print('The current price of', userSymbol, 'is:', thisStockPrice)
        print()
        
main()

print('Thanks for using!')

    



