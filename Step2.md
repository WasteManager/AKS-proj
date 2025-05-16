# Building Docker Images and push to ACR

  - Ensure docker installed and running
  - Ensure you are logged into Azure via power shell (Az login)
  - Pay attention to which subscription you are in, and if you have already created a resource group

# Create Resource Group
```
az group create --name log-aggregator-rg --location eastus
```

# Create ACR via powershell
```
az acr create --name logaggregatoracr --resource-group log-aggregator-rg --sku Basic
az acr login --name logaggregatoracr
```
# Get ACR login Server
```
az acr show --name logaggregatoracr --query loginServer --output tsv

```
# Build Docker images with correct tags. Ensure the ouput from the step above is what you input when you build (logaggregatoracr.azurecr.io should essentially be it)
```
# log-ingest
docker build -t logaggregatoracr.azurecr.io/log-ingest:v1 ./log-ingest

# parser
docker build -t logaggregatoracr.azurecr.io/parser:v1 ./parser

# search-api
docker build -t logaggregatoracr.azurecr.io/search-api:v1 ./search-api

# frontend
docker build -t logaggregatoracr.azurecr.io/frontend:v1 ./frontend
```

# Push images to ACR
```
docker push logaggregatoracr.azurecr.io/log-ingest:v1
docker push logaggregatoracr.azurecr.io/parser:v1
docker push logaggregatoracr.azurecr.io/search-api:v1
docker push logaggregatoracr.azurecr.io/frontend:v1
```

# Create AKS cluster
```
# Create Resource Group if not already created
az group create --name log-aggregator-rg --location usgovvirginia

# Create AKS Cluster

az aks create `
  --name log-aggregator-aks `
  --resource-group log-aggregator-rg `
  --node-count 2 `
  --enable-managed-identity `
  --generate-ssh-keys
```



# Attach ACR to AKS
```
az aks update \
  --name log-aggregator-aks \
  --resource-group log-aggregator-rg \
  --attach-acr logaggregatoracr

```

# Connect Kubectl to Cluster
```
az aks get-credentials `
  --name log-aggregator-aks `
  --resource-group log-aggregator-rg

```

