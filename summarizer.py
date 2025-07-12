import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)  # Enable CORS

# Set your HF API key here or get from environment variable
HF_API_KEY = os.getenv("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.route("/api/summarize", methods=["POST"])
def summarize_text():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    output = query({"inputs": text})

    if isinstance(output, dict) and output.get("error"):
        return jsonify({"error": output["error"]}), 500

    summary_text = output[0]['summary_text'] if output else ""
    return jsonify({"summary": summary_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
