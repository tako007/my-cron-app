from datetime import datetime, timezone, timedelta
from pathlib import Path

p = Path("runs.txt")

aylar = [
    "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
    "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"
]

# UTC+3 tanımı
tr_tz = timezone(timedelta(hours=3))

now = datetime.now(tr_tz)

formatted = f"{now.day} {aylar[now.month - 1]} {now.year} {now.hour:02d}:{now.minute:02d}"

with p.open("a") as f:
    f.write(formatted + "\n")

print("Cron çalıştı:", formatted)
