import random
from datetime import datetime

def generate_daily_report():
    statuses = ["success", "failed"]
    failure_reasons = ["Insufficient balance", "Payment gateway timeout", "Bank declined"]

    report = {
        "report_date": datetime.now().strftime("%Y-%m-%d"),
        "total_transactions": 0,
        "successful_transactions": 0,
        "failed_transactions": 0,
        "total_amount_vnd": 0,
        "transactions": []
    }

    # Create random 20–50 transactions
    for i in range(random.randint(20, 50)):
        status = random.choice(statuses)
        amount = random.randint(1000000, 30000000)

        txn = {
            "transaction_id": f"TXN-{i+1:03}",
            "student_id": f"STU-{1000+i}",
            "student_name": f"Student {i+1}",
            "amount_vnd": amount,
            "status": status,
            "timestamp": datetime.now().isoformat()
        }

        if status == "failed":
            txn["failure_reason"] = random.choice(failure_reasons)
            report["failed_transactions"] += 1
        else:
            report["successful_transactions"] += 1
            report["total_amount_vnd"] += amount

        report["transactions"].append(txn)

    report["total_transactions"] = len(report["transactions"])
    return report
