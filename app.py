import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# -----------------------------
# 🔐 Spotify Secrets
# -----------------------------
CLIENT_ID = st.secrets["SPOTIPY_CLIENT_ID"]
CLIENT_SECRET = st.secrets["SPOTIPY_CLIENT_SECRET"]

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
))

# -----------------------------
# 🎨 UI Styling (Clean + Modern)
# -----------------------------
st.set_page_config(page_title="Mood Music 🎧", layout="wide")

st.markdown("""
<style>
.main {
    background-color: #0E1117;
    color: white;
}
.card {
    background: #1c1f26;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

st.title("🎧 Mood-Based Music Recommender")
st.caption("Hindi • Punjabi • Haryanvi Only")

# -----------------------------
# 🧠 FIXED Mood Detection
# -----------------------------
def detect_mood(text):
    text = text.lower()

    if any(word in text for word in ["energetic", "gym", "workout", "hype", "excited"]):
        return "energetic"
    elif any(word in text for word in ["sad", "depressed", "cry", "heartbreak"]):
        return "sad"
    elif any(word in text for word in ["calm", "relax", "peace", "sleep"]):
        return "calm"
    elif any(word in text for word in ["happy", "fun", "party", "love"]):
        return "happy"
    else:
        return "happy"

# -----------------------------
# 🎵 Regional Song Fetch
# -----------------------------
def get_songs(mood):
    mood_map = {
        "happy": "bollywood happy songs",
        "sad": "bollywood sad songs",
        "energetic": "punjabi workout songs",
        "calm": "lofi hindi chill"
    }

    query = mood_map[mood] + " hindi punjabi"

    try:
        results = sp.search(
            q=query,
            type='track',
            limit=10,
            market='IN'   # 🔥 IMPORTANT FIX
        )

        songs = []
        for item in results['tracks']['items']:
            songs.append({
                "name": item['name'],
                "artist": ", ".join([a['name'] for a in item['artists']]),
                "image": item['album']['images'][0]['url'] if item['album']['images'] else None,
                "url": item['external_urls']['spotify'],
                "preview": item['preview_url']
            })

        return songs

    except Exception as e:
        st.error("⚠️ Spotify API error. Check your credentials or try again.")
        return []

# -----------------------------
# 🎧 INPUT
# -----------------------------
user_input = st.text_input("💭 How are you feeling?")

if st.button("🎵 Recommend"):
    if not user_input.strip():
        st.warning("Enter your mood")
    else:
        mood = detect_mood(user_input)
        st.subheader(f"🧠 Mood Detected: {mood.upper()}")

        songs = get_songs(mood)

        cols = st.columns(2)

        for i, song in enumerate(songs):
            with cols[i % 2]:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.image(song["image"])
                st.markdown(f"**{song['name']}**")
                st.caption(song["artist"])
                st.markdown(f"[▶ Play on Spotify]({song['url']})")

                if song["preview"]:
                    st.audio(song["preview"])

                st.markdown('</div>', unsafe_allow_html=True)
