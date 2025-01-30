# 🌱 Smart Irrigation System - IoT & Data Visualization 🌍💧

## 📌 Description
Ce projet simule un **système d'irrigation intelligent** basé sur des capteurs de sol et des prévisions météorologiques. Il utilise **MQTT** pour la communication entre capteurs et backend, **InfluxDB** pour le stockage des données, et **Grafana** pour la visualisation.

---

## 🚀 Installation et Configuration

📌 Explication des Dépendances
Package	Utilité
Flask	Gère le serveur backend et les requêtes HTTP.
paho-mqtt	Permet la communication via MQTT avec le broker Mosquitto.
requests	Utilisé pour envoyer des requêtes HTTP à l'API météo et à InfluxDB.
influxdb	Permet d'interagir avec la base de données InfluxDB.

### 1️⃣ **Prérequis**
- **Python 3.x**
- **Git**
- **Mosquitto (MQTT Broker)**
- **InfluxDB**
- **Grafana**
- **Virtualenv (optionnel, recommandé)**

### 2️⃣ **Cloner le projet**
```bash
git clone https://github.com/votre_nom_utilisateur/smart_irrigation.git
cd smart_irrigation
