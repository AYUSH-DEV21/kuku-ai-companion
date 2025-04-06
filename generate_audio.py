from gtts import gTTS
import os

# Create a folder if it doesn't exist
os.makedirs("assets", exist_ok=True)

audio_messages = {
    ("Motivation", "Chill"): "Take it slow today. Even a small step counts. You got this.",
    ("Motivation", "Productive"): "Time to shine! Stay focused, stay strong, and keep pushing.",
    ("Motivation", "Curious"): "Curiosity is your fuel. Let’s learn and grow today, one step at a time.",

    ("Fiction", "Chill"): "In a quiet world, a silent story begins to unfold under the moonlight.",
    ("Fiction", "Productive"): "She raced through the city streets, chasing her dream one breath at a time.",
    ("Fiction", "Curious"): "The hidden library whispered secrets waiting for someone brave enough to ask.",

    ("History", "Chill"): "During calm times, great thinkers shaped the world quietly behind the scenes.",
    ("History", "Productive"): "Driven by vision, ancient leaders carved their legacy in every stone and scroll.",
    ("History", "Curious"): "Curious minds once questioned the stars, the sea, and sparked revolutions."
}

for (genre, mood), message in audio_messages.items():
    filename = f"assets/{genre.lower()}_{mood.lower()}.mp3"
    tts = gTTS(text=message, lang='en')
    tts.save(filename)
    print(f"Saved: {filename}")
