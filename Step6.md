# create a small log spammer app that continuously POSTs fake logs to log-ingest

  - Create a log-generator folder under the aks-log-aggregator folder
  - Create the dockerfile and main.py files in the log-generator folder
  - Build and push
```
docker build -t logaggregatoracr.azurecr.us/log-generator:v1 ./log-generator
docker push logaggregatoracr.azurecr.us/log-generator:v1
```
  - Deploy Log Generator to Kubernetes
```
  - Create the Yaml file in manifests folder
```
  - Apply
```
  kubectl apply -f log-generator.yaml
```

