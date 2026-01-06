import joblib

disease_classifier = joblib.load("models/disease_model.pkl")

def predict_disease(features):
    probs = disease_classifier.predict_proba([features])[0]

    return {
        "Healthy": probs[0],
        "Asthma": probs[1],
        "COPD": probs[2]
    }