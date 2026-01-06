import librosa
import numpy as np

def load_audio(path):
    y, sr = librosa.load(path, sr=22050)
    return y, sr


def detect_cough_events(y, sr):
    energy = librosa.feature.rms(y=y)[0]
    threshold = np.mean(energy) + 1.5 * np.std(energy)

    frames = np.where(energy > threshold)[0]
    cough_events = librosa.util.frame(
        y, frame_length=int(0.5 * sr), hop_length=512
    )

    detected = [cough_events[:, i] for i in frames if i < cough_events.shape[1]]
    return detected


def extract_features(cough, sr):
    mfcc = np.mean(librosa.feature.mfcc(y=cough, sr=sr, n_mfcc=13), axis=1)
    zcr = np.mean(librosa.feature.zero_crossing_rate(cough))
    energy = np.mean(librosa.feature.rms(y=cough))
    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=cough, sr=sr))

    return np.hstack([mfcc, zcr, energy, spectral_centroid])