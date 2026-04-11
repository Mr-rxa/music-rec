from fastapi import FastAPI
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
analyzer = SentimentIntensityAnalyzer()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET")
))

# ---------------- MOOD DETECTION ----------------
def detect_mood(text):
    score = analyzer.polarity_scores(text)["compound"]

    if score >= 0.5:
        return "happy"
    elif score <= -0.5:
        return "sad"
    elif -0.5 < score < 0:
        return "calm"
    else:
        return "energetic"

# ---------------- LANGUAGE MAP ----------------
lang_map = {
    "Hindi": "bollywood hindi",
    "Punjabi": "punjabi",
    "Haryanvi": "haryanvi"
}

# ---------------- MOOD MAP ----------------
mood_map = {
    "happy": "happy songs",
    "sad": "sad songs",
    "energetic": "workout songs",
    "calm": "lofi chill"
}

# ---------------- API ----------------
@app.get("/recommend")
def recommend(mood_text: str, language: str, limit: int = 10):

    mood = detect_mood(mood_text)

    query = f"{mood_map[mood]} {lang_map.get(language, 'hindi')}"

    try:
        results = sp.search(q=query, type='track', limit=limit, market='IN')

        songs = []
        for item in results['tracks']['items']:
            songs.append({
                "name": item['name'],
                "artist": ", ".join([a['name'] for a in item['artists']]),
                "image": item['album']['images'][0]['url'] if item['album']['images'] else None,
                "url": item['external_urls']['spotify'],
                "preview": item['preview_url']
            })

        return {"mood": mood, "songs": songs}

    except Exception as e:
        return {"error": str(e)}
