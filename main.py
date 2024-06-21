from rabbitmq import RabbitMQ
import sys


def main():
    rabbitmq = RabbitMQ()
    try:
        rabbitmq.connect()
        print("Connection to RabbitMQ established successfully.")
    except Exception as e:
        print(f"Failed to establish connection to RabbitMQ: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
