import streamlit as st
import requests

def get_random_quote():
    response = requests.get('https://zenquotes.io/api/random')
    if response.status_code == 200:
        return response.json()[0]
    else:
        return None

st.set_page_config(page_title="Random Quote Generator", page_icon=":sparkles:", layout="wide")

st.markdown("""
    <style>
    body {
        background-color: #F3E5F5;
        color: #4A148C;
    }
    .quote-box {
        background-color: #E1BEE7;
        border-radius: 15px;
        padding: 20px;
        margin: 20px auto;
        max-width: 600px;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #4A148C;
    }
    .footer a {
        color: #6A1B9A;
        text-decoration: none;
        font-weight: bold;
    }
    .footer a:hover {
        color: #4A148C;
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Here's a Quote for You, Cutie 😘")
st.markdown("Welcome! Refresh the page to see a new quote.")

quote = get_random_quote()

if quote:
    st.markdown(f'<div class="quote-box"><blockquote>&ldquo;{quote["q"]}&rdquo;<br> &mdash; {quote["a"]}</blockquote></div>', unsafe_allow_html=True)
else:
    st.error("Failed to fetch a quote. Please try again later.")

st.markdown("""
    <div class="footer">
        Designed by <a href="https://linktr.ee/aryandhone555">Aryan</a> <br>
        <a href="mailto:er.aryandhone@gmail.com">er.aryandhone@gmail.com</a> |
        <a href="https://linkedin.com/in/aryandhone555">LinkedIn</a>
    </div>
    """, unsafe_allow_html=True)
