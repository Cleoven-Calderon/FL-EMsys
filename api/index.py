from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Vercel Flask!"})

# This is IMPORTANT for Vercel
handler = app
