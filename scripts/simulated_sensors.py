import random
import time
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC_SENSORS = "irrigation/sensors"
TOPIC_PUMP = "irrigation/pump"

# Variable pour stocker l'état de la pompe
pump_status = "OFF"

def on_message(client, userdata, msg):
    global pump_status
    pump_status = msg.payload.decode()
    print(f"🚰 Pompe mise à jour: {pump_status}")

def simulate_sensor_data():
    soil_moisture = round(random.uniform(10, 50), 2)
    
    # Si la pompe est activée, l'humidité augmente légèrement
    if pump_status == "ON":
        soil_moisture += random.uniform(5, 10)

    return {
        "soil_moisture": min(soil_moisture, 100),  # Max à 100%
        "temperature": round(random.uniform(20, 35), 2),
        "rain_detected": random.choice([True, False])
    }

def publish_data(client):
    while True:
        data = simulate_sensor_data()
        client.publish(TOPIC_SENSORS, str(data))
        print(f"Published: {data}")
        time.sleep(5)

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(BROKER, PORT)
    client.subscribe(TOPIC_PUMP)  # Écoute des commandes de la pompe
    client.loop_start()
    
    publish_data(client)
