# FastAPI Chat Application

This FastAPI chat application enables real-time messaging through WebSockets and supports asynchronous message streaming. Built with FastAPI, it showcases how to integrate asynchronous operations and WebSocket communication in a modern Python web framework.

The application communicates with the OpenAI API, using its responses to stream content to clients progressively. This method contrasts traditional HTTP requests by providing immediate, incremental updates through WebSocket connections.

## Features

- Real-time WebSocket communication facilitated by FastAPI.
- Asynchronous handling of messages and streaming.
- Environment configuration managed through `.env` files for API keys and other settings.
- Integrate Prometheus to track metrics on user mood during interactions with the AI, and to observe the frequency of requests to each endpoint.

## Project Structure

- `main.py`: Entry point of the FastAPI application, defining routes and app configuration.
- `controllers/`: Directory containing controllers definitions for HTTP and WebSocket endpoints.
- `services/`: Contains service logic, including communication with the OpenAI API.
- `dto/`: Defines Data Transfer Objects (DTOs) for structured data exchange.
- `monitoring/`: Implements custom metrics and monitoring functionality.
- `config/`: Configuration folder.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository to your local machine.

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Environment Configuration

Create a `.env` file in the root directory of the project and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### Running the Application

To run the FastAPI application:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Access the application at `http://127.0.0.1:8000`.

## Usage

- Establish a connection to the WebSocket endpoint at `/websocket-chat` for real-time messaging.
- Use the HTTP endpoint `/stream-chat/?message=<your_message>` to receive streamed responses asynchronously.

## Contributing

Contributions to the project are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.
