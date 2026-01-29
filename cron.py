from datetime import datetime
from pathlib import Path

p = Path("runs.txt")
now = datetime.now(ZoneInfo("Europe/Istanbul")).isoformat()
with p.open("a") as f:
    f.write(now + "\n")

print("Cron çalıştı:", now)
