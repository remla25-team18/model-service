from flask import Flask, request, jsonify
from predict import predict_sentiment
from model_loader import load_latest_model

app = Flask(__name__)

# Load latest model and vectorizer on startup
model, vectorizer, version = load_latest_model()

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"status": "Model-service is running"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' in request body"}), 400

    prediction = predict_sentiment(data["text"], model, vectorizer)
    return jsonify({"prediction": int(prediction), "version": str(version)}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
