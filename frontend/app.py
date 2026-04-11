import streamlit as st
import requests

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Mood AI 🎧", layout="wide")

BACKEND_URL = "http://127.0.0.1:8000"   # change after deployment

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

.title {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    color: #00FFD1;
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

# ---------------- HEADER ----------------
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

            try:
                response = requests.get(
                    f"{BACKEND_URL}/recommend",
                    params={
                        "mood_text": mood_input,
                        "language": language,
                        "limit": limit
                    }
                ).json()

                if "error" in response:
                    st.error(response["error"])
                else:
                    st.subheader(f"🧠 Mood Detected: {response['mood'].upper()}")

                    cols = st.columns(3)

                    for i, song in enumerate(response["songs"]):
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

            except Exception as e:
                st.error("Backend not running or connection failed")
