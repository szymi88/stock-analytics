import yfinance as yf
import numpy as np
import pandas as pd


def split_dates(df, label, date_column):
    df = df.reset_index()
    df['Date'] = df[date_column].dt.date
    df['Time' + label] = df[date_column].dt.time
    df = df.drop([date_column], axis=1)
    return df


def get_data(ticker, period):
    history = yf.Ticker(ticker).history(period=period, interval='15m').filter(["High", "Low"])

    max_high_filter = history.groupby(history.index.date)['High'].transform('max') == history['High']
    min_low_filter = history.groupby(history.index.date)['Low'].transform('min') == history['Low']
    high_df = history[max_high_filter].filter(['High'])
    low_df = history[min_low_filter].filter(['Low'])

    high_df = split_dates(high_df, 'High', 'Datetime')
    low_df = split_dates(low_df, 'Low', 'Datetime')
    dd = pd.merge(high_df, low_df, how='left', on='Date')

    by_days = yf.Ticker(ticker).history(period=period, interval='1d').filter(["Open", "Close"]).reset_index()
    by_days['Date'] = by_days['Date'].dt.date

    dd = pd.merge(dd, by_days.reset_index(), how='left', on='Date')
    dd['Change'] = (dd['Close'] - dd['Open'])
    dd['Up'] = dd['Change'] > 0

    dd['DayExtremum'] = np.where(dd['Up'] == True, dd['TimeHigh'], dd['TimeLow'])

    return dd


__all__ = ['get_data']

