# run_zookeeper.py

import subprocess
import time

def start_zookeeper():
    subprocess.run(["C:\\Kafka\\bin\\windows\\zookeeper-server-start.bat", "C:\\Kafka\\config\\zookeeper.properties"])
    print("Zookeeper started successfully.")

if __name__ == "__main__":
    start_zookeeper()
    time.sleep(500)  # Give Zookeeper some time to start

