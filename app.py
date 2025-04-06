import streamlit as st
from generator import generate_story
import os

st.set_page_config(page_title="Kuku AI Companion", layout="centered")

st.title("🎧 Kuku AI Companion")
st.write("Your daily personalized audio journey!")

# Dropdowns for genre and mood
genre = st.selectbox("Select your preferred genre:", ["Motivation", "Fiction", "History"])
mood = st.selectbox("How are you feeling today?", ["Chill", "Productive", "Curious"])

# Generate story and locate audio
if st.button("Generate My Daily Story"):
    story = generate_story(genre, mood)
    st.subheader("📝 Today's Story")
    st.write(story)

    # Dynamically build the file path based on selected genre and mood
    audio_file = f"assets/{genre.lower()}_{mood.lower()}.mp3"

    # Check if audio file exists
    if os.path.exists(audio_file):
        st.audio(audio_file, format="audio/mp3")
    else:
        st.error("Audio file not found. Please check the assets folder.")

# Engagement Metrics (just for mock effect)
st.markdown("---")
st.metric(label="Sessions Completed", value="3")
st.metric(label="Likes Received", value="12")
