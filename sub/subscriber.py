import psycopg2
import os
import paho.mqtt.client as mqtt
from datetime import datetime

db_password = os.getenv("DB_PASSWORD")
broker = os.getenv("BROKER")
# Verbindung zur Datenbank herstellen

conn = psycopg2.connect(
database="postgres-db", 
user="postgres-user",
host="postgres",
port=5432,
password=db_password)

print("Connected to database")

cur = conn.cursor()


def on_message(client, userdata, message):
    print("empfangene Nachricht: " + str(message.payload.decode("utf-8")))
    try:   
        timestamp = datetime.now()

        # SQL-Befehl zum Einfügen der Nachricht in die Tabelle
        sql = "INSERT INTO staging.messung(messung_id, payload, empfangen) VALUES (DEFAULT, %s, %s);"
        cur.execute(sql, (message.payload.decode("utf-8"),timestamp)) 
        conn.commit()        
        print("Nachricht erfolgreich in die Datenbank eingefügt.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Fehler beim Einfügen der Nachricht in die Datenbank:", error)

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="subscriberID-jlkiolososssiHSOFLi", clean_session=False)
mqttc.on_message = on_message
mqttc.connect(broker, 1883, 60)
mqttc.subscribe("DataMgmt", qos=1)
mqttc.loop_forever()
cur.close()
conn.close()
