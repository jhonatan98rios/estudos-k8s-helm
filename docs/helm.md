# Helm 
    é uma ferramenta de gerenciamento de pacotes para Kubernetes. Ele usa pacotes chamados charts para definir, instalar e gerenciar aplicações Kubernetes. Os componentes principais do Helm são:

### Charts
    Charts são pacotes que contêm todos os recursos Kubernetes necessários para instalar e executar uma aplicação.
    Cada chart tem a estrutura de diretórios específica e arquivos que descrevem o que será criado no cluster Kubernetes.
    
### Templates
    Dentro de um chart, você tem templates de recursos do Kubernetes (como Deployment, Service, etc.) que são arquivos YAML com placeholders.
    O Helm irá substituir esses placeholders por valores reais quando o chart for instalado.

### Values
    values.yaml é o arquivo que contém as variáveis que podem ser configuradas no Helm.
    Ele permite personalizar o comportamento de um chart, substituindo valores nos templates.

### Release
    Quando você instala um chart com o Helm, ele cria um release. O release é uma instância do chart que foi configurada e instalada no cluster Kubernetes.
    
### Repositórios
    Helm também permite armazenar charts em repositórios, o que facilita o compartilhamento e o gerenciamento de charts.