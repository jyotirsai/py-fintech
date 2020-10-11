import requests
import json

# set ticker
ticker = "AAPL"

# fetch the data
response = requests.get(
    f"https://www.alphavantage.co/query?function=TIME_SERIES_daily_ADJUSTED&outputsize=full&symbol={ticker}&apikey=RISJR704KEB8ZCB6")

rawData = json.loads(response.text)
timeSeriesData = rawData["Time Series (Daily)"]

# process the data
date = []
price = []


def dataProcessor(timeSeriesData):
    for data in timeSeriesData.items():
        date.append(data[0])
        price.append(float(data[1]["5. adjusted close"]))

    date.reverse()
    price.reverse()

    return date, price


finalData = dataProcessor(timeSeriesData)
