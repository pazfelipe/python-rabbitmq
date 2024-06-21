# RabbitMQ Example with Python

## Purpose

This project demonstrates how to set up and use RabbitMQ with Python. It includes examples of how to connect to RabbitMQ, publish messages to a queue, and consume messages from a queue. The project also uses Docker to manage RabbitMQ in a containerized environment.

## Requirements

To run this project, you will need the following:

- Python 3.8+
- Docker
- Docker Compose
- RabbitMQ

## Setup

### Activate the virtual environment

1. **Create the virtual environment:**

    ```sh
    python -m venv .venv
    ```

2. **Activate the virtual environment:**
    - On Windows:

        ```sh
        .venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source .venv/bin/activate
        ```

### Install the dependencies

1. **Install the required Python packages:**

    ```sh
    pip install -r requirements.txt
    ```

### Start the Docker container

1. **Build and run the RabbitMQ container using Docker Compose:**

    ```sh
    docker-compose up -d
    ```

### Start the RabbitMQ server

1. **Run the main script to start the RabbitMQ server:**

    ```sh
    python main.py
    ```

### Publish a message

1. **Run the publisher script to publish a test message:**

    ```sh
    python publisher.py
    ```

### Note

The RabbitMQ management console can be accessed at [http://localhost:15672](http://localhost:15672).

## Project Structure

```sh
.
├── docker-compose.yaml   # Docker Compose file for RabbitMQ
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── README.md             # Project documentation
├── rabbitmq.py           # RabbitMQ connection and operations
└── main.py               # Main script to start the RabbitMQ server
└── publisher.py          # Publisher script to publish a message
```

### Important

- Ensure that the `.env` file contains the correct RabbitMQ credentials and settings.
- Make sure to start the Docker container before running any Python scripts.
