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

### Installation

#### Clone the Repository:
```bash
git clone https://github.com/yourusername/AI_Tutor_withmemory.git
cd AI_Tutor_withmemory
