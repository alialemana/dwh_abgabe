# MQTT-Fallstudie in Kubernetes

## Docker-Image 
Der Aufbau des Dockerimages ist in der Ausarbeitung genauer beschrieben. Um es neu zu bilden und in das Repository auf Dockerhub hochzuladen, müssen folgende Befehle ausgeführt werden.

```
docker build -t alialemana/publisher:latest
docker push alialemana/publisher:latest'''
```

## Vorgehen zum Starten des Clusters
### Secret Erstellen
Das Secret wird aus Sicherheitsgründen nicht mit in das öffentliche Repository geladen. Um das Cluster zu starten, muss daher vorher ein Schritt durchgeführt werden. 
In abgabe/postgres/postgres.yaml muss unter postgres-secret der username und das passwort angegeben werden. Kubernetes erwartet es base64 encoded, dafür folgenden Befehl mit selbst gewählten Credentials durchführen. 

```
echo -n '<username>' | base64
echo -n '<password>' | base64
```

### Starten
Nachdem das Secret vervollständigt wurde, kann mit `bash run.bash` der Cluster gestartet werden. Mit `bash destroy.bash` wird das Cluster wieder heruntergefahren. 

## Debuggen
Um beispielsweise zu überprüfen, ob die Daten in die Datenbank eingefügt wurden, folgenden Befehl ausführen, um in den Postgres-Pod zu gelangen.

```
kubectl exec -it <podid> -- psql -U <username> postgres-db
```

Mit `select * from staging.messung` sieht man dann die Daten.

