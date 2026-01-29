from datetime import datetime
from pathlib import Path

p = Path("runs.txt")
aylar = [
    "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
    "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"
]
now = datetime.now()
now = f"{now.day} {aylar[now.month - 1]} {now.year} {now.hour:02d}:{now.minute:02d}"

with p.open("a") as f:
    f.write(now + "\n")

print("Cron çalıştı:", now)
