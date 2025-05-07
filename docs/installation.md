# 🚀 Install Fission Locally with Kind, Helm, and Kubectl

This guide walks you through setting up Fission—a serverless framework for Kubernetes—on your local machine using `kind`, `helm`, and `kubectl`.

---

## 🧰 Prerequisites

Ensure you have the following tools installed:

* **kubectl**: Kubernetes command-line tool

  * 📘 [Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

* **helm**: Kubernetes package manager

  * 📘 [Install Helm](https://helm.sh/docs/intro/install/)

* **kind**: Tool for running local Kubernetes clusters using Docker

  * 📘 [Install kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)

* **Docker**: Required by kind to create containerized clusters

  * 📘 [Install Docker](https://docs.docker.com/get-docker/)

---

## 🏗️ Step 1: Create a Local Kubernetes Cluster with Kind

Create a new Kubernetes cluster named `fission-cluster`:

```bash
kind create cluster --name fission-cluster
```

Verify the cluster is running:

```bash
kubectl cluster-info --context kind-fission-cluster
```

---

## 📦 Step 2: Install Fission with Helm

### 1. Create the Fission Namespace

```bash
kubectl create namespace fission
```

### 2. Install Fission CRDs


```bash
kubectl create -k "github.com/fission/fission/crds/v1?ref=v1.20.1"
```

### 3. Add the Fission Helm Repository

```bash
helm repo add fission-charts https://fission.github.io/fission-charts/
helm repo update
```

### 4. Install Fission Using Helm

```bash
helm install --version v1.20.1 --namespace $FISSION_NAMESPACE fission \
  --set serviceType=NodePort,routerServiceType=NodePort \
  fission-charts/fission-all
```

For more details, refer to the [official Fission installation guide](https://fission.io/docs/installation/).([Fission][6])

---

## 🛠️ Step 3: Install the Fission CLI

Download and install the Fission CLI:

```bash
curl -Lo fission https://github.com/fission/fission/releases/download/v1.20.1/fission-v1.20.1-linux-amd64
chmod +x fission
sudo mv fission /usr/local/bin/
```

Replace the URL with the appropriate one for your operating system if you're not using Linux.

---

## ✅ Step 4: Verify the Installation

Check the Fission version:

```bash
fission version
```

Run a health check:

```bash
fission check
```

You should see all components marked as healthy.

---

## 🧪 Step 5: Deploy a Sample Function

### 1. Create a Python Environment

```bash
fission environment create --name python --image fission/python-env
```

### 2. Write a Sample Function

Create a file named `hello.py` with the following content:

```python
def main():
    return "Hello, World from Python!"
```

### 3. Deploy the Function

```bash
fission function create --name hellopy --env python --code hello.py
```

### 4. Create an HTTP Route

```bash
fission route create --method GET --url /hellopy --function hellopy
```

### 5. Access the Function

Retrieve the Fission router service details:

```bash
kubectl --namespace fission get svc router
```

Use the external IP and port to access your function:

```bash
curl http://<FISSION_ROUTER_IP>:<PORT>/hellopy
```

Replace `<FISSION_ROUTER_IP>` and `<PORT>` with the actual values from the previous command.

---

### 6. Keda Installation

Since we are using event driven architecture with kafka, we need to install keda.

#### 1. Install KEDA

```bash
helm repo add kedacore https://kedacore.github.io/charts
helm repo update
kubectl create namespace keda
helm install keda kedacore/keda --namespace keda
```

#### 2.Setup Kafka

Deploy Kafka using Strimzi, which simplifies running Apache Kafka on Kubernetes. Follow the [Strimzi](https://strimzi.io/quickstarts/) installation guide for kind.

---

#### 3. Create kafka topics

Now, create three Kafka topics as mentioned below, replace namespace and cluster with yours.

##### 1. Kafka topic for function invocation

```bash
cat << EOF | kubectl create -n my-kafka-project -f -
apiVersion: kafka.strimzi.io/v1beta1
kind: KafkaTopic
metadata:
  name: request-topic
  labels:
    strimzi.io/cluster: "my-cluster"
spec:
  partitions: 3
  replicas: 2
EOF
```

##### 2. Kafka topic for function response

```bash
cat << EOF | kubectl create -n my-kafka-project -f -
apiVersion: kafka.strimzi.io/v1beta1
kind: KafkaTopic
metadata:
  name: response-topic
  labels:
    strimzi.io/cluster: "my-cluster"
spec:
  partitions: 3
  replicas: 2
EOF
```

##### 3. Kafka topic for error response

```bash
cat << EOF | kubectl create -n my-kafka-project -f -
apiVersion: kafka.strimzi.io/v1beta1
kind: KafkaTopic
metadata:
  name: error-topic
  labels:
    strimzi.io/cluster: "my-cluster"
spec:
  partitions: 3
  replicas: 2
EOF
```


## 📚 Additional Resources

* **Fission Documentation**: [https://fission.io/docs/](https://fission.io/docs/)

* **Fission GitHub Repository**: [https://github.com/fission/fission](https://github.com/fission/fission)([Medium][4])

* **Fission Helm Charts**: [https://artifacthub.io/packages/helm/fission-charts/fission-all](https://artifacthub.io/packages/helm/fission-charts/fission-all)([Artifact Hub][9])

---

This setup provides a local environment to develop and test serverless functions using Fission on Kubernetes. For production deployments, consider using a managed Kubernetes service and follow best practices for scalability and security.([Medium][4])

---

[1]: https://kubernetes.io/blog/2016/10/helm-charts-making-it-simple-to-package-and-deploy-apps-on-kubernetes/?utm_source=chatgpt.com "Helm Charts: making it simple to package and deploy ... - Kubernetes"
[2]: https://kind.sigs.k8s.io/docs/user/quick-start/?utm_source=chatgpt.com "Quick Start - kind - Kubernetes"
[3]: https://gitlab.unimelb.edu.au/feit-comp90024/comp90024/-/blob/master/installation/README.md?utm_source=chatgpt.com "installation/README.md · master · COMP90024 ... - GitLab"
[4]: https://medium.com/%40mr.gmanojkumar/deploying-and-running-python-functions-with-fission-on-kubernetes-47129a81761a?utm_source=chatgpt.com "Deploying and Running Python Functions with Fission on Kubernetes"
[5]: https://github.com/fluxcd/flux2/discussions/1783?utm_source=chatgpt.com "Cannot install fission helm using flux · fluxcd flux2 · Discussion #1783"
[6]: https://fission.io/docs/installation/?utm_source=chatgpt.com "Installing Fission"
[7]: https://kubernetes.io/blog/2017/01/fission-serverless-functions-as-service-for-kubernetes/?utm_source=chatgpt.com "Fission: Serverless Functions as a Service for Kubernetes"
[8]: https://github.com/fission/fission-workflows/blob/master/INSTALL.md?utm_source=chatgpt.com "fission-workflows/INSTALL.md at master - GitHub"
[9]: https://artifacthub.io/packages/helm/fission-charts/fission-all?utm_source=chatgpt.com "fission-all - Helm chart - Artifact Hub"
