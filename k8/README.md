# to run this image on k8 (kubernetes) locally
note: ensure you update the tag in deployment.yaml

### startup
1. cd into k8
2. start docker
3. run ```minikube start``` (in cmd or bash)

### apply the configuration
1. run ```kubectl apply -f trino-nlp-embeddings-deployment.yaml```
2. run ```kubectl apply -f trino-nlp-embeddings-service.yaml```

### verify they're running
kubectl get pods (should say running)
kubectl get services (note there's no load balancer on local deployments)

### now port forward (since nodeport is not working for some reason)
kubectl port-forward service/trino-nlp-embeddings 8080:8080

### now access your trino service through your browser
http://localhost:8080