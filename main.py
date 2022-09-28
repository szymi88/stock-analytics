import yfinance as yf
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as datetime
import data as data

ticker = '^GDAXI'
period = '7d'
df = data.get_data(ticker, period)

print(df)

#df['AAA'] = datetime.datetime.combine(df['Date'].dt.date, df['DayExtremum'])
#df['AAA'] = pd.Timestamp.combine(pd.to_datetime(df['Date']), pd.to_datetime(df['DayExtremum']))
df['AAA'] = pd.to_datetime('2013-01-06'+' '+'23:00:00')

#print(df[['AAA']].dtypes)
#print(df['DayExtremum'].describe())

by_days = yf.Ticker(ticker).history(period=period, interval='15m').filter(["Close"]).reset_index()
#print(by_days)


matplotlib.use('TkAgg')
pd.plotting.register_matplotlib_converters()
#plt.plot(dd['Date'], dd['DayExtremum'], '*')
plt.plot(by_days['Datetime'], by_days['Close'])

#dates = pd.date_range("20130101", periods=6)
#df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
#plt.plot(df)
#plt.show()
plt.savefig('myfilename.png')

#print(dd)
