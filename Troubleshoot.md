# If getting the following error
```
 Error from server (Forbidden): error when creating "https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.9.4/deploy/static/provider/cloud/deploy.yaml": admission webhook "validation.gatekeeper.sh" denied the request: [azurepolicy-k8sazurev1loadbalancernopublic-cecdfeacd5ad9b6d8417] Load Balancers should not have public IPs. azure-load-balancer-internal annotation is required for ingress-nginx-controller
```

  - Deploy ingress-NGINX with internal load balancer in AKS
  ```
Create new namespace
Apply a modified Ingress deployment with the internal LB annotation
```

  - Create ingress-nginx namespace
```
kubectl create namespace ingress-nginx
```
  - Create internal load balance configmap
```
Create a ingress-internal.yaml in manifests folder
```

  - Deploy NGINX Ingress with Internal LB
```
  - Ensure you have helm installed
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update

helm upgrade --install ingress-nginx ingress-nginx/ingress-nginx `
  --namespace ingress-nginx `
  --create-namespace `
  --set controller.service.annotations."service\.beta\.kubernetes\.io/azure-load-balancer-internal"="true"

  - Ensure you have chocolatey installed
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

  - 
