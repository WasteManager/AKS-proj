# What is being deployed
```
| Component    | Port  | Type         | Notes                                     |
| ------------ | ----- | ------------ | ----------------------------------------- |
| `log-ingest` | 8000  | ClusterIP    | Receives logs and forwards to parser      |
| `parser`     | 8001  | ClusterIP    | Parses logs and stores in MongoDB         |
| `search-api` | 8002  | ClusterIP    | Queries logs from MongoDB                 |
| `frontend`   | 3000  | LoadBalancer | React app for user interface              |
| `mongodb`    | 27017 | ClusterIP    | Shared MongoDB instance for parser/search |
```

  -  Configure/copy all of the YAML files directly into the manifests folder
  -  Once all of the YAML files are saved we will deploy to AKS

# Deploy to AKS
```
# Ensure that the terminal is in the manifests folder

cd "$env:USERPROFILE\Documents\aks-log-aggregator\manifests"
kubectl apply -k .

# Check that it is working
kubectl get pods,svc

# Look for external IP of frontend service
kubectl get service frontend




