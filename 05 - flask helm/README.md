
# Create a image
```bash
    docker build -t flask-helm .
```

# Run the container
```bash
    docker run -p 8080:8080 flask-helm
```    

# Tag image too use on minukube registry
```bash
    docker tag flask-helm 127.0.0.1:5000/flask-helm
```

# Push to minukube registry
```bash
    docker push 127.0.0.1:5000/flask-helm
```

# Install Chart on Kubernetes
```bash
    helm install flask-helm ./flask-helm
```

# Port Forward
```bash
    minikube service flask-helm
```
ou
```bash
    kubectl port-forward svc/flask-helm 8080:80
```

# Updating the chart
```bash
    helm upgrade flask-helm ./flask-helm
```

# Deleting the chart
```bash
    helm delete flask-helm
```