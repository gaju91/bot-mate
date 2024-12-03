from flask import Flask, request, jsonify
from app.chatbot import chatbot_response

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    """
    Chat endpoint to handle user queries.
    """
    user_query = request.json.get("message")
    if not user_query:
        return jsonify({"error": "No message provided"}), 400
    
    try:
        response = chatbot_response(user_query)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
