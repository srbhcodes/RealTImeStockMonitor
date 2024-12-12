import random  # Add this line to import the random module
import requests
from kafka import KafkaProducer
import time
import json

# Your Alpha Vantage API Key
API_KEY = 'KO53F1C1355VWAZ6'

# Function to fetch real-time stock price
def get_stock_price(stock_symbol):
    url = f'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': stock_symbol,
        'interval': '5min',  # You can change the interval as per your need
        'apikey': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Parse the latest stock price
    try:
        last_refreshed = data['Meta Data']['3. Last Refreshed']
        stock_price = data['Time Series (5min)'][last_refreshed]['4. close']
        return float(stock_price)
    except KeyError:
        print(f"Error fetching data for {stock_symbol}")
        return None

# Kafka Producer setup
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

stocks = ['AAPL', 'GOOGL', 'AMZN', 'TSLA']

while True:
    stock = random.choice(stocks)  # Randomly select a stock
    price = get_stock_price(stock)
    
    if price:
        data = {'stock': stock, 'price': price}
        producer.send('stock_prices', value=data)
        print(f"Produced: {data}")
    else:
        print(f"Skipping {stock} due to fetch error.")
    
    time.sleep(60)  # Fetch data every 1 minute
