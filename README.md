
# Flask Chat Application

This Flask chat application facilitates real-time messaging via WebSockets and offers support for asynchronous message streaming. Constructed using Flask and Flask-SocketIO, it demonstrates the incorporation of asynchronous features within a Flask framework. 

The application interacts with the OpenAI API, serving as an example of utilizing the response to stream content to clients incrementally, instead of waiting for the entire response. This approach is employed to illustrate the differences between HTTP and WebSocket communication methods.
## Features

- Real-time WebSocket communication with Flask-SocketIO.
- Asynchronous message streaming and handling.
- Environment configuration using dotenv for API keys and other settings.
- CORS setup for cross-origin resource sharing.

## Project Structure

- `app.py`: Initializes the Flask application and SocketIO.
- `routes.py`: Defines HTTP routes for the application.
- `chat_service.py`: Functions for chat with OpenAi 

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:

2. Install the required packages:

```bash
pip install -r requirements.txt
```

### Environment Configuration

Create a `.env` file in the project root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### Running the Application

1. Start the Flask application:

```bash
flask run
```

2. Access the application at `http://127.0.0.1:8000`.

## Usage

- Connect to the WebSocket endpoint at `/websocket-chat` to start sending and receiving messages in real-time.
- Access `/stream-chat/?message=<your_message>` to stream responses for a message asynchronously.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.
