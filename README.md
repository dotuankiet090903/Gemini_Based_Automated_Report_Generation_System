# 📊 Automated Report Generation & Summarization API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Google Gemini](https://img.shields.io/badge/LLM-Google%20Gemini-orange.svg)

## 🌟 Overview
This project is a **FastAPI-based microservice** designed to simulate an automated system report pipeline. It goes beyond simple data generation by leveraging a **Large Language Model (Google Gemini)** to digest complex, structured system logs (JSON) and output accessible, human-readable summaries.

### Why this project?
In enterprise environments, systems generate vast arrays of JSON logs. This microservice demonstrates how to intercept structured data and automatically translate it into intuitive language for managers and stakeholders.

### 🔄 The Pipeline
1. **Generate**: Creates a fake daily report dataset in JSON format.
2. **Store**: Persists the dataset locally.
3. **Read**: Exposes the dataset via an API endpoint.
4. **Summarize**: Prompts an LLM to generate a natural language summary.

---

## 📂 Project Structure
```text
Gemini_Based_Automated_Report_Generation_System/
│── .venv/                 # Virtual Environment
│── data/
│   └── dataset.json       # Generated structured data
│── main.py                # FastAPI Application Entry
│── report_generator.py    # Mock Data Generator
│── LLM.py                 # LLM Integration Logic
│── requirements.txt       # Dependencies
│── README.md              # You are here!
```

---

## 🚀 Setup Instructions

### 1. Environment Preparation
Ensure you have **Python 3.9+** installed. Activate your virtual environment and install dependencies:

**Windows PowerShell:**
```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Launch the Application
Start the Uvicorn ASGI server:
```bash
uvicorn main:app --reload
```
- **API Base URL**: `http://127.0.0.1:8000`
- **Interactive API Docs (Swagger UI)**: `http://127.0.0.1:8000/docs`

---

## 🌐 API Workflow

To use the service, follow this logical flow:

### Step 1: Generate Data
*Must be called first to initialize `dataset.json`.*
```http
GET /report/generate
```

### Step 2: Read Data (Optional)
*View the raw, structured JSON report.*
```http
GET /report/read
```

### Step 3: Summarize ✨
*Have the LLM analyze and summarize the report in plain English.*
```http
GET /report/summarize?mode=concise
```
> **Parameters:**
> - `mode` (query param): Choose either `concise` (default) or `detailed`.

### Step 4: Health Check
*Verify the API is running correctly.*
```http
GET /health
```

---
**Tech Stack:** FastAPI, Uvicorn, Python, Google Gemini API
