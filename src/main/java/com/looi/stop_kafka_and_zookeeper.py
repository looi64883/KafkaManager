import subprocess

def stop_kafka_and_zookeeper():
    subprocess.run(["C:\\Kafka\\bin\\windows\\kafka-server-stop.bat"])
    subprocess.run(["C:\\Kafka\\bin\\windows\\zookeeper-server-stop.bat"])
    print("Kafka and Zookeeper stopped successfully.")

# Uncomment the line below to test
if __name__ == "__main__":
    stop_kafka_and_zookeeper()
