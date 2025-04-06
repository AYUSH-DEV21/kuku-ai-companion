def generate_story(genre, mood):
    sample = {
        "Motivation": f"As you begin your {mood.lower()} day, remember: every step forward is a victory.",
        "Fiction": f"In a distant land filled with {mood.lower()} whispers, a hero rises...",
        "History": f"During the {mood.lower()} days of the Renaissance, innovation flourished across Europe...",
    }
    return sample.get(genre, "Your story is being crafted...")
