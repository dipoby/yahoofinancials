from yahoofinancials import YahooFinancials
from os import listdir
from datetime import date, timedelta


def read_cfg(tickers_list):
    # reading tickers.config file
    print('Get tickers list:')
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
        print('Enter start date(yyyy-mm-dd):')
        start_date = input()
        end_date = str(date.today())
    else:
        filename = '-' + str(date.today())
        start_date = str(date.today())
        end_date = str(date.today())

    # get data from yahoo....
    for ticker in tickers:
        print('Receiving data for ticker: '+ ticker + '...')
        yahoo_financials = YahooFinancials(ticker)
        with open('./stock_data/'+ticker+filename + '.json', 'w') as f:
            f.write(str(yahoo_financials.get_historical_price_data(start_date, end_date, 'daily')))
        file_list_raw.append(ticker+filename)

    return file_list_raw

tickers_list = []
file_list_raw = []

read_cfg(tickers_list)
ingest_data(tickers_list, file_list_raw)
print(file_list_raw)

    
