from kafka import KafkaConsumer
import sqlite3
import json

consumer = KafkaConsumer('stock_prices', bootstrap_servers='localhost:9092', value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Connect to SQLite database (or create it)
conn = sqlite3.connect('stocks.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS stock_prices (stock TEXT, price REAL)''')
conn.commit()

print("Listening for messages...")

for message in consumer:
    data = message.value
    print(f"Consumed: {data}")
    cursor.execute('INSERT INTO stock_prices (stock, price) VALUES (?, ?)', (data['stock'], data['price']))
    conn.commit()

