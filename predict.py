from lib_ml.preprocess import preprocess_text

def predict_sentiment(text, model, vectorizer):
    # Preprocess input using lib-ml
    processed_text = preprocess_text([text])
    X = vectorizer.transform(processed_text).toarray()

    # Predict
    return model.predict(X)[0]