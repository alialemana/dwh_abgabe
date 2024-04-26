import psycopg2
import os
import paho.mqtt.client as mqtt
from datetime import datetime

db_password = os.getenv("POSTGRES_PASSWORD")
broker = os.getenv("BROKER")
database = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")

# Verbindung zur Datenbank herstellen
conn = psycopg2.connect(
database=database, 
user=user,
host="postgres",
port=5432,
password=db_password)

print("Connected to database")

cur = conn.cursor()

table_sql = """
DROP SCHEMA IF EXISTS staging CASCADE;
CREATE SCHEMA staging;
CREATE TABLE staging.messung (
messung_id SERIAL,
payload JSON NOT NULL,
empfangen TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
CONSTRAINT pk_messung PRIMARY KEY(messung_id));
"""

cur.execute(table_sql)
conn.commit()

def on_message(client, userdata, message):
    print("empfangene Nachricht: " + str(message.payload.decode("utf-8")))
    try:   
        timestamp = datetime.now()

        # SQL-Befehl zum Einfügen der Nachricht in die Tabelle
        sql = """
        INSERT INTO staging.messung(messung_id, payload, empfangen) VALUES (DEFAULT, %s, %s);
        """

        # Ausführen des Befehls
        cur.execute(sql, (message.payload.decode("utf-8"),timestamp)) 
        conn.commit()
        print("Nachricht erfolgreich in die Datenbank eingefügt.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Fehler beim Einfügen der Nachricht in die Datenbank:", error)

# Herstellen der Verbindung zum MQTT Broker und subscriben
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="subscriberID-jlkiolososssiHSOFLi", clean_session=False)
mqttc.on_message = on_message
mqttc.connect(broker, 1883, 60)
mqttc.subscribe("DataMgmt", qos=1)
mqttc.loop_forever()
cur.close()
conn.close()
