
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

# Apply the deployment
```bash
    kubectl apply -f ./deployment.yaml
```


# Port Forward
```bash
    minikube service custom-nginx-service
```
ou
```bash
    kubectl port-forward svc/custom-nginx-service 8080:80
```