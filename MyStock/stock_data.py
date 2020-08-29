from yahoofinancials import YahooFinancials
import yfinance as yf
import datetime

# yahoo_financials = YahooFinancials('AAPL')
# print(yahoo_financials.get_financial_stmts('annual', 'income'))
#
#


def yfinance(ticker):
    tickerdata = yf.Ticker(ticker)
    tickerinfo = tickerdata.info
    investment =tickerinfo['shortName']
    print('Investment :  '+ investment)
    today = datetime.datetime.today().isoformat()
    print('Today  :  ' + today)
    tikckerdf = tickerdata.history(period='1d', start="2020-1-1", end=today[:10])
    pricelast = tikckerdf['Close'].iloc[-1]
    print('Investment :  ' + investment)
    print(pricelast)
    print(tickerinfo)

yfinance('TSLA')







#
#
#
#
# tech_stocks = ['AAPL', 'MSFT', 'INTC']
# bank_stocks = ['WFC', 'BAC', 'C']
# commodity_futures = ['GC=F', 'SI=F', 'CL=F']
# cryptocurrencies = ['BTC-USD', 'ETH-USD', 'XRP-USD']
# currencies = ['EURUSD=X', 'JPY=X', 'GBPUSD=X']
# mutual_funds = ['PRLAX', 'QASGX', 'HISFX']
# us_treasuries = ['^TNX', '^IRX', '^TYX']
#
# yahoo_financials_tech = YahooFinancials(tech_stocks)
# yahoo_financials_banks = YahooFinancials(bank_stocks)
# yahoo_financials_commodities = YahooFinancials(commodity_futures)
# yahoo_financials_cryptocurrencies = YahooFinancials(cryptocurrencies)
# yahoo_financials_currencies = YahooFinancials(currencies)
# yahoo_financials_mutualfunds = YahooFinancials(mutual_funds)
# yahoo_financials_treasuries = YahooFinancials(us_treasuries)
#
# tech_cash_flow_data_an = yahoo_financials_tech.get_financial_stmts('annual', 'cash')
# bank_cash_flow_data_an = yahoo_financials_banks.get_financial_stmts('annual', 'cash')
#
# banks_net_ebit = yahoo_financials_banks.get_ebit()
# tech_stock_price_data = yahoo_financials_tech.get_stock_price_data()
# daily_bank_stock_prices = yahoo_financials_banks.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
# daily_commodity_prices = yahoo_financials_commodities.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
# daily_crypto_prices = yahoo_financials_cryptocurrencies.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
# daily_currency_prices = yahoo_financials_currencies.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
# daily_mutualfund_prices = yahoo_financials_mutualfunds.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')
# daily_treasury_prices = yahoo_financials_treasuries.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')