
# Create a image
```bash
    docker build -t flask-app .
```

# Run the container
```bash
    docker run -p 8080:8080 flask-app
```    

# Tag image too use on minukube registry
```bash
    docker tag flask-app 127.0.0.1:5000/flask-app
```

# Push to minukube registry
```bash
    docker push 127.0.0.1:5000/flask-app
```

# Apply the deployment
```bash
    kubectl apply -f ./deployment.yaml
```


# Port Forward
```bash
    minikube service flask-app-service
```

ou 

```bash
    kubectl port-forward svc/flask-app-service 8080:80
```