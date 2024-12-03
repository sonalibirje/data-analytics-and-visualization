import yfinance as yf
import os

def fetch_price_data(symbol, start_date, end_date, output_file):
    data = yf.download(symbol, start=start_date, end=end_date)
    data.to_csv(output_file)

if __name__ == "__main__":
    os.makedirs("../data", exist_ok=True)
    fetch_price_data('CL=F', '2018-01-01', '2024-01-01', '../data/crude_oil_prices.csv')