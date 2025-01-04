
# Create a image
```bash
    docker build -t websockets-helm .
```

# Tag image too use on minukube registry
```bash
    docker tag websockets-helm 127.0.0.1:5000/websockets-helm
```

# Push to minukube registry
```bash
    docker push 127.0.0.1:5000/websockets-helm
```

<!-- # Create a chart
Executar somente uma vez
```bash
    helm create websockets-helm
``` -->

# Install Chart on Kubernetes
```bash
    helm install websockets-helm ./websockets-helm
```

# Port Forward
```bash
    minikube service websockets-helm
```
ou
```bash
    kubectl port-forward svc/websockets-helm 8080:80
```

# Updating the chart
```bash
    helm upgrade websockets-helm ./websockets-helm
```

# Deleting the chart
```bash
    helm delete websockets-helm
```