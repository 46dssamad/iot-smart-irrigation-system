from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL d'InfluxDB
INFLUXDB_URL = "http://localhost:8086/write?db=smart_irrigation"

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    print(f"Received data: {data}")

    # Convertir les données au format InfluxDB Line Protocol
    line = f"sensors,location=garden soil_moisture={data['soil_moisture']},temperature={data['temperature']},rain_detected={int(data['rain_detected'])}"

    # Envoyer les données à InfluxDB
    try:
        response = requests.post(INFLUXDB_URL, data=line)
        if response.status_code == 204:
            print("Data written to InfluxDB successfully")
        else:
            print(f"Failed to write data: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
