import json
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent

TASKS = BASE / "tasks"
RESULTS = BASE / "results"

TASKS.mkdir(exist_ok=True)
RESULTS.mkdir(exist_ok=True)

counter = int(time.time())

task_text = input("Masukkan tugas: ")

if "riset" in task_text.lower():
    filename = f"research_{counter}.json"
else:
    filename = f"task_{counter}.json"

task_file = TASKS / filename

with open(task_file, "w") as f:
    json.dump({"task": task_text}, f)

print(f"Hermes mengirim: {filename}")

print("Menunggu hasil...")

result_file = RESULTS / filename

while not result_file.exists():
    time.sleep(1)

with open(result_file) as f:
    result = json.load(f)

print("\n=== HASIL ===")
print(json.dumps(result, indent=2))
