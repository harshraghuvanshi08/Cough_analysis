import streamlit as st
from aud_process import load_audio, detect_cough_events, extract_features
from utils import encode_questionnaire
from classifier import classify_cough, aggregate_cough_features
from disease_classifier import predict_disease
from report_gen import generate_report, lung_health_index


st.title("AI Respiratory Screening System")

audio_file = st.file_uploader("Upload Cough WAV File", type=["wav"])

st.subheader("Health Questionnaire")
age = st.number_input("Age", 1, 100, 26)
gender = st.selectbox("Gender", ["male", "female"])
smoking = st.checkbox("Smoker")
wheezing = st.checkbox("Wheezing")
mucus = st.checkbox("Mucus")
night_cough = st.checkbox("Night Cough")
frequent_cough = st.checkbox("Frequent Cough")
difficulty_breathing = st.checkbox("Difficulty Breathing")
family_asthma = st.checkbox("Family History of Asthma")
smoke_exposure = st.checkbox("Smoke Exposure")

if st.button("Run Screening") and audio_file:
    y, sr = load_audio(audio_file)
    coughs = detect_cough_events(y, sr)

    cough_features, labels = [], []
    for c in coughs:
            f = extract_features(c, sr)
            label, _ = classify_cough(f)
            cough_features.append(f)
            labels.append(label)

    cough_stats = aggregate_cough_features(cough_features, labels)

    q = {
        "age": age,
        "gender": gender,
        "smoking": smoking,
        "wheezing": wheezing,
        "mucus": mucus,
        "night_cough": night_cough,
        "frequent_cough": frequent_cough,
        "difficulty_breathing": difficulty_breathing,
        "family_asthma": family_asthma,
        "smoke_exposure": smoke_exposure
    }

    features = [
        cough_stats["wet_percentage"],
        cough_stats["total_coughs"],
        cough_stats["mean_energy"],
        cough_stats["mean_spectral_centroid"],
        q["age"],
        q["smoking"],
        q["wheezing"]
    ]

    disease_probs = predict_disease(features)

    report = generate_report(q, cough_stats, disease_probs)


    st.subheader("Respiratory Screening Report")
    st.json(report)
