from kafka import KafkaProducer
import json

# Kafka producer instance
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def place_order(order_data):
    producer.send('order_topic', order_data)
    print(f"Order sent to queue: {order_data}")

# Example Order
order = {"order_id": 1, "user_id": 123, "product_id": 456, "quantity": 2}
place_order(order)
