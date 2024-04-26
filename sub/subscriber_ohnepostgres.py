import psycopg2
import os
import paho.mqtt.client as mqtt
from datetime import datetime

db_password = os.getenv("DB_PASSWORD")
broker = os.getenv("BROKER")
def on_message(client, userdata, message):
    print("empfangene Nachricht: " + str(message.payload.decode("utf-8")))
    try:   
        timestamp = datetime.now()
        print("Nachricht erfolgreich in die Datenbank eingefügt.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Fehler beim Einfügen der Nachricht in die Datenbank:", error)

# Herstellen der Verbindung zum MQTT Broker und subscriben
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="subscriberID-jlkiolososssiHSOFLi", clean_session=False)
mqttc.on_message = on_message
mqttc.connect("127.0.0.1", 1883, 60)
mqttc.subscribe("DataMgmt", qos=1)
mqttc.loop_forever()
cur.close()
conn.close()

