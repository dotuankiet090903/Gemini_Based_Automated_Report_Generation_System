from fastapi import FastAPI, Body
from report_generator import generate_daily_report
from LLM import summarize_report
import json
import os

app = FastAPI(title="Report Microservice")

# --- 1. Generate report on-demand ---
@app.get("/report/generate")
def generate_report():
    report = generate_daily_report()
    return report


# --- 2. Read existing JSON file ---
@app.get("/report/read")
def read_existing_report():
    file_path = "data/dataset.json"

    if not os.path.exists(file_path):
        return {"error": "Sample report not found"}

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


# --- 3. Ping (for LLM health check) ---
@app.get("/health")
def health_check():
    return {"status": "Report Service Running"}

from LLM import summarize_report

# --- 4. Report Summarize ---
@app.get("/report/summarize")
def summarize_existing_report(mode: str = "concise"):
    file_path = "data/dataset.json"

    if not os.path.exists(file_path):
        return {"error": "Sample report not found"}

    with open(file_path, "r", encoding="utf-8") as f:
        report = json.load(f)

    summary = summarize_report(report, mode)

    return {
        "source": "data/dataset.json",
        "mode": mode,
        "summary": summary
    }