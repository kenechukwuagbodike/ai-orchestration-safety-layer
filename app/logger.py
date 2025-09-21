import json
import time
from pathlib import Path

# Logs will be saved here
LOG_FILE = Path("logs/audit.log")

# Ensure the logs directory exists
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

def write_audit_log(user: str, prompt: str, status: str, reason: str = ""):
    """
    Write a structured log entry to the audit log file.
    Each entry is a JSON line with timestamp, user, prompt, status, and reason.
    """
    log_entry = {
        "timestamp": time.time(),
        "user": user,
        "prompt": prompt,
        "status": status,
        "reason": reason
    }
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")