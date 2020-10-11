import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from Datafetch import finalData

dateString = finalData[0]
prices = finalData[1]

dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dateString]

plt.plot(dates, prices)
plt.ylabel("Price ($USD)")
plt.show()
