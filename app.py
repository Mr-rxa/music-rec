import streamlit as st
import random
from datetime import datetime
import base64

# Page configuration
st.set_page_config(
    page_title="🎵 Music Recommender",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    
    .mood-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .song-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    .mood-selector {
        background: white;
        border-radius: 15px;
        padding: 1rem;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        flex: 1;
        margin: 0 0.5rem;
    }
</style>
""", unsafe_allow_html=True)
def get_music_recommendation(mood):
    mood_music = {
        "happy": [
            "Tareefan - Veere Di Wedding--https://www.youtube.com/watch?v=3SWc5G8Gx7E&pp=ygUZdGFyZWVmYW4gdmVlcmUgZGkgd2VkZGluZw%3D%3D",
            "Morni Banke - Badhaai Ho--https://www.youtube.com/watch?v=1EadhOBcfI0&pp=ygULbW9ybmkgYmFua2U%3D",
            "Laung Laachi - Laung Laachi--https://www.youtube.com/watch?v=YpkJO_GrCo0&pp=ygULbGF1bmcgbGFjaGk%3D",
            "Sauda Khara Khara - Good Newwz--https://www.youtube.com/watch?v=LYEqeUr-158&pp=ygURc2F1ZGEga2hhcmEga2hhcmE%3D",
            "Dil Chori - Sonu Ke Titu Ki Sweety--https://www.youtube.com/watch?v=xWi8nDUjHGA&pp=ygUKZGlsICBjaG9yaQ%3D%3D",
            "Lungi Dance - Chennai Express--https://www.youtube.com/watch?v=69CEiHfS_mc&pp=ygULbHVuZ2kgZGFuY2U%3D",
            "Bolo Ta Ra Ra - Daler Mehndi--https://www.youtube.com/watch?v=lhVceZE1lf4&pp=ygUNYm9sbyB0YSByYSByYQ%3D%3D",
            "Gaddi Jaandi Ae Chalaang - Karan Aujla--https://www.youtube.com/watch?v=VBwADjEvXPk&pp=ygULZ2FkZGkgamFuZGk%3D",
            "Tamma Tamma Again - Badrinath Ki Dulhania--https://www.youtube.com/watch?v=EEX_XM6SxmY&pp=ygURdGFtbWEgdGFtbWEgYWdhaW4%3D",
            "Coka - Sukh-E Muzical Doctorz--https://www.youtube.com/watch?v=7lWeQs8Firo&pp=ygUEY29rYQ%3D%3D",
            "Badtameez Dil - Yeh Jawaani Hai Deewani--https://www.youtube.com/watch?v=II2EO3Nw4m0&pp=ygUNYmFkdGFtZWV6IGRpbA%3D%3D",
            "Kala Chashma - Baar Baar Dekho--https://www.youtube.com/watch?v=4WRJHbL4dAk&pp=ygUTa2FsYSBjaGFzbWEgZGogc29uZw%3D%3D",
            "Chogada - Loveyatri--https://www.youtube.com/watch?v=asYxxtiWUyw&pp=ygUHY2hvZ2FkYQ%3D%3D",
            "Aankh Marey - Simmba--https://www.youtube.com/watch?v=_KhQT-LGb-4&pp=ygUUQWFua2ggTWFyZXkgLSBTaW1tYmE%3D",
            "High Rated Gabru - Guru Randhawa--https://www.youtube.com/watch?v=hjWf8A0YNSE&pp=ygUgSGlnaCBSYXRlZCBHYWJydSAtIEd1cnUgUmFuZGhhd2E%3D",
            "Genda Phool - Badshah--https://www.youtube.com/watch?v=SD4Z8dlZPd8&pp=ygUVR2VuZGEgUGhvb2wgLSBCYWRzaGFo0gcJCYQJAYcqIYzv",
            "Gani - Akhil--https://www.youtube.com/watch?v=FNxD8nRCCms&pp=ygUMS29rYSAtIEFraGls",
            "Naah - Hardy Sandhu--https://www.youtube.com/watch?v=8qs2dZO6wcc&pp=ygUEbmFhaA%3D%3D",
            "Jind Mahi - Diljit Dosanjh--https://www.youtube.com/watch?v=gfYXKP5V-Tc&pp=ygUYSmluZCBNYWhpIC0gR2lwcHkgR3Jld2Fs",
            "Phulkari - Ranjit Bawa--https://www.youtube.com/watch?v=KyK3Pn4JaSI&pp=ygUTTG92ZXIgLSBSYW5qaXQgQmF3YQ%3D%3D",
            "Kya baat aa - Karan Aujla--https://www.youtube.com/watch?v=x-KbnJ9fvJc&pp=ygUmUHlhYXIgSG90YSBLYXlpIEJhYXIgSGFpIC0gS2FyYW4gQXVqbGE%3D",
            "Sadi Gali - Tanu Weds Manu--https://www.youtube.com/watch?v=w_HaezV0DqI&pp=ygUaU2FkaSBHYWxpIC0gVGFudSBXZWRzIE1hbnU%3D",
            "Chikni Chameli - Agneepath--https://www.youtube.com/watch?v=QcQpqWhTBCE&pp=ygUaQ2hpa25pIENoYW1lbGkgLSBBZ25lZXBhdGg%3D",
            "Lagdi Lahore Di - Guru Randhawa--https://www.youtube.com/watch?v=dZ0fwJojhrs&pp=ygUfTGFnZGkgTGFob3JlIERpIC0gR3VydSBSYW5kaGF3YQ%3D%3D",
            "Aaja Mexico Challiye - Karan Aujhla--https://www.youtube.com/watch?v=PRjFAk7hRSc&pp=ygUVIEFhamEgTWV4aWNvIENoYWxsaXll",
            "Khadke Glassy - Honey Singh--https://www.youtube.com/watch?v=YcDw4h3SUfI&pp=ygUsS2hhZGtlIEdsYXNzeSAtIEthcmFuIEF1amxhIGFuZCBHYXJyeSBTYW5kaHXSBwkJhAkBhyohjO8%3D",
            "Jatt Da Muqabala - Sidhu Moosewala--https://www.youtube.com/watch?v=LSDxjp6sWYQ&pp=ygUMamF0dCBkYSBtdWth0gcJCYQJAYcqIYzv",
            "Chail Haryana ka - Haryanvi--https://www.youtube.com/watch?v=WsmMT2EHRB4&pp=ygUSaGFwcHkgaGFyeWFudmkgb25n0gcJCYQJAYcqIYzv",
            "Last peg - Haryanvi--https://www.youtube.com/watch?v=4-Dqft187HQ&pp=ygULdGVyaSBiaGFiaGk%3D",
            "Baarish Ki Jaaye - B Praak--https://www.youtube.com/watch?v=TYaNfLLOLNY&pp=ygUYYmFhcmlzaCBraSBqYWF5ZSBiIHByYWFr",
            "Kahani Suno 2.0 - Kaifi Khalil--https://www.youtube.com/watch?v=_XBVWlI8TsQ&pp=ygUNa2FoYW5pIHN1bm8gMg%3D%3D",
            "Baarish - Vishal Mishra--https://www.youtube.com/watch?v=FgckcPiDcjE&pp=ygUUYmFyaXNoIHZpc2hhbCBtaXNocmE%3D",
            "Dil Diyan Gallan - Tiger Zinda Hai--https://www.youtube.com/watch?v=SAcpESN_Fk4&pp=ygUOZGlsIGRpeWEgZ2FsbGE%3D",
            "Tum Hi Ho Bandhu - Cocktail--https://www.youtube.com/watch?v=o1RducJbUdc&pp=ygUPdHVtaGkgaG8gYmFuZGh1",
            "Bole Chudiyan - Kabhi Khushi Kabhie Gham--https://www.youtube.com/watch?v=IBvg3WeqP1U&pp=ygUSYm9sZSBjaHVkaXlhbiBra2tn",
            "Chandigarh Mein - Good Newwz--https://www.youtube.com/watch?v=yt4-qlU__iM&pp=ygUNY2hhbmRpZ2FyaCBtZQ%3D%3D",
            "Softly - Karan Aujla--https://www.youtube.com/watch?v=cWMxCE2HTag&pp=ygUWZ2FkaSBqYW5kaSBrYXJhbiBhdWpsYdIHCQmECQGHKiGM7w%3D%3D",
            "Chhor Denge - Parampara Tandon--https://www.youtube.com/watch?v=hGf8rOwFzvo&pp=ygUKY2hvciBkZW5nZQ%3D%3D",
            "Kachha Badam - Bhuban Badyakar--https://www.youtube.com/watch?v=WJYyeOkFytQ&pp=ygUMa2FjY2hhIGJhZGFt",
            "2 Khatole - Masoom Sharma--https://www.youtube.com/watch?v=obgMGM6I2rE&pp=ygUFMiBraGE%3D",
            "Blender - Masoom Sharma--https://www.youtube.com/watch?v=gGnGSKKsATM&pp=ygUMYmxlbmRlciBzb25n",
            "Parole - Masoom Sharma--https://www.youtube.com/watch?v=HAAoQvk-8mM&pp=ygUGcGFyb2xl",
            "Nazra ke teer - Vikram Sarkar--https://www.youtube.com/watch?v=cehyr946p64&pp=ygUNbmF6cmEga2UgdGVlcg%3D%3D"
        ],
        "sad": [
        "Dildaar Tera - Sandeep Chandel, Rohit Sardhana--https://www.youtube.com/watch?v=cSUhBp3jNJQ",
        "Nashe Pate - Mohit Sharma--https://www.youtube.com/watch?v=oAzyZGa9ygE",
        "Dil Tut Gya - Diler Kharkiya--https://www.youtube.com/watch?v=5jNexY8xrug",
        "Aashiqi Ka Rog - Diler Kharkiya--https://www.youtube.com/watch?v=QgZupxYr-RA",
        "Kamaal Hai - Amit Dhull--https://www.youtube.com/watch?v=przUl8E1WBY",
        "Haal Dil Ka - Anupam Nagar--https://www.youtube.com/watch?v=mSp5KbMP-ck",
        "Sharafat - Ruba Khan--https://www.youtube.com/watch?v=jKVBdUMq_yM",
        "Daraar - UK Haryanvi--https://www.youtube.com/watch?v=E76HbJshn_k",
        "Vidaai - Simran Bumrah--https://www.youtube.com/watch?v=kUB-KX7T4eQ",
        "Dhokhe Ne Salam - Ajesh Kumar--https://www.youtube.com/watch?v=y13xKGDgy2Y",
        "Moon Bound - Prem Dhillon--https://www.youtube.com/watch?v=4MPhysi03L8",
        "Raah - Navaan Sandhu--https://www.youtube.com/watch?v=Zgt8ogWWu1Q",
        "Just a Dream - Prem Dhillon--https://www.youtube.com/watch?v=oUJbvr8jcyk",
        "Regret - Sidhu Moosewala--https://www.youtube.com/watch?v=xgMGfOt7XhU",
        "No Soul There - Prem Dhillon--https://www.youtube.com/watch?v=DQepFnrPNtg",
        "Jaan - Gurnam Bhullar--https://www.youtube.com/watch?v=jdFKLWxNVpw",
        "Kalli Jind - Amrit Maan--https://www.youtube.com/watch?v=XyCOJa5dcBE",
        "Yaari - Karan Aujla--https://www.youtube.com/watch?v=O7OXkERmtZc",
        "Tere Te - Gurnam Bhullar--https://www.youtube.com/watch?v=ppYekYPxZFo",
        "Dark Love - Sidhu Moosewala--https://www.youtube.com/watch?v=MtHugZNPC4Y",
        "Tujhe Kitna Chahne Lage - Arijit Singh--https://www.youtube.com/watch?v=2IGDsD-dLF8",
        "Channa Mereya - Arijit Singh--https://www.youtube.com/watch?v=bzSTpdcs-EI",
        "Tum Hi Ho - Arijit Singh--https://www.youtube.com/watch?v=Umqb9KENgmk",
        "Kabira - Pritam, Tochi Raina, Rekha Bhardwaj--https://www.youtube.com/watch?v=jHNNMj5bNQw",
        "Tera Ban Jaunga - Akhil Sachdeva, Tulsi Kumar--https://www.youtube.com/watch?v=Qdz5n1Xe5Qo",
        "Likh dega ke jaani - Gold e Gill--https://www.youtube.com/watch?v=nM-OKWu5OXk&pp=ygURc2FkIGhhcnlhbnZpIHNvbmc%3D",
        "Syahi - Sinta Bhai--https://www.youtube.com/watch?v=J0rEeO3HFv8&pp=ygURc2FkIGhhcnlhbnZpIHNvbmc%3D",
        "Badmash bolu su - KD--https://www.youtube.com/watch?v=Mk132xeCnMQ&pp=ygURc2FkIGhhcnlhbnZpIHNvbmc%3D",
        "Mulakat - Vijay Verma--https://www.youtube.com/watch?v=oBPReTvycEc&pp=ygURc2FkIGhhcnlhbnZpIHNvbmc%3D",
        "Baba Ji - Sapna Chaudhary--https://www.youtube.com/watch?v=tnlnqTRV5ZQ&pp=ygUHYmFiYSBqaQ%3D%3D"
        ],
        "energetic": [
        "Goli - Diler Kharkiya--https://www.youtube.com/watch?v=GMmkbU5b92Q",
        "Bhangra Paale - Gippy Grewal--https://www.youtube.com/watch?v=WYa2qi0s9Ek",
        "Khadke Glassy - Yo Yo Honey Singh--https://www.youtube.com/watch?v=AmrRPNwrGQU",
        "Chandigarh - Kaka--https://www.youtube.com/watch?v=2DIU1SjTJB4",
        "Nalayak - Raju Punjabi--https://www.youtube.com/watch?v=ZdDt3419Q0w",
        "Rutba - Satinder Sartaaj--https://www.youtube.com/watch?v=ZdDt3419Q0w",
        "Winning Speech - Karan Aujla--https://www.youtube.com/watch?v=vsWxs1tuwDk",
        "Jee Nai Lagda - Karan Aujla--https://www.youtube.com/watch?v=BXNxrT59MzQ ",
        "Jxggi's anthem - Jxggi--https://www.youtube.com/watch?v=RNKRt9cx1os",
        "Baarish - Kaka-- https://www.youtube.com/watch?v=7i2VpgOhoiI",
        "Lungi Dance - Yo Yo Honey Singh--https://www.youtube.com/watch?v=69CEiHfS_mc",
        "Morni Banke - Guru Randhawa, Neha Kakkar--https://www.youtube.com/watch?v=1EadhOBcfI0",
        "Sauda khara khara - Sukhbir--https://www.youtube.com/watch?v=1EadhOBcfI0",
        "High Rated Gabru - Guru Randhawa--https://www.youtube.com/watch?v=hjWf8A0YNSE",
        "Taki Taki - DJ Snake, Selena Gomez--https://www.youtube.com/watch?v=ixkoVwKQaJg",
        "Laung Laachi - Mannat Noor--https://www.youtube.com/watch?v=YpkJO_GrCo0",
        "Dope Shope - Yo Yo Honey Singh--https://www.youtube.com/watch?v=dHsV56I1GwE",
        "Brown Munde - AP Dhillon, Gurinder Gill, Shinda Kahlon--https://www.youtube.com/watch?v=VNs_cCtdbPc",
        "Bolo Ta Ra Ra - Sukhbir--https://www.youtube.com/watch?v=lhVceZE1lf4",
        "God Damn - Karan Aujla--https://www.youtube.com/watch?v=au5uNkCKzaY",
        "Kar Gayi Chull - Badshah, Neha Kakkar--https://www.youtube.com/watch?v=NTHz9ephYTw",
        "Dil Chori - Yo Yo Honey Singh--https://www.youtube.com/watch?v=xWi8nDUjHGA",
        "Aankh Marey - Mika Singh--https://www.youtube.com/watch?v=_KhQT-LGb-4",
        "Badtameez Dil - Pritam, Vishal Dadlani--https://www.youtube.com/watch?v=II2EO3Nw4m0",
        "Ghungroo - Arijit Singh, Shilpa Rao--https://www.youtube.com/watch?v=qFkNATtc3mc",
        "Yaar Bathere- Yo Yo Honey Singh--https://www.youtube.com/watch?v=GNSXB6k0NW8",
        "Kala Chashma - Badshah, Neha Kakkar--https://www.youtube.com/watch?v=k4yXQkG2s1E",
        "Tamma Tamma Again - Badshah, Bappi Lahiri--https://www.youtube.com/watch?v=EEX_XM6SxmY",
        "Chhote Chhote Peg - Neha Kakkar, Yo Yo Honey Singh--https://www.youtube.com/watch?v=xvYBg6MWPbM",
        "Balam Pichkari - Vishal Dadlani, Shalmali Kholgade--https://www.youtube.com/watch?v=0WtRNGubWGA",
        "4G Ka Jamana - Sapna Choudhary--https://www.youtube.com/watch?v=XjGEJDig1uo&pp=ygUYaGFyeWFudmkgZW5lcmdldGljIHNvbmdz",
        "College aali Chori - Ashoka Deshwal--https://www.youtube.com/watch?v=sxH0msI9kEM&pp=ygUYaGFyeWFudmkgZW5lcmdldGljIHNvbmdz",
        "Solid Body - Ajay Hooda--https://www.youtube.com/watch?v=ou-litQ9hWQ&pp=ygUYaGFyeWFudmkgZW5lcmdldGljIHNvbmdz"
        ],
        "relaxed": [
            "Tum Hi Ho - Aashiqui 2--https://www.youtube.com/watch?v=Umqb9KENgmk",
            "Tera Ban Jaunga - Kabir Singh--https://www.youtube.com/watch?v=Qdz5n1Xe5Qo",
            "Kabira - Yeh Jawaani Hai Deewani--https://www.youtube.com/watch?v=jHNNMj5bNQw",
            "Dil Diyan Gallan - Tiger Zinda Hai--https://www.youtube.com/watch?v=SAcpESN_Fk4",
            "Pee Loon - Once Upon a Time in Mumbaai--https://www.youtube.com/watch?v=WCTro3qabjE",
            "Raabta - Agent Vinod--https://www.youtube.com/watch?v=zlt38OOqwDc",
            "Tujhse Naraz Nahi Zindagi - Masoom--https://www.youtube.com/watch?v=LZ_YUOr-tYw",
            "Khuda Jaane - Bachna Ae Haseeno--https://www.youtube.com/watch?v=cmMiyZaSELo",
            "Tera Hone Laga Hoon - Ajab Prem Ki Ghazab Kahani--https://www.youtube.com/watch?v=rLR37BR88T0",
            "Jeene Laga Hoon - Ramaiya Vastavaiya--https://www.youtube.com/watch?v=qpIdoaaPa6U",
            "Tum Se Hi - Jab We Met--https://www.youtube.com/watch?v=Cb6wuzOurPc",
            "Agar Tum Saath Ho - Tamasha--https://www.youtube.com/watch?v=sK7riqg2mr4",
            "Hasi Ban Gaye - Hamari Adhuri Kahani--https://www.youtube.com/watch?v=FOkVXadnO88",
            "Tera Ban Jaunga - Kabir Singh--https://www.youtube.com/watch?v=Qdz5n1Xe5Qo",
            "Kahin Toh Hogi Woh - Jaane Tu... Ya Jaane Na--https://www.youtube.com/watch?v=hCsY8T0uBGA",
            "Channa Mereya - Ae Dil Hai Mushkil--https://www.youtube.com/watch?v=bzSTpdcs-EI",
            "Mann Ki Manzil - Haryanvi--https://www.youtube.com/watch?v=dPy5UUgTy38",
            "Tere Bina - Guru Randhawa--https://www.youtube.com/watch?v=m05HDNnxLFk",
            "Dil Chura Liya - Haryanvi--https://www.youtube.com/watch?v=7pHQsft4New",
            "Kuch Is Tarah - Atif Aslam--https://www.youtube.com/watch?v=7pHQsft4New",
            "Tujhe Kitna Chahne Lage - Kabir Singh--https://www.youtube.com/watch?v=AgX2II9si7w",
            "Tum Mile - Tum Mile--https://www.youtube.com/watch?v=odVptmgIcD0",
            "Tera Hone Laga Hoon - Ajab Prem Ki Ghazab Kahani--https://www.youtube.com/watch?v=rLR37BR88T0",
            "Tera Ban Jaunga - Kabir Singh--https://www.youtube.com/watch?v=Qdz5n1Xe5Qo",
            "Kahin Toh Hogi Woh - Jaane Tu... Ya Jaane Na--https://www.youtube.com/watch?v=hCsY8T0uBGA",
            "Tum Se Hi - Jab We Met--https://www.youtube.com/watch?v=Cb6wuzOurPc",
            "Hasi Ban Gaye - Hamari Adhuri Kahani--https://www.youtube.com/watch?v=FOkVXadnO88",
            "Dil Diyan Gallan - Tiger Zinda Hai--https://www.youtube.com/watch?v=SAcpESN_Fk4",
            "Pee Loon - Once Upon a Time in Mumbaai--https://www.youtube.com/watch?v=WCTro3qabjE",
            "Raabta - Agent Vinod--https://www.youtube.com/watch?v=zlt38OOqwDc",
            "Kabira - Yeh Jawaani Hai Deewani--https://www.youtube.com/watch?v=jHNNMj5bNQw",
            "Tujhse Naraz Nahi Zindagi - Masoom--https://www.youtube.com/watch?v=LZ_YUOr-tYw",
            "Khuda Jaane - Bachna Ae Haseeno--https://www.youtube.com/watch?v=cmMiyZaSELo",
            "Tere Bina - Guru Randhawa--https://www.youtube.com/watch?v=9JDSGhhiOwI",
            "Dil Chura Liya - Haryanvi--https://www.youtube.com/watch?v=7pHQsft4New",
            "Kuch Is Tarah - Atif Aslam--https://www.youtube.com/watch?v=jjk-nmsXYhw",
            "Tujhe Kitna Chahne Lage - Kabir Singh--https://www.youtube.com/watch?v=2IGDsD-dLF8",
            "Tum Mile - Tum Mile--https://www.youtube.com/watch?v=UcqI3uBKgTg"
        ],
        "romantic": [
           "Tere Bina - Arijit Singh--https://www.youtube.com/watch?v=m05HDNnxLFk",
           "Kahani Suno - Kaifi khalil--https://www.youtube.com/watch?v=_XBVWlI8TsQ",
           "Lilo Chaman - Diler Kharkiya--https://www.youtube.com/watch?v=d7_Puc95qrc",
           "Yaad Teri - Raju Punjabi--https://www.youtube.com/watch?v=ZQdA-7UrQRM",
           "Aacha Lage Se - Raju Punjabi--https://www.youtube.com/watch?v=veVOxTkKSMU",
           "Jine Laga Hu - Girish Kumar--https://www.youtube.com/watch?v=qpIdoaaPa6U",
           "Dil Ibaadat Kar Raha Hai - Pritam--https://www.youtube.com/watch?v=U2QNhsAgIIE",
           "Dil Ki Baat - Renuka Pawar--https://www.youtube.com/watch?v=HjD2icD6Ihc",
           "Ik Kahani - Kaka--https://www.youtube.com/watch?v=4y6vAzD4h1U",
           "Karke Haar Singar - Vikash Kumar--https://www.youtube.com/watch?v=2jMN2MCqOsI",
           "Tum Hi Ho - Arijit Singh--https://www.youtube.com/watch?v=Umqb9KENgmk",
           "Tujhe Kitna Chahne Lage - Arijit Singh--https://www.youtube.com/watch?v=AgX2II9si7w",
           "Raabta - Arijit Singh--https://www.youtube.com/watch?v=vEe-UgJvUHE",
           "Kabira - Pritam, Tochi Raina, Rekha Bhardwaj--https://www.youtube.com/watch?v=jHNNMj5bNQw",
           "Tum Se Hi - Mohit Chauhan--https://www.youtube.com/watch?v=Cb6wuzOurPc",
           "Dil Diyan Gallan - Atif Aslam--https://www.youtube.com/watch?v=SAcpESN_Fk4",
           "Tera Hone Laga Hoon - Atif Aslam, Alisha Chinai--https://www.youtube.com/watch?v=rLR37BR88T0",
           "Khuda Jaane - Vishal-Shekhar, KK, Shreya Ghoshal--https://www.youtube.com/watch?v=cmMiyZaSELo",
           "Agar Tum Saath Ho - Arijit Singh, Alka Yagnik--https://www.youtube.com/watch?v=sK7riqg2mr4",
           "Pehla Nasha - Udit Narayan, Sadhana Sargam--https://www.youtube.com/watch?v=Ki41AKu0iHc",
           "Tera Ban Jaunga - Akhil Sachdeva, Tulsi Kumar--https://www.youtube.com/watch?v=Qdz5n1Xe5Qo",
           "Qismat - Amrinder Gill--https://www.youtube.com/watch?v=9xVp8m0fJSg",
           "Sohneya - Gurnam Bhullar--https://www.youtube.com/watch?v=57WhKDZAbqQ",
           "Jaan - Gurnam Bhullar--https://www.youtube.com/watch?v=jdFKLWxNVpw",
           "Ik Vaari - Arijit Singh--https://www.youtube.com/watch?v=zXLgYBSdv74",
           "Taare - Gurnam Bhullar--https://www.youtube.com/watch?v=ppYekYPxZFo",
            "kamlee -Sarrb--https://www.youtube.com/watch?v=9hMC7NA0yMw",
           "Pehli Nazar Mein - Atif Aslam--https://www.youtube.com/watch?v=BadBAMnPX0I",
           "Tum Har Lamha - Arijit Singh--https://www.youtube.com/watch?v=SdGL0qxgZGM",
           "Ik Supna- Ambar Vashisht--https://www.youtube.com/watch?v=sOoQH5z7BT8"
        ],
        "Motivated":[
            "Chak De India - Vidya Malvade--https://www.youtube.com/watch?v=bnqLzCsffwY&pp=ygUNY2hhayBkZSBpbmRpYQ%3D%3D",
            "Zinda - Farhan Akhtar--https://www.youtube.com/watch?v=Ax0G_P2dSBw&pp=ygUFWmluZGE%3D",
            "Kar Har Maidaan Fateh - Rajkumar Hirani--https://www.youtube.com/watch?v=9iIX4PBplAY&pp=ygUUa2FyIGhhciBtYWlkYW4gZmF0ZWg%3D",
            "Chak Lein De - Kailash Kher--https://www.youtube.com/watch?v=kd-6aw99DpA&pp=ygUMY2hhayBsZWluIGRl",
            "Salaam - Bintu Pabra--https://www.youtube.com/watch?v=Te3jgvurEy8&pp=ygUGc2FsYWFt",
            "hale Chalo - Srinivas--https://www.youtube.com/watch?v=LQmHKl3oNu0&pp=ygULY2hhbGUgY2hhbG8%3D",
            "Azaadiyan - Anu Malik--https://www.youtube.com/watch?v=jdMlP9MCXiE&pp=ygUJYXphYWRpeWFu0gcJCYQJAYcqIYzv",
            "Ziddi Dil - Mary Kom--https://www.youtube.com/watch?v=hu9Ac_HPC7s&pp=ygUJemlkZGkgZGls",
            "Dhakkad - Raftaar--https://www.youtube.com/watch?v=0zFoHrvbRu4&pp=ygUHZGhha2thZA%3D%3D",
            "Apna Time Aayega - Zoya Akhtar--https://www.youtube.com/watch?v=jFGKJBPFdUA&pp=ygUQYXBuYSB0aW1lIGFheWVnYQ%3D%3D",
            "Naadaan Parinde - A.R.Rahman--https://www.youtube.com/watch?v=6MgsHSAcI9k&pp=ygUPbmFhZGFhbiBwYXJpbmRl",
            "Jai Ho - A.R.Rahman--https://www.youtube.com/watch?v=xwwAVRyNmgQ&list=RDxwwAVRyNmgQ&start_radio=1",
            "Rang De Basanti - daler Mehndi--https://www.youtube.com/watch?v=c769V25pX08&pp=ygUPcmFuZyBkZSBiYXNhbnRp",
            "Chal Utth Bandeya - Kajal Aggarwal--https://www.youtube.com/watch?v=Hs0HTJnqfuw&pp=ygURY2hhbCB1dGhoIGJhbmRleWE%3D",
            "Mera Intekam Dekhegi - Krishna Beuraa--https://www.youtube.com/watch?v=BiVyN2ftrrs&pp=ygUUbWVyYSBpbnRla2FtIGRla2hlZ2k%3D",
            "Manzoor - Dev Arijit--https://www.youtube.com/watch?v=7owkGgkr0oE&pp=ygUUTWFuem9vciBkaWxlciBhcmlqaXQ%3D",
            "No Limit - Baadshah--https://www.youtube.com/watch?v=hD14MHAFvt8&pp=ygUIbm8gbGltaXTSBwkJhAkBhyohjO8%3D",
            "Bhirad Ladgi - Masoom Sharma--https://www.youtube.com/watch?v=nHbdEle8wZg&pp=ygULYmlyYWQgbGFkZ2k%3D",
            "Basti Ka Hasti - Mc Stan--https://www.youtube.com/watch?v=GbXtCRCT0Ig&pp=ygUSbWFpIGJhc3RpIGthIGhhc3Rp",
            "Rula Ke Gya Ishq Tera - Stebin Ben--https://www.youtube.com/watch?v=BfSRJKaYUuE&pp=ygUbcnVsYSBrZSBnYXlhIGlzaHEgdGVyYSBzb25n0gcJCYQJAYcqIYzv",
            "Success - Khushi pandher--https://www.youtube.com/watch?v=aryAYD8rcTg&pp=ygUUc3VjY2VzcyBwdW5qYWJpIHNvbmc%3D",
            "Struggler - Yash Vashisht--https://www.youtube.com/watch?v=7cDQq_0J7Co&pp=ygUJc3RydWdnbGVy",
            "sapne - Mohit Sharma--https://www.youtube.com/watch?v=1pR0llldJ6Y&pp=ygUTc2FwbmUgaGFyeWFudmkgc29uZw%3D%3D",
            "Situation - Akshay Shokeen--https://www.youtube.com/watch?v=ibVntEdKVBY&pp=ygUOc2l0dWF0aW9uIHNvbmc%3D",
            "Aaho - KD desirock--https://www.youtube.com/watch?v=CauZEiJs3ak&pp=ygUJYWFobyBzb25n",
            "Aam Jahe Munde - Parmish Verma--https://www.youtube.com/watch?v=muds1gFUTN8&pp=ygUOYWFtIGphaGUgbXVuZGU%3D",
            "Bhaag Milkha Bhaag - Siddharth Mahadevan--https://www.youtube.com/watch?v=hc7IJO7fD78&pp=ygUTYmhhYWpnIG1pbGtoYSBiaGFhZw%3D%3D",
            "Bholenath - KAKA WRLD--https://www.youtube.com/watch?v=a4pi2zKbf8Q&pp=ygUJYmhvbGVuYXRo",
            "Damru Ala - Billa Sonipat Aala--https://www.youtube.com/watch?v=bRM0G0-reZw&pp=ygUJYmhvbGVuYXRo",
            "Vampire - Kabira--https://www.youtube.com/watch?v=0TPmmMQfK4A&pp=ygUHdmFtcGlyZQ%3D%3D",    
            "Broken - KD Desi Rock--https://www.youtube.com/watch?v=El2q-329oVE&pp=ygUGYnJva2Vu",
    ]
    }
    songs = mood_music.get(mood, [])
    if songs:
        return random.sample(songs, min(5, len(songs)))
    return []

# Helper functions
def get_mood_emoji(mood):
    emoji_map = {
        "happy": "😊",
        "sad": "😢", 
        "energetic": "⚡",
        "relaxed": "😌",
        "romantic": "💕",
        "Motivated": "💪"
    }
    return emoji_map.get(mood, "🎵")

def get_mood_description(mood):
    descriptions = {
        "happy": "Upbeat and cheerful songs to lift your spirits!",
        "sad": "Melancholic tunes to help you process your emotions.",
        "energetic": "High-energy tracks to get you pumped up!",
        "relaxed": "Calming melodies for a peaceful state of mind.",
        "romantic": "Love songs that speak to the heart.",
        "Motivated": "Inspiring tracks to push you towards your goals!"
    }
    return descriptions.get(mood, "Great music for your current mood!")

def extract_song_info(song_string):
    if "--" in song_string:
        parts = song_string.split("--")
        return parts[0].strip(), parts[1].strip()
    return song_string, ""

# Initialize session state
if 'recommendation_history' not in st.session_state:
    st.session_state.recommendation_history = []
if 'total_recommendations' not in st.session_state:
    st.session_state.total_recommendations = 0

# Main interface
st.markdown('<h1 class="main-header">🎵 Music Recommender System 🎶</h1>', unsafe_allow_html=True)

# Sidebar for additional features
with st.sidebar:
    st.markdown("### 🎛️ Settings")
    num_recommendations = st.slider("Number of recommendations", 1, 10, 5)
    
    st.markdown("### 📊 Statistics")
    st.metric("Total Recommendations", st.session_state.total_recommendations)
    st.metric("Sessions Today", len(st.session_state.recommendation_history))
    
    if st.button("🔄 Clear History"):
        st.session_state.recommendation_history = []
        st.session_state.total_recommendations = 0
        st.rerun()

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="mood-selector">', unsafe_allow_html=True)
    mood = st.selectbox(
        "🎭 Select your mood:",
        ["happy", "sad", "energetic", "relaxed", "romantic", "Motivated"],
        format_func=lambda x: f"{get_mood_emoji(x)} {x.title()}"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Mood description
    st.markdown(f'<div class="mood-card">', unsafe_allow_html=True)
    st.markdown(f"### {get_mood_emoji(mood)} {mood.title()}")
    st.markdown(f"*{get_mood_description(mood)}*")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("### 🎯 Quick Stats")
    st.markdown('<div class="stats-container">', unsafe_allow_html=True)
    st.markdown(f'<div class="stat-card">', unsafe_allow_html=True)
    st.markdown(f"**{len(st.session_state.recommendation_history)}**<br>Sessions", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="stat-card">', unsafe_allow_html=True)
    st.markdown(f"**{datetime.now().strftime('%H:%M')}**<br>Current Time", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Recommendation button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎵 Get Recommendations", use_container_width=True):
        songs = get_music_recommendation(mood)
        if songs:
            # Limit to user-selected number
            songs = songs[:num_recommendations]
            
            # Store in session state
            session_data = {
                'mood': mood,
                'songs': songs,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            st.session_state.recommendation_history.append(session_data)
            st.session_state.total_recommendations += len(songs)
            
            # Display recommendations
            st.markdown("### 🎶 Your Personalized Recommendations")
            
            for i, song in enumerate(songs, 1):
                song_name, song_url = extract_song_info(song)
                
                st.markdown(f'<div class="song-card">', unsafe_allow_html=True)
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"**{i}. {song_name}**")
                    if song_url:
                        st.markdown(f"[🎬 Watch on YouTube]({song_url})")
                
                with col2:
                    if st.button(f"🎵 Play {i}", key=f"play_{i}"):
                        st.markdown(f"🎵 Now playing: **{song_name}**")
                
                st.markdown('</div>', unsafe_allow_html=True)
            
            # Success message
            st.success(f"✨ Found {len(songs)} perfect songs for your {mood} mood!")
            
        else:
            st.error("😔 Sorry, no recommendations available for this mood.")

# Show recent history
if st.session_state.recommendation_history:
    st.markdown("### 📚 Recent Recommendations")
    for i, session in enumerate(reversed(st.session_state.recommendation_history[-3:]), 1):
        with st.expander(f"Session {len(st.session_state.recommendation_history) - i + 1} - {session['mood'].title()} ({session['timestamp']})"):
            for song in session['songs']:
                song_name, _ = extract_song_info(song)
                st.write(f"• {song_name}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p>🎵 Made with ❤️ for music lovers everywhere 🎵</p>
    <p>Discover your perfect soundtrack for every mood!</p>
</div>
""", unsafe_allow_html=True)