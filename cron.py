from datetime import datetime
from pathlib import Path

p = Path("runs.txt")

now = datetime.utcnow().isoformat()
with p.open("a") as f:
    f.write(now + "\n")

print("Cron çalıştı:", now)
