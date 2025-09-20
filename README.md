# AI Orchestration & Safety Layer
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi)
![LangChain](https://img.shields.io/badge/Framework-LangChain-2E86C1)
![Guardrails](https://img.shields.io/badge/Safety-Guardrails-orange)
![FAISS](https://img.shields.io/badge/VectorDB-FAISS-5D6D7E)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker)
![Azure](https://img.shields.io/badge/Cloud-Azure-0078D4?logo=microsoftazure)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-E6522C?logo=prometheus)
![Grafana](https://img.shields.io/badge/Dashboard-Grafana-F46800?logo=grafana)
![Terraform](https://img.shields.io/badge/IaC-Terraform-7B42BC?logo=terraform)


## Executive Summary
This project demonstrates how enterprises can deploy safe, API-driven GenAI services by combining orchestration, guardrails, and governance. It aligns with Apple, Microsoft, and Google’s AI Architect requirements, providing a reusable template for secure AI adoption.

---

## Situation
AI adoption is accelerating across industries, but without orchestration and governance, firms face risks: unsafe prompts, bias, lack of audit trails.

## Complication
LLMs generate unfiltered, unpredictable outputs. Enterprises lack visibility and compliance-ready governance. Big Tech JDs now explicitly require solutions for this.

## Resolution — What I Built
- FastAPI orchestration API
- Guardrails for prompt moderation
- Audit logging + Prometheus/Grafana monitoring
- Dockerized for enterprise deployment

📊 **Architecture Overview (C4)**  
- Context diagram (enterprise context)  
- Container diagram (APIs, DBs, monitoring)  
- Component diagram (modules inside orchestration service)  


---

## 🛠 Tooling Exposure
- Development: VS Code, Cursor, Replit
- Infra: Docker, Azure Container Instances, Terraform
- AI/ML: LangChain, Guardrails, HuggingFace, FAISS
- Monitoring: Prometheus, Grafana
- Governance: ADRs, C4 diagrams

---

## 🚀 Getting Started
```bash
# clone repo
git clone <your-repo-url>
cd ai-orchestration-safety-layer

# setup environment
pip install -r requirements.txt

# run service
uvicorn app.main:app --reload
