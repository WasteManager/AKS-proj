# AKS-proj
Comprehensive Guide which documents steps to deploy a full functional log aggregator platform on Azure Kubernetes Service. Includes setup commands, YAML Files, docker configs and troubleshooting


## Prerequisites

### Required Tools

- Docker Desktop
- Node.js (for React frontend)
- Python 3.11+ (for backend and log generator)
- Azure CLI
- kubectl
- Helm
- Chocolatey (optional, for Helm on Windows)

### Install Instructions

```powershell

# Chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Helm
choco install kubernetes-helm -y

# Node.js
choco install nodejs -y

Install Docker Desktop separately: https://www.docker.com/products/docker-desktop

```

### Architecture

```layout
[ Client App / Curl ] 
        ↓
   ┌────────────┐
   │ Log Ingest │ ◄──── External HTTP
   └────────────┘
        ↓
   ┌────────────┐
   │ Parser     │ ◄──── Parses raw logs into JSON format
   └────────────┘
        ↓
   ┌────────────┐
   │ Storage    │ ◄──── MongoDB or PostgreSQL
   └────────────┘
        ↑
   ┌────────────┐
   │ Search API │ ◄──── REST interface to query logs
   └────────────┘
        ↑
   ┌────────────┐
   │ Frontend   │ ◄──── React or plain HTML dashboard
   └────────────┘
```

### Services Breakdown

```Services Breakdown
| Service      | Tech Stack    | Role                                                       |
| ------------ | ------------- | ---------------------------------------------------------- |
| `log-ingest` | FastAPI       | Exposes a `/logs` endpoint to accept logs from clients     |
| `parser`     | Python worker | Normalizes log structure (e.g. timestamp, level, message)  |
| `storage`    | MongoDB       | Stores parsed logs                                         |
| `search-api` | FastAPI       | Provides a `/search` endpoint for querying stored logs     |
| `frontend`   | React or HTML | Simple dashboard to query/search logs and visualize output |




