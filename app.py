import streamlit as st
import requests
from datetime import date

# Set page title and icon
st.set_page_config(page_title="Catholic Daily", page_icon="✝️")

st.title("🙏 Catholic Daily")
today = date.today()
st.write(f"### {today.strftime('%A, %B %d, %Y')}")

# --- 1. GET THE SAINT OF THE DAY ---
def get_saint():
    # Using a public Liturgical Calendar API
    url = f"http://calapi.inadiutorium.cz/api/v1/calendars/general-en/today"
    try:
        response = requests.get(url).json()
        celebrations = response.get('celebrations', [])
        if celebrations:
            return celebrations[0]['title']
        return "Ordinary Time"
    except:
        return "Blessings on this Day"

# --- 2. GET THE BIBLE VERSE (Catholic Translation) ---
def get_bible_verse():
    # 'dra' is the Douay-Rheims translation
    url = "https://bible-api.com/verse_of_the_day?translation=dra"
    try:
        data = requests.get(url).json()
        text = data['verse']['text']
        ref = data['verse']['name']
        return text, ref
    except:
        return "For God so loved the world...", "John 3:16"

# Display the Information
st.divider()
st.subheader("😇 Today's Saint/Feast")
st.info(get_saint())

st.divider()
st.subheader("📖 Daily Catholic Scripture")
verse_text, verse_ref = get_bible_verse()
st.write(f"*{verse_text}*")
st.caption(f"— {verse_ref} (Douay-Rheims Version)")
