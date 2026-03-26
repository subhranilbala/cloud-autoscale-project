import psutil
import time
import os

THRESHOLD = 75

def check_usage():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    return cpu, mem

while True:
    cpu, mem = check_usage()
    print(f"CPU: {cpu}%, Memory: {mem}%")

    if cpu > THRESHOLD or mem > THRESHOLD:
        print("Threshold exceeded! Triggering cloud scaling...")
        os.system("bash scale_to_cloud.sh")
        break

    time.sleep(5)
