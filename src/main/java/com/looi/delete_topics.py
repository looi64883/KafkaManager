import subprocess

def delete_kafka_topic():
    topic_name = input("Enter the name of the Kafka topic to delete: ")
    try:
        subprocess.run(["C:\\Kafka\\bin\\windows\\kafka-topics.bat", "--bootstrap-server", "localhost:9092", "--delete", "--topic", topic_name], check=True)
        print(f"Kafka topic '{topic_name}' deleted successfully.")

    except subprocess.CalledProcessError as e:
        print("Error deleting Kafka topic:", e.stderr)

# Uncomment the line below to test
if __name__ == "__main__":
    delete_kafka_topic()
