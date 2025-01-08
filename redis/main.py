import reids
import json
import psycopg2

# connect to Redis
cache = redis.Redis(host='localhost', port=6379, db=0)

# Connect to PostgreSQL
conn = psycopg2.connect()

def get_product(product_id):
    # check cache first
    cached_product = cache.get(product_id)
    if cached_product:
        print("Cache hit")
        return json.load(cached_product)

    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE id = %s", (product_id))
    product = cur.fetchone()

    if product:
        cache.set(product_id, json.dumps(product), ex=3600)
