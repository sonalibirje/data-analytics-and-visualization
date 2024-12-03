import yfinance as yf
import os

def fetch_price_data(symbol, start_date, end_date, output_file):
    # Download the data from Yahoo Finance
    data = yf.download(symbol, start=start_date, end=end_date)
    
    # Check if data is downloaded
    if data.empty:
        print("No data downloaded. Check the symbol or date range.")
        return
    
    # Print the first few rows for debugging purposes
    print(data.head())
    
    # Save the data to the specified output file
    data.to_csv(output_file)
    
    # Verify if the file was saved successfully
    if os.path.isfile(output_file):
        print(f"File saved successfully: {output_file}")
    else:
        print(f"Failed to save file: {output_file}")

if __name__ == "__main__":
    # Ensure the 'data' directory exists
    folder_name = "data"
    os.makedirs(folder_name, exist_ok=True)
    
    # Define the output file path within the existing 'data' folder
    output_file = os.path.join(folder_name, "crude_oil_prices.csv")
    
    # Fetch price data and save it
    fetch_price_data('CL=F', '2018-01-01', '2024-01-01', output_file)
