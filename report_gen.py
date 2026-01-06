def lung_health_index(wet_pct, cough_count):
    score = 100
    score -= wet_pct * 0.3
    score -= cough_count * 2
    return max(0, round(score, 1))


def risk_label(prob):
    if prob > 0.7:
        return "High"
    elif prob > 0.4:
        return "Medium"
    else:
        return "Low"


def generate_report(data, cough_report, disease_prob):
    return {
        "Patient Info": data,
        "Cough Summary": cough_report,
        "Lung Health Index": lung_health_index(
            cough_report["wet_percentage"],
            cough_report["total_coughs"]
        ),
        "Asthma Risk": {
            "Probability": disease_prob["Asthma"],
            "Risk Level": risk_label(disease_prob["Asthma"])
        },
        "COPD Risk": {
            "Probability": disease_prob["COPD"],
            "Risk Level": risk_label(disease_prob["COPD"])
        },
        "Overall Assessment": (
            "Abnormal" if disease_prob["Asthma"] > 0.5 or disease_prob["COPD"] > 0.5
            else "Normal"
        )
    }