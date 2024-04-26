import paho.mqtt.client as mqtt
import json
import time
import random
import os 

# Get broker-name from environment, in this case the mosquitto-broker-service
broker = os.getenv("BROKER")

# Log-Callback Function
def on_log(client, userdata, paho_log_level, messages):
    if paho_log_level == mqtt.LogLevel.MQTT_LOG_ERR:
        print(message)

# Connect-Callback Function
def on_connect(client, userdata, flags, reason_code):
    if reason_code.is_failure:
        print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
    else:
        print("connected")

# Publish-Callback Function
def on_publish(client, userdata, mid):
    print("PUBACK erhalten für Nachricht mit id", mid)

# Initialize MQTT Client with specified ID
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "publisherID-lksadhouivhlefhiuvuk7388490fshsdlfviop", clean_session=False)
# Connect to Broker
mqttc.connect(broker, 1883, 60)
# Start loop
mqttc.loop_start()

# as debugging, message are counted
msg_count=1
while True:
    # sent payload
    jsonPayload = {
        "fin": "SNTU411STM9032444",
        "zeit": int(time.time()),
        "geschwindigkeit": random.randint(0, 50),
    }
    # stores the answer of publishing in results
    results = mqttc.publish("DataMgmt", json.dumps(jsonPayload), qos=1)
    status = results[0]
    if status == 0:
        print(f"Sent `{jsonPayload}`to topic", msg_count, results[1])
    else:
        print("sending failed")
    msg_count +=1
    mqttc.on_publish
    mqttc.on_log
    print("gesendet")
    time.sleep(5)
