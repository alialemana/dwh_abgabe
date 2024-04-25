import paho.mqtt.client as mqtt
import json
import time
import random
import os 

broker = os.getenv("BROKER")
FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60

def on_log(client, userdata, paho_log_level, messages):
    if paho_log_level == mqtt.LogLevel.MQTT_LOG_ERR:
        print(message)
def on_connect(client, userdata, flags, reason_code):
    if reason_code.is_failure:
        print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
    else:
        # we should always subscribe from on_connect callback to be sure
        # our subscribed is persisted across reconnections.
        print("connected")
def on_disconnect(client, userdata, rc):
    logging.info("Disconnected with result code: %s", rc)
    reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
    while reconnect_count < MAX_RECONNECT_COUNT:
        logging.info("Reconnecting in %d seconds...", reconnect_delay)
        time.sleep(reconnect_delay)
def on_publish(client, userdata, mid):
    print("PUBACK erhalten für Nachricht mit id", mid)

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "publisherID-lksadhouivhlefhiuvuk7388490fshsdlfviop", clean_session=False)
mqttc.connect(broker, 1883, 60)
msg_count=1
while True:
    
    jsonPayload = {
        "fin": "SNTU411STM9032444",
        "zeit": int(time.time()),
        "geschwindigkeit": random.randint(0, 50),
    }
    results = mqttc.publish("DataMgmt", json.dumps(jsonPayload), qos=0)
    status = results[0]
    if status == 0:
        print(f"Sent `{jsonPayload}`to topic", msg_count, results[1])
    else:
        print("sending failed")
    msg_count +=1
    mqttc.on_publish
    mqttc.on_disconnect
    mqttc.on_log
    print("gesendet")
    time.sleep(5)
