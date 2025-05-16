# This is the folder structure that you will create locally on your machine. I would advise creating the folder under Documents. But ultimately the choice is up to you. Just know where it is.
```

### Directory Layout

log-aggregator/
├── log-ingest/
│   └── Dockerfile
├── parser/
│   └── Dockerfile
├── search-api/
│   └── Dockerfile
├── frontend/
│   └── Dockerfile
├── manifests/
│   ├── kustomization.yaml
│   ├── log-ingest.yaml
│   ├── parser.yaml
│   ├── search-api.yaml
│   ├── frontend.yaml
│   └── mongodb.yaml
└── README.md
```
### Example commands
```
From Powershell, navigate to where you want it saved and you can use the following commands

mkdir aks-log-aggregator
cd aks-log-aggregator
mkdir log-ingest parser search-api frontend log-generator manifests
