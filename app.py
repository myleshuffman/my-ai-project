from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Hello from my-ai-project"})

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify({"received": data})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
