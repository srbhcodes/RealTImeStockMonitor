from kafka import KafkaProducer
import random
import time
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

stocks = ['AAPL', 'GOOGL', 'AMZN', 'TSLA']

while True:
    stock = random.choice(stocks)
    price = round(random.uniform(100, 1500), 2)
    data = {'stock': stock, 'price': price}
    producer.send('stock_prices', value=data)
    print(f"Produced: {data}")
    time.sleep(2)

