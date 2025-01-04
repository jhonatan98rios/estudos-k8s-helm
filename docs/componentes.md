# Pods
    Descrição: A menor unidade executável no Kubernetes. Representa uma ou mais containers que compartilham o mesmo namespace de rede e volume de armazenamento.
    Função: Gerenciar a execução de containers, garantindo que eles sejam agrupados logicamente para funcionar juntos.

# ReplicaSets
    Descrição: Um controlador que garante que um número específico de réplicas de um pod esteja sempre em execução.
    Função: Oferece escalabilidade e tolerância a falhas ao manter o número desejado de réplicas. É frequentemente gerenciado indiretamente por um Deployment.

# Deployments
    Descrição: Um controlador de nível superior que gerencia ReplicaSets e, consequentemente, Pods.
    Função: Facilita operações como atualizações contínuas, rollback e escalabilidade. Permite definir o estado desejado da aplicação.

# Services
    Descrição: Um recurso que expõe um conjunto de Pods como um único serviço, permitindo comunicação estável entre componentes.

## Tipos:
    ClusterIP: Acesso interno dentro do cluster.
    NodePort: Exposição em uma porta específica de cada nó.
    LoadBalancer: Integração com balanceadores de carga externos.
    ExternalName: Mapeia para um nome DNS externo.

# Ingress
    Descrição: Um recurso que gerencia o acesso HTTP/S externo aos serviços do cluster.
    Função: Oferece roteamento baseado em URLs, suporte a TLS e balanceamento de carga por meio de controladores Ingress.

# ConfigMaps
    Descrição: Um objeto usado para armazenar dados de configuração não sensíveis em formato de pares chave-valor.
    Função: Facilita a injeção de configurações em Pods, mantendo-os desacoplados de configurações específicas.

# Secrets
    Descrição: Um objeto usado para armazenar dados sensíveis, como senhas, tokens e chaves de API.
    Função: Protege informações confidenciais, permitindo que sejam usadas de maneira segura pelos Pods.

# Namespaces
    Descrição: Divisões lógicas dentro de um cluster Kubernetes.
    Função: Facilita a organização e o isolamento de recursos, permitindo o gerenciamento eficiente de múltiplos ambientes ou equipes.

# PersistentVolumes (PV) e PersistentVolumeClaims (PVC)

## PersistentVolumes (PV):
    Descrição: Representam volumes de armazenamento provisionados no cluster.
    Função: Abstraem o armazenamento subjacente (e.g., NFS, EBS, GCP Disk).

## PersistentVolumeClaims (PVC):
    Descrição: Solicitações de armazenamento feitas pelos Pods.
    Função: Conecta um Pod a um PV disponível.

# StatefulSets
    Descrição: Um controlador para gerenciar Pods que requerem identidade persistente (e.g., bancos de dados).
    Função: Garante ordens específicas de criação, exclusão e atualização de Pods, além de nomes consistentes e armazenamento persistente.

# DaemonSets
    Descrição: Um controlador que garante que uma cópia de um Pod seja executada em todos (ou em um subconjunto) dos nós do cluster.
    Função: Usado para tarefas específicas de nó, como logging, monitoramento e configurações de rede.

# Jobs e CronJobs
## Jobs:
    Descrição: Um recurso para execução de tarefas únicas ou limitadas.
    Função: Garante que um número específico de execuções de Pods seja concluído com sucesso.
## CronJobs:
    Descrição: Tarefas agendadas que criam Jobs periodicamente.
    Função: Ideal para execuções repetitivas baseadas em cron (e.g., backups diários).

# Horizontal Pod Autoscaler (HPA)
    Descrição: Um recurso para escalabilidade automática de Pods com base em métricas como uso de CPU/memória.
    Função: Ajusta dinamicamente o número de réplicas de Pods para atender à demanda.

# ClusterRoles e RoleBindings
    Função: Controlam quem pode acessar o quê dentro do cluster, utilizando o modelo RBAC (Role-Based Access Control).

## ClusterRoles:
    Descrição: Define permissões de acesso a recursos no nível do cluster.
    
## RoleBindings:
    Descrição: Associa usuários, grupos ou contas de serviço a Roles ou ClusterRoles.