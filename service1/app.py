from flask import Flask, jsonify
import requests
import random
from prometheus_client import Counter, Gauge, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Métricas para Prometheus
REQUEST_COUNT = Counter('service1_requests_total', 'Total number of /combined requests')
SIMULATED_VALUE = Gauge('service1_simulated_value', 'Simulated value for monitoring')

@app.route('/combined')
def combined():
    REQUEST_COUNT.inc()
    value = random.uniform(0, 100)
    SIMULATED_VALUE.set(value)

    s2 = requests.get("http://service2/info").json()
    s3 = requests.get("http://service3/info").json()

    return jsonify({
        "service": "1",
        "message": "Hola desde el servicio 1",
        "simulated_value": value,
        "from_service2": s2,
        "from_service3": s3
    })

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


