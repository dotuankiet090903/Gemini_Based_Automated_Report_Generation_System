# Report Microservice with LLM-based Summarization

## Overview

This project implements a **FastAPI-based microservice** that simulates a system report pipeline and uses a **Large Language Model (LLM)** to automatically summarize generated reports.

The system follows these steps:
1. Generate a daily report dataset in JSON format.
2. Store the report locally.
3. Read the generated dataset via an API endpoint.
4. Use an LLM to generate a natural language summary of the report.

This project demonstrates how LLMs can be integrated into backend services to convert **structured system data (JSON)** into **human-readable summaries**.

---

## Project Structure

```text
Gemini_Based_Automated_Report_Generation_System/
│── .venv/
│── data/
│   └── dataset.json
│── main.py
│── report_generator.py
│── LLM.py
│── requirements.txt
│── README.md
```

## Requirements

- Python 3.9+
- Virtual environment (`.venv`)
- Dependencies listed in `requirements.txt`

---

## Setup Instructions

### 1. Create and activate virtual environment

**Windows**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

**Running the Application**

```bash
uvicorn main:app --reload
```

API base URL: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

## API Workflow
**Step 1: Generate report dataset**

```bash
GET /report/generate
```
Important: This endpoint must be called first to generate data (dataset.json).

**Step 2: Read generated report**

```bash
GET /report/read
```

**Step 3: Summarize report using LLM**

```bash
GET /report/summarize?mode=concise
```

There are 2 modes: concise (default) and detailed.

**Step 4: Health check**

```bash
GET /health
```

## Technologies Used

- FastAPI
- Uvicorn
- Python
- Large Language Models (LLM)
- Google Gemini API
