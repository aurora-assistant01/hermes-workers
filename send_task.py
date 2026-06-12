import json
import time
from pathlib import Path

task_id = f"task_{int(time.time())}"

task = {
"task_id": task_id,
"task": input("Task: ")
}

Path(f"tasks/{task_id}.json").write_text(
json.dumps(task, indent=2)
)

print("Created", task_id)
