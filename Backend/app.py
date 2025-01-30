from flask import Flask, request, jsonify
import requests
import paho.mqtt.client as mqtt

app = Flask(__name__)

# Configuration MQTT
MQTT_BROKER = "localhost"
MQTT_TOPIC_PUMP = "irrigation/pump"

# Seuil d'humidité
SOIL_MOISTURE_THRESHOLD = 30

# MQTT Client pour publier l'état de la pompe
mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, 1883, 60)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    print(f"Received data: {data}")

    # Envoyer les données vers InfluxDB
    line = f"sensors,location=garden soil_moisture={data['soil_moisture']},temperature={data['temperature']},rain_detected={int(data['rain_detected'])}"
    requests.post("http://localhost:8086/write?db=smart_irrigation", data=line)

    # 🚀 **Contrôle automatique de la pompe**
    pump_status = "OFF"

    if data["soil_moisture"] < SOIL_MOISTURE_THRESHOLD and not data["rain_detected"]:
        pump_status = "ON"
    else:
        pump_status = "OFF"

    print(f"🚰 Pompe d'eau: {pump_status}")
    mqtt_client.publish(MQTT_TOPIC_PUMP, pump_status)  # 🔄 Envoi de la commande via MQTT

    return jsonify({"status": "success", "pump_status": pump_status}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
