import json
import time
from pathlib import Path

TASKS = Path("tasks")
RESULTS = Path("results")

print("Worker2 started")

while True:
    for task_file in TASKS.glob("research_*.json"):
        try:
            with open(task_file) as f:
                task = json.load(f)

            result = {
                "task": task.get("task"),
                "status": "researched",
                "worker": "worker2",
                "notes": "research completed"
            }

            result_file = RESULTS / task_file.name

            with open(result_file, "w") as f:
                json.dump(result, f, indent=2)

            task_file.unlink()

            print(f"Processed {task_file.name}")

        except Exception as e:
            print("ERROR:", e)

    time.sleep(5)
