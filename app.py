import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Mood AI 🎧", layout="wide")

CLIENT_ID = st.secrets["SPOTIPY_CLIENT_ID"]
CLIENT_SECRET = st.secrets["SPOTIPY_CLIENT_SECRET"]

# ---------------- SPOTIFY ----------------
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
))

# ---------------- MOOD MODEL ----------------
analyzer = SentimentIntensityAnalyzer()

def detect_mood(text):
    score = analyzer.polarity_scores(text)["compound"]

    if score >= 0.5:
        return "happy"
    elif score <= -0.5:
        return "sad"
    elif score < 0:
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

# ---------------- CACHING ----------------
@st.cache_data(ttl=3600)
def get_songs(mood, language, limit):
    query = f"{mood_map[mood]} {lang_map[language]}"

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

    return songs

# ---------------- UI ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #141E30, #243B55);
    color: white;
}

.title {
    text-align:center;
    font-size:3rem;
    font-weight:bold;
    color:#00FFD1;
}

.glass {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 15px;
    margin-bottom: 20px;
    transition: 0.3s;
}

.glass:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 20px rgba(0,255,200,0.4);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🎧 Mood AI Recommender</div>', unsafe_allow_html=True)

# ---------------- INPUT ----------------
col1, col2, col3 = st.columns(3)

with col1:
    mood_input = st.text_input("💭 Your Mood")

with col2:
    language = st.selectbox("🌍 Language", ["Hindi", "Punjabi", "Haryanvi"])

with col3:
    limit = st.slider("🎵 Number of Songs", 5, 20, 10)

# ---------------- BUTTON ----------------
if st.button("🔥 Recommend Songs"):

    if not mood_input.strip():
        st.warning("Enter your mood")

    else:
        with st.spinner("🎧 Finding perfect songs..."):

            mood = detect_mood(mood_input)

            st.subheader(f"🧠 Mood Detected: {mood.upper()}")

            songs = get_songs(mood, language, limit)

            cols = st.columns(3)

            for i, song in enumerate(songs):
                with cols[i % 3]:
                    st.markdown('<div class="glass">', unsafe_allow_html=True)

                    if song["image"]:
                        st.image(song["image"])

                    st.markdown(f"### {song['name']}")
                    st.caption(song["artist"])

                    st.markdown(f"[▶ Play on Spotify]({song['url']})")

                    if song["preview"]:
                        st.audio(song["preview"])

                    st.markdown('</div>', unsafe_allow_html=True)
