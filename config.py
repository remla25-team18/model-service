import os
MODEL_REPO_URL = "https://raw.githubusercontent.com/remla25-team18/operation/main"
MODEL_DIR = "model"
VECTORIZER_DIR = "vectorizer"

MODEL_SERVICE_HOST = os.getenv("MODEL_SERVICE_HOST", "localhost")
MODEL_SERVICE_PORT = int(os.getenv("MODEL_SERVICE_PORT", 5050))
MODEL_SERVICE_URL = f"http://{MODEL_SERVICE_HOST}:{MODEL_SERVICE_PORT}"