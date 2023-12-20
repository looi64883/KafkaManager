# create_topics.py
import subprocess

def create_kafka_topics():
    topic_name = input("Enter the name of the Kafka topic to create: ")
    try:
        subprocess.run(["C:\\Kafka\\bin\\windows\\kafka-topics.bat", "--create", "--topic", topic_name, "--bootstrap-server", "localhost:9092"], check=True)
        print(f"Kafka topic '{topic_name}' created successfully.")

    except subprocess.CalledProcessError as e:
        print("Error creating Kafka topics:", e.stderr)

# Uncomment the line below to test
if __name__ == "__main__":
    create_kafka_topics()