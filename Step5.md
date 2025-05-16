# Add ingress controller to AKS
  - Install NGINX
    ```
    kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.9.4/deploy/static/provider/cloud/deploy.yaml
    ```
- It will create:

  - A nginx-ingress-controller service of type LoadBalancer

  - All necessary roles, config maps, and webhooks
 
- Wait for external IP
```
- kubectl get service ingress-nginx-controller -n ingress-nginx
```

  - Create ingress resource: You will create a yaml file in the manifests folder

  - Apply the ingress yaml
```
kubectl apply -f ingress.yaml
```


