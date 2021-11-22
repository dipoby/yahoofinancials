from yahoofinancials import YahooFinancials
from datetime import date, timedelta
from os import listdir



def read_cfg(tickers_list):
    # reading tickers.config file
    print('Reading tickers list:')
    with open('tickers.config') as f:
        for line in f:
            if line[0] != '#':
                tickers_list.append(line.strip())
    print(tickers_list)
    return tickers_list


def ingest_data(tickers, file_list_raw):
    # Check directory is empty for Initial run
    if len(listdir('./stock_data')) == 0:
        filename = '-initial-load'
        start_date = '2011-03-10'
        end_date = str(date.today())
    else:
        filename = '-' + str(date.today())
        #start_date = str(date.today()-timedelta(days=1))
        start_date = str(date.today())
        end_date = str(date.today())

    # Receiving data from yahoofinancials
    for ticker in tickers:
        print('Receiving data for '+ticker + '...')
        yahoo_financials = YahooFinancials(ticker)
        with open('./stock_data/'+ticker+filename + '.raw', 'w') as f:
            f.write(str(yahoo_financials.get_historical_price_data(start_date, end_date, 'daily')))
        file_list_raw.append(ticker+filename)

    return file_list_raw


if __name__ == '__main__':
    tickers_list = []
    file_list_raw = []

    read_cfg(tickers_list)
    ingest_data(tickers_list, file_list_raw)
    print(file_list_raw)
