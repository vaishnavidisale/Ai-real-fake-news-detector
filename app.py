import streamlit as st
from groq import Groq
import feedparser
import urllib.parse
import re

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="🌈 AI Fake News Detector",
    page_icon="📰",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.big-title {
    font-size:40px !important;
    font-weight:700;
    color:#ff4b4b;
    text-align:center;
}
.result-box {
    padding:20px;
    border-radius:15px;
    margin-top:20px;
}
.real {
    background-color:#d4edda;
}
.fake {
    background-color:#f8d7da;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🌈 AI Fake News Detector</p>', unsafe_allow_html=True)
st.write("### 🧠 Detect whether news is REAL or FAKE using AI")

# ---------------- USER INPUT ----------------
user_input = st.text_area("✍ Enter News Text Here", height=200)

# ---------------- GOOGLE NEWS FUNCTION ----------------
def get_google_news(query):
    encoded_query = urllib.parse.quote(query)
    rss_url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(rss_url)
    return feed.entries[:5]

# ---------------- AI ANALYSIS ----------------
if st.button("🚀 Analyze News"):

    if not user_input.strip():
        st.warning("⚠ Please enter some news text.")
    else:
        with st.spinner("Analyzing with AI..."):
            try:
                client = Groq(api_key="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")

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "system",
                            "content": """You are a professional fact-checker.
Return output in this format:

Verdict: REAL or FAKE
Confidence: percentage
Explanation: detailed reason
Keywords: important keywords separated by comma
"""
                        },
                        {"role": "user", "content": user_input}
                    ]
                )

                result = response.choices[0].message.content

                # ---------------- DISPLAY RESULT ----------------
                if "REAL" in result.upper():
                    st.markdown(f'<div class="result-box real">{result}</div>', unsafe_allow_html=True)
                    st.success("🟢 News appears REAL")
                    st.progress(85)
                else:
                    st.markdown(f'<div class="result-box fake">{result}</div>', unsafe_allow_html=True)
                    st.error("🔴 News appears FAKE")
                    st.progress(45)

                # ---------------- EXTRACT KEYWORDS ----------------
                keyword_match = re.search(r"Keywords:(.*)", result)
                if keyword_match:
                    keywords = keyword_match.group(1).strip()
                    articles = get_google_news(keywords)

                    st.write("## 📰 Related News Articles")

                    if articles:
                        for article in articles:
                            st.markdown(f"""
                            ### 🔗 {article.title}
                            [Read Full Article]({article.link})
                            ---
                            """)
                    else:
                        st.info("No related articles found.")

            except Exception as e:
                st.error(f"Error: {e}")
