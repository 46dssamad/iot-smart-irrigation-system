import paho.mqtt.client as mqtt
import requests

BROKER = "localhost"
PORT = 1883
TOPIC_SENSORS = "irrigation/sensors"
TOPIC_PUMP = "irrigation/pump"
FLASK_ENDPOINT = "http://localhost:5000/data"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker!")
    client.subscribe(TOPIC_SENSORS)
    client.subscribe(TOPIC_PUMP)  # 🔄 Écoute des commandes pour la pompe

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    topic = msg.topic

    if topic == TOPIC_SENSORS:
        print(f"Received from MQTT: {payload}")
        requests.post(FLASK_ENDPOINT, json=eval(payload))

    elif topic == TOPIC_PUMP:
        print(f"🚰 Pompe: {payload}")  # Affiche l'état de la pompe reçu depuis Flask

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT)
    client.loop_forever()
