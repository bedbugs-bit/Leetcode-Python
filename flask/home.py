from crypt import methods

from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)



# Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/products/<product_id>', methods=['GET'])
def product(product_id):
    REQUEST_COUNT.labels(methods='GET', endpoint = '/products/<product_id>').inc()

    return jsonify({"product_id": product_id})

if __name__ == "__main__":
    app.run(port=5000)