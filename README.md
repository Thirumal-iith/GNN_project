# GNN_project

A **Graph Neural Network (GNN)** project designed for deployment on **Kubeflow** and **Kubernetes**, created as part of the **BRICS** pipeline integration.  
This repo enables end-to-end training, serving, and scaling of GNN models inside a cloud-native ML pipeline.

---

## 📌 Overview

The project implements a GNN model and provides the necessary components to:

- Containerize the training and inference pipeline  
- Deploy to **Kubeflow Pipelines** for orchestration  
- Run on **Kubernetes** for scalable and reproducible ML workflows  
- Support modular experimentation and CI/CD integration  

---

## 🚀 Features

- End-to-end GNN pipeline (training → evaluation → inference)  
- Dockerized setup for portability  
- Integration with Kubeflow Pipelines  
- Scalable deployment on Kubernetes cluster  
- Modular code for future GNN variants  

---

## 📂 Repository Structure

GNN_project/
├── src/ # GNN model code and utilities
├── pipeline/ # Kubeflow pipeline components & definitions
├── k8s/ # Kubernetes manifests (YAML)
├── Dockerfile # Container image definition
├── requirements.txt # Python dependencies
├── pyproject.toml # Project configuration
├── notebooks/ # Jupyter notebooks for testing/debugging
├── .gitignore
└── README.md

yaml
Copy code

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Thirumal-iith/GNN_project.git
cd GNN_project
Create and activate a virtual environment (optional):

bash
Copy code
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt


## ▶️ Usage
🔹 Local Development
Run the training locally:

bash
Copy code
python src/train.py --config configs/config.yaml
🔹 Build Docker Image
bash
Copy code
docker build -t gnn-project:latest .
🔹 Push to Registry
bash
Copy code
docker tag gnn-project:latest <registry-url>/gnn-project:latest
docker push <registry-url>/gnn-project:latest
🔹 Deploy on Kubernetes
Apply manifests from the k8s/ folder:

bash
Copy code
kubectl apply -f k8s/
🔹 Run with Kubeflow Pipelines
Upload or compile the pipeline definition:

bash
Copy code
dsl-compile --py pipeline/gnn_pipeline.py --output gnn_pipeline.yaml
Then, run the pipeline from the Kubeflow Pipelines dashboard.



## 📦 Requirements
Python (see .python-version or requirements.txt)

Docker

Kubernetes cluster (minikube, kind, or cloud provider)

Kubeflow Pipelines installed on the cluster




## 🗂️ Data
Place datasets in data/ or mount from external storage

Format depends on the GNN task (e.g., node classification, link prediction, graph classification)



## 🤝 Contributing
Contributions are welcome!

Fork the repository

Create a new branch (git checkout -b feature-xyz)

Commit and push your changes

Open a Pull Request
