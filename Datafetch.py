import requests
import json

# fetch the data
response = requests.get(
    "https://www.alphavantage.co/query?function=TIME_SERIES_daily_ADJUSTED&outputsize=full&symbol=AAPL&apikey=RISJR704KEB8ZCB6")

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
