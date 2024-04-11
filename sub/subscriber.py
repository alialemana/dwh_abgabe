import os
import paho.mqtt.client as mqtt
from datetime import datetime

def on_message(client, userdata, message):
    print("empfangene Nachricht: " + str(message.payload.decode("utf-8")))

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="subscriberID-jlkiolososssiHSOFLi", clean_session=False)
mqttc.on_message = on_message
mqttc.connect("broker.hivemq.com", 1883, 60)
mqttc.subscribe("ping", qos=1)
mqttc.loop_forever()
