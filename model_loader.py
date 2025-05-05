import os
import requests
from joblib import load
from config import MODEL_REPO_URL, MODEL_DIR, VECTORIZER_DIR

def download_file(url, save_path):
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to download {url} (status {response.status_code})")
    with open(save_path, "wb") as f:
        f.write(response.content)

def get_latest_timestamp():
    url = f"{MODEL_REPO_URL}/manifest.json"
    response = requests.get(url)
    print(response)
    if response.status_code != 200:
        raise RuntimeError(f"Could not fetch latest model timestamp. URL tried: {url} — Status: {response.status_code}")
    return response.json()

def load_latest_model():
    model_timestamp = get_latest_timestamp()[MODEL_DIR]
    vectorizer_timestamp = get_latest_timestamp()[VECTORIZER_DIR]
    model_filename = f"model-{model_timestamp}.pkl"
    vectorizer_filename = f"bow-{vectorizer_timestamp}.pkl"

    os.makedirs(MODEL_DIR, exist_ok=True)
    os.makedirs(VECTORIZER_DIR, exist_ok=True)

    model_path = os.path.join(MODEL_DIR, model_filename)
    vectorizer_path = os.path.join(VECTORIZER_DIR, vectorizer_filename)

    if not os.path.exists(model_path):
        print("Downloading model...")
        download_file(f"{MODEL_REPO_URL}/model/{model_filename}", model_path)

    if not os.path.exists(vectorizer_path):
        print("Downloading vectorizer...")
        download_file(f"{MODEL_REPO_URL}/vectorizer/{vectorizer_filename}", vectorizer_path)

    print(f"Loaded model: {model_path}")
    print(f"Loaded vectorizer: {vectorizer_path}")

    # model = load(model_path)
    # vectorizer = load(vectorizer_path)
    # return model, vectorizer
    return (True, True)

if __name__ == "__main__":
    load_latest_model()