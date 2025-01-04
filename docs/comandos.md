# Comandos Gerais

Exibir a versão do Kubernetes:
```bash
kubectl version
```

Listar informações do cluster:
```bash
kubectl cluster-info
```

Ver os nós do cluster:
```bash
kubectl get nodes
```

# Trabalhando com Pods

Listar Pods em um namespace:
```bash
kubectl get pods -n <namespace>
```

Obter detalhes de um Pod:
```bash
kubectl describe pod <pod-name> -n <namespace>
```

Visualizar logs de um Pod:
```bash
kubectl logs <pod-name>
```

Acessar um Pod interativamente:
```bash
kubectl exec -it <pod-name> -- /bin/bash
```

# Trabalhando com Deployments

Listar Deployments:
```bash
kubectl get deployments
```

Criar ou aplicar um Deployment a partir de um arquivo YAML:
```bash
kubectl apply -f <file.yaml>
```

Atualizar o número de réplicas:
```bash
kubectl scale deployment <deployment-name> --replicas=<number>
```

Realizar rollback de um Deployment:
```bash
kubectl rollout undo deployment <deployment-name>
```

# Verificar o status do Deployment:

```bash
kubectl rollout status deployment <deployment-name>
```

# Trabalhando com Services

Listar Services:
```bash
kubectl get services
```

Criar ou aplicar um Service a partir de um arquivo YAML:
```bash
kubectl apply -f <file.yaml>
```

Obter detalhes de um Service:
```bash
kubectl describe service <service-name>
```

# Trabalhando com ConfigMaps e Secrets

Listar ConfigMaps:
```bash
kubectl get configmaps
```

Criar um ConfigMap:
```bash
kubectl create configmap <configmap-name> --from-literal=<key>=<value>
```

Listar Secrets:
```bash
kubectl get secrets
```

Criar um Secret a partir de pares chave-valor:
```bash
kubectl create secret generic <secret-name> --from-literal=<key>=<value>
```

# Trabalhando com Namespaces

Listar Namespaces:
```bash
kubectl get namespaces
```

Criar um Namespace:
```bash
kubectl create namespace <namespace-name>
```

Usar um Namespace por padrão:
```bash
kubectl config set-context --current --namespace=<namespace-name>
```

# Trabalhando com PersistentVolumes (PV) e Claims (PVC)

Listar PersistentVolumes:
```bash
kubectl get pv
```

Listar PersistentVolumeClaims:
```bash
kubectl get pvc
```

# Debug e Monitoramento

Inspecionar recursos com detalhes em YAML/JSON:
```bash
kubectl get <resource-type> <resource-name> -o yaml
kubectl get <resource-type> <resource-name> -o json
```

Monitorar eventos do cluster:
```bash
kubectl get events
```

Observar mudanças em tempo real:
```bash
kubectl get pods -w
```

# Trabalhando com Recursos YAML

Validar um arquivo YAML sem aplicá-lo:
```bash
kubectl apply --dry-run=client -f <file.yaml>
```

Excluir um recurso definido em um arquivo YAML:
```bash
kubectl delete -f <file.yaml>
```

# Comandos de Escalabilidade

Escalar um Deployment horizontalmente:
```bash
kubectl scale deployment <deployment-name> --replicas=<number>
```

Habilitar Auto Scaling para um Deployment:
```bash
kubectl autoscale deployment <deployment-name> --cpu-percent=<threshold> --min=<min-replicas> --max=<max-replicas>
```

# Trabalhando com Ingress

Listar Ingresses:
```bash
kubectl get ingress
```

Obter detalhes de um Ingress:
```bash
kubectl describe ingress <ingress-name>
```

# Exclusão de Recursos

Deletar um recurso específico:
```bash
kubectl delete <resource-type> <resource-name>
```

Deletar todos os Pods em um Namespace:
```bash
kubectl delete pods --all -n <namespace>
```