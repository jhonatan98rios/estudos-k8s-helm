# Attemption
Here we have a point of attemption. We need to deploy backend and frontend and make the backend port foward to then do the deploy of frontend again.

# Create a image
```bash
    docker build -t websockets-chat-frontend ./frontend
    docker build -t websockets-chat-backend ./backend
```

# Tag image too use on minukube registry
```bash
    docker tag websockets-chat-frontend 127.0.0.1:5000/websockets-chat-frontend
    docker tag websockets-chat-backend 127.0.0.1:5000/websockets-chat-backend
```

# Push to minukube registry
```bash
    docker push 127.0.0.1:5000/websockets-chat-frontend
    docker push 127.0.0.1:5000/websockets-chat-backend
```

# Install Chart on Kubernetes
```bash
    helm install websockets-chat-helm ./websockets-chat-helm
```

# Port Forward
```bash
    minikube service websockets-chat-helm-backend
```

# Update frontend image
Before to run these commands, update the endpoint of websockets using the port obtained on the previous step

```bash
    docker build -t websockets-chat-frontend ./frontend
```

# Tag image too use on minukube registry
```bash
    docker tag websockets-chat-frontend 127.0.0.1:5000/websockets-chat-frontend
```

# Push to minukube registry
```bash
    docker push 127.0.0.1:5000/websockets-chat-frontend
```

# Updating the chart
```bash
    helm upgrade websockets-chat-helm ./websockets-chat-helm
```

# Force pods to be updated
```bash
    kubectl get pods # Search for the websockets-chat-helm-frontend pod id
    kubectl rm <pod-id> --force
```

# Port Forward
```bash
    minikube service websockets-chat-helm-frontend
```


# Deleting the chart
```bash
    helm delete websockets-chat-helm
```