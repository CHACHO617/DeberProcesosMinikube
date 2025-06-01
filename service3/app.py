from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/info')
def info():
    return jsonify({"service": "3", "message": "Hola desde el servicio 3"})  # Cambia a 3 en service3

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
