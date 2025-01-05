# Inicializar o minikube
minikube start

# Habilitar o registry do minikube como principal durante o uso o terminal (ao abri um novo terminal precisa ser executado novamente)
minikube addons enable registry
minikube docker-env 
& minikube -p minikube docker-env --shell powershell | Invoke-Expression