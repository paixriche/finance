import yfinance as yf
import pandas as pd

def get_correct_ticker(ticker):
    return ticker

def get_company_name(ticker):
    ticker = get_correct_ticker(ticker)
    # company_name = stock.info['longBusinessSummary'].split(',')[0]
    company_name = ticker.split('.')[0]
    return company_name

def get_stock_info(ticker):
    ticker = get_correct_ticker(ticker)
    stock = yf.Ticker(ticker)
    # .history(period="ytd")
    # mowi.head()
    return stock.info

def get_number_of_stocks(ticker):
    ticker = get_correct_ticker(ticker)
    stock = get_stock_info(ticker)
    return stock['sharesOutstanding']

def get_stock_price_dev(ticker, period="ytd"):
    stock = yf.Ticker(get_correct_ticker(ticker))
    company_name = get_company_name(ticker)

    df_stock_price_dev = pd.DataFrame(stock.history(period)['Close'])
    df_stock_price_dev.columns=[str("Stock Price of " + company_name)]
    return df_stock_price_dev   

def multiple_stock_prices_dev(tickers, period='ytd'):
    df_sp = get_stock_price_dev(get_correct_ticker(tickers[0]), period)
    for i in range(1, len(tickers)):
        df_sp_company = get_stock_price_dev(get_correct_ticker(tickers[i]), period)
        df_sp = pd.merge(df_sp, df_sp_company, left_index=True, right_index=True)
    return df_sp

# MARKET CAP
def market_cap_dev(df_stock_price, n_shares_outstanding):
    df_market_cap = df_stock_price*n_shares_outstanding
    return df_market_cap

def market_cap_dev_from_ticker(ticker, period='ytd'):
    ticker = get_correct_ticker(ticker)
    stock = get_stock_info(ticker)
    company_name = get_company_name(ticker)

    df_stock_price_dev = get_stock_price_dev(ticker, period)
    n_shares_outstanding = get_number_of_stocks(ticker)

    df = pd.DataFrame(market_cap_dev(df_stock_price_dev, n_shares_outstanding))
    df.columns=[str("Market Cap of " + company_name)]
    return df

def market_cap_dev_from_tickers(tickers, period='ytd'):
    df_mc = market_cap_dev_from_ticker(get_correct_ticker(tickers[0]), period)
    for i in range(1, len(tickers)):
        df_mc_company = market_cap_dev_from_ticker(get_correct_ticker(tickers[i]), period)
        df_mc = pd.merge(df_mc, df_mc_company, left_index=True, right_index=True)
    return df_mc

# PERCENTAGE CHANGE
def pct_change_from_start(df):
    return df.apply(lambda x: (x/(x.iloc[0])-1))