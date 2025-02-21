from flask import Flask, render_template, request, jsonify
import os

# Set the API key directly in code (for development only)
os.environ["GROQ_API_KEY"] = "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"

# Retrieve the GROQ API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("Please set the GROQ_API_KEY environment variable.")

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Change this line
app = Flask(__name__)  # <-- This is the fix

# Initialize the ChatGroq LLM
llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Create a prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a helpful and friendly mental health ai assistant assistant. 
            If someone comes to you seeking for kind words and validation you must make  them feel warm, welcomed and comfortable. be a little funny to brighten their mood up. dont repeat the same words in replies
            Keep responses concise and under 30 words.
            """
        ),
        ("human", "{input}")
    ]
)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    try:
        # Get the user's input message
        msg = request.form["msg"]
        
        # Process the message using the chain
        chain = prompt | llm
        response = chain.invoke({"input": msg})
        
        return jsonify({"response": response.content})
    except Exception as e:
        print(f"Error during chat processing: {e}")
        return jsonify({"error": "An error occurred. Please try again later."})

if __name__ == '__main__':  # <-- Fix this part too
    app.run(debug=True)
