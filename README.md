# Personal AI Tutor Chatbot

## Overview
The Personal AI Tutor Chatbot is an interactive web-based AI-driven educational tool designed to assist students with their questions across various subjects. The system leverages Google's Generative AI via the LangChain library and incorporates memory management using ChromaDB to provide personalized responses based on past interactions with each user.

## Features
- **Interactive Chat Interface:** Users can interact with the chatbot through a simple web interface.
- **User-Specific Memory:** The chatbot remembers past interactions for each user, providing contextual responses based on user history.
- **Scalable and Flexible:** Built with Flask, the application can handle multiple users simultaneously.
- **Integration with Google Generative AI:** Utilizes LangChain's integration with Google Generative AI to generate high-quality, informative responses.

## Technologies Used
- **Flask:** A lightweight WSGI web application framework used for building the server-side of the chatbot.
- **HTML/CSS/JavaScript:** For building the frontend interface of the chatbot.
- **LangChain:** A library for building applications powered by language models.
- **ChromaDB:** Used as a vector store for memory management, allowing the bot to store and retrieve past user interactions.
- **Google Generative AI (Gemini):** Provides the language model for generating responses.
- **Mem0:** Mem0 enhances AI assistants and agents with an intelligent memory layer, enabling personalized AI interactions.

## Getting Started

### Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.8 or higher installed.
- Flask, Flask-CORS, and other required Python packages installed.
- A valid Google API key for the Generative AI (Gemini) service.
- A `secrete.txt` file in the root directory containing your Google API key.

## Installation

#### Clone the Repository:
```bash
git clone https://github.com/yourusername/AI_Tutor_withmemory.git
cd AI_Tutor_withmemory
```
## Setup ChromaDB
Ensure that ChromaDB is correctly configured and accessible. This project uses ChromaDB for memory management.

## Configure Google API Key
Create a `secrete.txt` file in the root directory and add your Google API key:

```text
YOUR_GOOGLE_API_KEY_HERE
```
## Run the Application
Start the Flask server:

```bash
python app.py
```
The application will be available at http://127.0.0.1:5000.
## File Structure
- `app.py`: The main Flask application that handles API requests and serves the frontend.
- `index.html`: The frontend interface for interacting with the chatbot.
- `personal_ai_tutor.py`: Contains the PersonalAITutor class, managing AI interactions and memory.
- `requirements.txt`: Lists all the dependencies required for the project.
- `secrete.txt`: Contains the Google API key (not included in the repository).

## How to Use
1. Open a web browser and navigate to `http://127.0.0.1:5000`.
2. Enter a User ID in the provided input field.
3. Type a message or question in the chat input and click "Send".
4. The bot will respond based on your input, and it will remember previous interactions associated with your User ID.
5. You can switch User IDs at any time to simulate different users or test multiple scenarios.

## Example
Here’s a quick example of how to interact with the chatbot:

- **User:** "What is the capital of France?"
- **Bot:** "The capital of France is Paris."

If the user later asks, "Remind me of the capital of France," the bot will remember the previous conversation and provide a consistent answer.

## Contributing
If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Open a pull request.

## License
## Custom License

### 1. License Grant
Arahanta pokhrel grants you a non-exclusive, non-transferable license to use, but not to modify or distribute, the software for personal or internal business purposes only.

### 2. Restrictions
- You may not use this software for commercial purposes without explicit permission from Arahanta Pokhrel.
- You may not distribute, sell, or sublicense the software to third parties.

### 3. Ownership
All rights, title, and interest in and to the software, including any intellectual property rights, remain with Arahanta Pokhrel.

### 4. No Warranty
The software is provided "as is," without warranty of any kind, either express or implied, including but not limited to the implied warranties of merchantability or fitness for a particular purpose.

### 5. Contact
For any questions regarding this license or to request a commercial license, please contact Arahanta Pokhrel.









