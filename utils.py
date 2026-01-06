def encode_questionnaire(q):
    return [
        q["age"],
        1 if q["gender"] == "male" else 0,
        int(q["smoking"]),
        int(q["wheezing"]),
        int(q["mucus"]),
        int(q["night_cough"]),
        int(q["frequent_cough"]),
        int(q["difficulty_breathing"]),
        int(q["family_asthma"]),
        int(q["smoke_exposure"])
    ]