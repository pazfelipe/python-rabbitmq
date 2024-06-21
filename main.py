from rabbitmq import RabbitMQ
import sys


def callback(ch, method, properties, body):
    print(f"Received message: {body}")


def main():
    rabbitmq = RabbitMQ()
    try:
        print("Connection to RabbitMQ established successfully.")
        rabbitmq.consume(queue_name="test_queue", callback=callback)
    except Exception as e:
        print(f"Failed to establish connection to RabbitMQ: {e}")
        sys.exit(1)
    finally:
        rabbitmq.close()


if __name__ == "__main__":
    main()
