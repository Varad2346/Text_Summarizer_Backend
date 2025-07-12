# 🧠 Text Summarizer Backend

A Flask-based backend API for summarizing long pieces of text using Hugging Face's `distilbart-cnn-12-6` transformer model. This backend can be connected to a frontend (like React) or used independently via API calls.

---

## 🚀 Features

- 📄 Accepts raw text via POST request
- 🤖 Uses Hugging Face transformer model for abstractive summarization
- 🌐 Provides summarized response in JSON
- 🔐 Supports CORS for frontend communication
- 🔧 Easy to deploy on platforms like Render

---

## 📦 Tech Stack

- Python
- Flask
- Transformers (`HuggingFace`)
- Flask-CORS
