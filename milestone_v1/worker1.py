import json
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

TASKS = BASE / "tasks"
RESULTS = BASE / "results"

print("Worker1 started")

while True:
    for task_file in TASKS.glob("task*.json"):
        try:
            with open(task_file) as f:
                task = json.load(f)

            result = {
                "task": task.get("task"),
                "status": "done",
                "worker": "worker1"
            }

            result_file = RESULTS / task_file.name

            with open(result_file, "w") as f:
                json.dump(result, f, indent=2)

            task_file.unlink()

            print(f"Processed {task_file.name}")

        except Exception as e:
            print("ERROR:", e)

    time.sleep(5)
