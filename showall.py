import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime
import finplot as fplt
import glob

mylist = [f for f in glob.glob("S&P500/*.csv")]

for stock in mylist:
    df =pd.read_csv(str(stock))
    df =df.drop([0,60])
    df['buy'] = np.where(df['Signal'] == 'buy',df['Close'],np.nan)
    df['sold'] = np.where(df['Signal'] == 'sell',df['Close'],np.nan)
    plt.figure(figsize=(10,8))
    # plt.grid()
    plt.title('Buy and Sold Signal')
    plt.plot(df['Close'])
    plt.plot(df['buy'],color='yellow')
    plt.plot(df['sold'],color='red')
    plt.ylabel('Price')
    plt.xlabel('Date')
    plt.show()