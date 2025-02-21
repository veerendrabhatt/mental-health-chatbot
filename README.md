# Mental Health Chatbot Project

## Overview
This project involves the development of a mental health support chatbot that uses advanced language models to provide users with empathetic responses and guidance. The chatbot is designed to be a safe, anonymous space for users to share their feelings, ask for advice, and receive self-help resources. It is built using **Flask** for web functionality and **LangChain** for natural language processing and interaction management.

## Features
- **Emotion Recognition**: Understands the emotional tone of user input and responds accordingly.
- **Mental Health Resources**: Provides suggestions and links to mental health resources, including helplines and informative articles.
- **Self-help Techniques**: Offers coping mechanisms, including breathing exercises and mindfulness tips.

## Technologies Used
- **Flask**: For building the web interface and handling API requests.
- **LangChain**: Used for processing and managing conversations with pre-trained language models.
  - `langchain-core` handles the core functionality of conversational agents.
  - `langchain-groq` (or any other supported language models) helps improve chatbot performance.
- **Python-dotenv**: For managing environment variables such as API keys and sensitive data.
- **Natural Language Processing (NLP)**: The chatbot understands and processes user input using language models.
- **Other Libraries**:
  - `requests` (for API calls if necessary)
  - `Flask-Cors` (to handle cross-origin resource sharing, if deploying the chatbot on a different domain)
  
## Installation

### Prerequisites
Make sure you have the following software installed:
- Python 3.6+
- pip (Python package manager)

### Steps to Set Up the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/veerendrabhatt/mental-health-chatbot.git
   cd mental-health-chatbot
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Your `requirements.txt` should include:
   ```
   Flask==2.2.2
   langchain-groq==0.1.0
   langchain-core==0.1.0
   python-dotenv==0.19.2
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory of the project.
   - Add your environment variables (e.g., API keys for language models or any other sensitive information):
     ```
     OPENAI_API_KEY=your_api_key_here
     LANGCHAIN_API_KEY=your_langchain_api_key_here
     ```

5. **Run the Flask application**:
   ```bash
   python app.py
   ```

6. **Access the chatbot**:
   - Open your browser and go to `http://localhost:5000` to start interacting with the chatbot.

## Usage

Once the chatbot is running, users can interact with it through a simple web interface. The chatbot will try to understand their input and provide thoughtful responses related to mental health.

### Example Interaction:

**User**: "I feel really anxious about work."

**Chatbot**: "It’s understandable to feel anxious about work sometimes. Have you tried practicing some grounding techniques? They can help bring you back to the present moment. Would you like to try one?"

**User**: "Yes, I'd like to try."

**Chatbot**: "Great! Let’s try a 5-4-3-2-1 grounding exercise. Start by identifying 5 things you can see around you..."

## Contributing

We welcome contributions to this project! If you would like to improve or expand the chatbot, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-name`)
6. Create a new pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the creators of [LangChain](https://www.langchain.com/) for providing an excellent framework to build conversational agents.
- Special thanks to the mental health professionals who contributed feedback and resources for the chatbot's responses.
