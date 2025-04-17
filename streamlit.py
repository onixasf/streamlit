import streamlit as st
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Judul
st.title("Audio Playback & Waveform Viewer")

# File audio lokal
audio_file = "lingkungan.mp3"

# Tampilkan pemutar audio
st.subheader("Audio Playback")
with open(audio_file, 'rb') as f:
    st.audio(f.read(), format="audio/mp3")

# Load audio untuk visualisasi
y, sr = librosa.load(audio_file, sr=None)
st.subheader("Waveform Visualization")

# Plot waveform
fig, ax = plt.subplots()
librosa.display.waveshow(y, sr=sr, ax=ax)
ax.set_title("Waveform of lingkungan.mp3")
st.pyplot(fig)