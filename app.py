from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from personal_ai_tutor import PersonalAITutor  # Assuming you have your AI tutor in this file

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Initialize the AI Tutor
ai_tutor = PersonalAITutor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_id = data.get("user_id", "default")
    question = data.get("question", "")
    
    # Ask the AI Tutor
    response = ai_tutor.ask(question, user_id=user_id)
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
