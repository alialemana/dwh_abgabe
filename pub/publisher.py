import paho.mqtt.client as mqtt
import json
import time
import random


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "lksadhouivhlefhiuvuk7388490fshsdlfviop", clean_session=False)
mqttc.connect("broker.hivemq.com", 1883, 60)

while True:
    
    jsonPayload = {
        "fin": "SNTU411STM9032444",
        "zeit": int(time.time()),
        "geschwindigkeit": random.randint(0, 50),
    }
    mqttc.publish("ping", json.dumps(jsonPayload), qos=1)
    time.sleep(5)
