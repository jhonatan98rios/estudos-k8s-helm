
# Create a image
```bash
    docker build -t custom-nginx .
```

# Run the container
```bash
    docker run -it --rm -d -p 8080:80 --name custom-nginx custom-nginx
```    

# Tag image too use on minukube registry
```bash
    docker tag custom-nginx localhost:5000/custom-nginx
```

# Push to minukube registry
```bash
    docker push localhost:5000/custom-nginx
```

# Install Chart on Kubernetes
```bash
    helm install nginx-helm ./nginx-helm
```

# Port Forward
```bash
    minikube service nginx-helm
```
ou
```bash
    kubectl port-forward svc/nginx-helm-service 8080:80
```

# Updating the chart
```bash
    helm upgrade nginx-helm ./nginx-helm
```

# Deleting the chart
```bash
    helm delete nginx-helm
```