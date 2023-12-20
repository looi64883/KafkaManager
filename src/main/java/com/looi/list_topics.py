# list_topics.py
import subprocess

def display_kafka_topics():
    try:
        result = subprocess.run(["C:\\Kafka\\bin\\windows\\kafka-topics.bat", "--bootstrap-server", "localhost:9092", "--list"], capture_output=True, text=True, check=True)
        print("Kafka Topics:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error displaying Kafka topics:", e.stderr)

# Uncomment the line below to test
if __name__ == "__main__":
    display_kafka_topics()

