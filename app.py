import streamlit as st
from textblob import TextBlob
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import nltk

nltk.download('punkt')

# -----------------------------
# 🔐 Secure Credentials
# -----------------------------
try:
    CLIENT_ID = st.secrets["SPOTIPY_CLIENT_ID"]
    CLIENT_SECRET = st.secrets["SPOTIPY_CLIENT_SECRET"]
except:
    st.error("Spotify credentials not found. Add them to secrets.")
    st.stop()

# Spotify connection
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
))

# -----------------------------
# 🧠 Mood Detection
# -----------------------------
def detect_mood(text):
    text = text.lower()
    polarity = TextBlob(text).sentiment.polarity

    if "angry" in text:
        return "energetic"
    elif "love" in text or "romantic" in text:
        return "happy"
    elif polarity > 0.3:
        return "happy"
    elif polarity < -0.3:
        return "sad"
    elif "tired" in text or "relax" in text:
        return "calm"
    else:
        return "calm"

# -----------------------------
# 🎵 Get Songs
# -----------------------------
def get_songs(mood):
    mood_map = {
        "happy": "happy upbeat",
        "sad": "sad songs",
        "energetic": "workout music",
        "calm": "chill relaxing"
    }

    results = sp.search(q=mood_map[mood], type='track', limit=8)

    songs = []
    for item in results['tracks']['items']:
        songs.append({
            "name": item['name'],
            "artist": item['artists'][0]['name'],
            "url": item['external_urls']['spotify'],
            "image": item['album']['images'][0]['url'],
            "preview": item['preview_url']
        })

    return songs

# -----------------------------
# 🎧 UI
# -----------------------------
st.title("🎧 Mood Music Recommender")

user_input = st.text_input("How are you feeling?")

if st.button("Recommend 🎵"):
    if user_input.strip() == "":
        st.warning("Please enter your mood")
    else:
        mood = detect_mood(user_input)
        st.subheader(f"🧠 Detected Mood: {mood}")

        songs = get_songs(mood)

        for song in songs:
            st.image(song["image"], width=200)
            st.write(f"**{song['name']}** - {song['artist']}")
            st.write(song["url"])

            if song["preview"]:
                st.audio(song["preview"])

            st.write("---")
