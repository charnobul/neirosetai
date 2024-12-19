from flask import Flask, request, jsonify, render_template
from chatbot import ChatBot

app = Flask(__name__)
bot = ChatBot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = bot.generate_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
