import subprocess

def kafka_consumer():
    topic_name = input("Enter the name of the Kafka topic to consume: ")
    try:
        subprocess.run(["C:\\Kafka\\bin\\windows\\kafka-console-consumer.bat", "--topic", topic_name, "--from-beginning", "--bootstrap-server", "localhost:9092"])
    except KeyboardInterrupt:
        print("Consumer stopped.")

# Uncomment the line below to test
kafka_consumer()
