# MQTT-Fallstudie in Kubernetes

## Docker-Image 
Das Dockerfile sieht folgendermaßen aus:

docker build -t alialemana/publisher:latest
docker push alialemana/publisher:latest


~/Documents/lectures/dhbw-dwh/abgabe$ kubectl exec -it postgres-665b7554dc-69gds -- psql -U postgres-user postgres-db
