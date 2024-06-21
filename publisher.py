from rabbitmq import RabbitMQ


def publish_test_message():
    rabbitmq = RabbitMQ()
    try:
        rabbitmq.publish(queue_name="test_queue", message="Test message")
        print("Test message published successfully.")
    except Exception as e:
        print(f"Failed to publish test message: {e}")
    finally:
        rabbitmq.close()


if __name__ == "__main__":
    publish_test_message()
