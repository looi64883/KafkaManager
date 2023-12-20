import subprocess
import time

def start_kafka():
    subprocess.run(["C:\\Kafka\\bin\\windows\\kafka-server-start.bat", "C:\\Kafka\\config\\server.properties"])
    print("Kafka started successfully.")

if __name__ == "__main__":
    start_kafka()
    time.sleep(500)  # Give Kafka some time to start