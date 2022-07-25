import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

from stockHelper import *

def get_index_divisor(df_stocks, base=100):
    sum_start = df_stocks.sum(axis=1)[0]
    return sum_start/base

# PRICE WEIGHTED
def create_price_weighted_index(tickers, base=100, period='ytd'):
    df_stocks = multiple_stock_prices_dev(tickers, period)
    
    index_divisor = get_index_divisor(df_stocks, base)
    df_stocks = df_stocks/index_divisor
    
    df_stocks = pd.DataFrame(df_stocks.sum(axis=1))
    df_stocks.columns=[str("Value of Index")]

    return df_stocks

# MARKET/CAPITAL WEIGHTED
def create_market_weighted_index(tickers, base=100, period='ytd'):
    df_stocks = market_cap_dev_from_tickers(tickers, period)
    
    index_divisor = get_index_divisor(df_stocks, base)
    df_stocks = df_stocks/index_divisor
    
    df_stocks = pd.DataFrame(df_stocks.sum(axis=1))
    df_stocks.columns=[str("Value of Index")]

    return df_stocks

# EQUAL WEIGHTED
def create_equal_weighted_index(tickers, base=100, period='ytd'):
    df_stocks = multiple_stock_prices_dev(tickers, period)
    df_stocks = pct_change_from_start(df_stocks)+1

    index_divisor = get_index_divisor(df_stocks, base)
    df_stocks = df_stocks/index_divisor
    
    df_stocks = pd.DataFrame(df_stocks.sum(axis=1))
    df_stocks.columns=[str("Value of Index")]
    
    return df_stocks
