import time

def task():
    print("Task executed at", time.ctime())

for i in range(3):
    task()
    time.sleep(5)

import subprocess
# Initialize git repository
subprocess.run(["git", "init"])
# Create a sample file
with open("test.txt", "w") as f:
    f.write("DevOps Lab Git Automation")
# Add file
subprocess.run(["git", "add", "."])
# Commit
subprocess.run(["git", "commit", "-m", "Initial commit using Python"])
print("Git repository initialized and committed.")
