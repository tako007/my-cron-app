from datetime import datetime

now = datetime.utcnow().isoformat()
print(f"Cron çalıştı: {now}")
