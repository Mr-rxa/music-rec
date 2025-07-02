# 🎵 Music Recommender System

A beautiful and interactive music recommendation app built with Streamlit that suggests songs based on your current mood.

## ✨ Features

- **Mood-Based Recommendations**: Get personalized song suggestions based on 6 different moods
- **Beautiful UI**: Modern, responsive design with gradient backgrounds and smooth animations
- **Interactive Elements**: Click to play buttons and YouTube links for each song
- **Session History**: Track your recommendation history and statistics
- **Customizable**: Choose how many recommendations you want (1-10)
- **Real-time Stats**: See your usage statistics and current time

## 🎭 Available Moods

- 😊 **Happy** - Upbeat and cheerful songs
- 😢 **Sad** - Melancholic tunes for emotional moments
- ⚡ **Energetic** - High-energy tracks to get pumped
- 😌 **Relaxed** - Calming melodies for peace
- 💕 **Romantic** - Love songs for the heart
- 💪 **Motivated** - Inspiring tracks for goals

## 🚀 Installation & Usage

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone or download the project**
   ```bash
   git clone https://github.com/Mr-rxa/music-rec.git
   cd music-rec
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, copy the URL from the terminal

## 🎯 How to Use

1. **Select Your Mood**: Choose from the dropdown menu with emoji indicators
2. **Customize Settings**: Use the sidebar to adjust the number of recommendations
3. **Get Recommendations**: Click the "Get Recommendations" button
4. **Explore Songs**: 
   - Click "Play" buttons to simulate playing songs
   - Click YouTube links to watch music videos
   - View your recommendation history

## 🎨 UI Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Gradient Backgrounds**: Beautiful color schemes for different moods
- **Card-based Layout**: Clean, organized presentation of songs
- **Interactive Elements**: Hover effects and smooth transitions
- **Statistics Dashboard**: Track your usage and session data

## 📊 Features Overview

- **Session Management**: Tracks your recommendation history
- **Statistics**: View total recommendations and session count
- **History Clearing**: Reset your session data anytime
- **YouTube Integration**: Direct links to music videos
- **Mood Descriptions**: Helpful descriptions for each mood category

## 🛠️ Technical Details

- **Framework**: Streamlit
- **Language**: Python 3.7+
- **Styling**: Custom CSS with gradients and animations
- **State Management**: Streamlit session state
- **Data Structure**: Dictionary-based song database

## 🎵 Song Database

The app includes a curated collection of songs across various genres:
- Bollywood hits
- Punjabi tracks
- Haryanvi songs
- International hits
- Motivational tracks

Each song includes:
- Song name and artist
- Direct YouTube link
- Mood categorization

## 🔧 Customization

You can easily customize the app by:
- Adding new songs to the `mood_music` dictionary
- Modifying the CSS styles in the `st.markdown` section
- Adding new mood categories
- Changing the color schemes

## 📱 Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge

## 🤝 Contributing

Feel free to contribute by:
- Adding more songs to the database
- Improving the UI/UX
- Adding new features
- Fixing bugs

## 📄 License

This project is open source and available under the MIT License.

## 🎵 Enjoy Your Music!

Discover your perfect soundtrack for every mood with our Music Recommender System! 
