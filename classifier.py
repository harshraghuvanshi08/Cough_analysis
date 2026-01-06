import joblib
import numpy as np

wet_dry_classifier = joblib.load("models/wet_dry_model.pkl")

def classify_cough(features):
    prob = wet_dry_classifier.predict_proba([features])[0]
    label = "Wet" if prob[1] > 0.5 else "Dry"
    return label, prob[1]

def aggregate_cough_features(cough_features, cough_labels):
    total = len(cough_labels)
    wet = cough_labels.count("Wet")
    dry = cough_labels.count("Dry")

    wet_pct = (wet / total) * 100 if total else 0

    return {
        "total_coughs": total,
        "wet_coughs": wet,
        "dry_coughs": dry,
        "wet_percentage": wet_pct,
        "mean_energy": np.mean([f[-2] for f in cough_features]),
        "mean_spectral_centroid": np.mean([f[-1] for f in cough_features])
    }