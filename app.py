import os
from flask import Flask, request, jsonify
from predict import predict_sentiment
from model_loader import load_latest_model
from config import MODEL_SERVICE_PORT


def get_current_version():
    try:
        version_file = open("VERSION", "r")
        version = version_file.read().strip()
        version_file.close()
        # remove "-pre", decrease Patch version by 1
        version = version.split("-")[0]
        version_parts = version.split(".")
        if len(version_parts) == 3:
            major, minor, patch = version_parts
            patch = str(int(patch) - 1)
            version = f"{major}.{minor}.{patch}"
        else:
            raise ValueError("Version format is incorrect")
        return version
    except FileNotFoundError:
        return None


app = Flask(__name__)

# Load latest model and vectorizer on startup
model, vectorizer, model_version = load_latest_model()
version = get_current_version()


# ---
# summary: Health check for the model service
# description: Returns 200 if the model service is running.
# operationId: getTestStatus
# responses:
#   200:
#     description: Service is up and running
@app.route("/test", methods=["GET"])
def test():
    return jsonify({"status": "Model-service is running"}), 200


# ---
# summary: Predict sentiment from input text
# description: Returns 0 or 1 indicating the sentiment class (e.g., negative or positive).
# operationId: postPredictSentiment
# parameters:
#   - name: text
#     in: body
#     description: The input text to classify
#     required: true
#     schema:
#       type: object
#       required:
#         - text
#       properties:
#         text:
#           type: string
# responses:
#   200:
#     description: Successful prediction
#     schema:
#       type: object
#       properties:
#         prediction:
#           type: integer
#   400:
#     description: Missing text in input
#     schema:
#       type: object
#       properties:
#         error:
#           type: string
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' in request body"}), 400

    prediction = predict_sentiment(data["text"], model, vectorizer)
    return jsonify({"prediction": int(prediction)}), 200


# ---
# summary: Get the current model version
# description: Returns the semantic version of the currently loaded model.
# operationId: getModelVersion
# responses:
#   200:
#     description: Version string
#     schema:
#       type: object
#       properties:
#         version:
#           type: string
@app.route("/version", methods=["GET"])
def get_version():
    return jsonify({"version": version}), 200


if __name__ == "__main__":
    port = MODEL_SERVICE_PORT
    app.run(host="0.0.0.0", port=port)
