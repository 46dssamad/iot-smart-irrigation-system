from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Endpoint pour recevoir les données
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    print(f"Received data: {data}")
    # Vous pouvez ajouter ici des règles logiques pour contrôler la pompe
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
