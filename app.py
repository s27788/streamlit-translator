import streamlit as st
from deep_translator import GoogleTranslator

# Page config
st.set_page_config(
    page_title="Translator AI",
    page_icon="🌍",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: Arial, sans-serif;
}

.main {
    background-color: #0E1117;
}

.block-container {
    max-width: 850px;
    padding-top: 1rem;
    padding-bottom: 1rem;
}

h1 {
    text-align: center;
    color: white;
    font-size: 52px !important;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #CCCCCC;
    font-size: 20px;
    margin-bottom: 20px;
}

.image-container {
    display: flex;
    justify-content: center;
    margin-bottom: 15px;
}

.success-box {
    background-color: #123524;
    padding: 14px;
    border-radius: 12px;
    color: #7CFC98;
    font-size: 18px;
    margin-top: 18px;
    margin-bottom: 18px;
    text-align: center;
}

.translation-title {
    text-align: center;
    color: white;
    margin-top: 10px;
    margin-bottom: 15px;
}

.translation-box {
    background-color: #1E1E1E;
    padding: 18px;
    border-radius: 15px;
    color: white;
    font-size: 22px;
    border: 1px solid #333333;
    text-align: center;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 30px;
    font-size: 14px;
}

div.stButton > button {
    width: 100%;
    height: 55px;
    font-size: 20px;
    border-radius: 12px;
}

textarea {
    font-size: 18px !important;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<h1>🇬🇧 English ➜ 🇩🇪 German</h1>
""", unsafe_allow_html=True)

# Subtitle
st.markdown("""
<div class="subtitle">
Aplikacja tłumaczy tekst z języka angielskiego na niemiecki przy użyciu AI.
</div>
""", unsafe_allow_html=True)

# Center image
st.markdown('<div class="image-container">', unsafe_allow_html=True)

st.image(
    "https://cdn-icons-png.flaticon.com/512/3898/3898082.png",
    width=170
)

st.markdown('</div>', unsafe_allow_html=True)

# Input
text = st.text_area(
    "✍️ Wpisz tekst po angielsku",
    placeholder="Przykład: How are you?",
    height=140
)

# Button
translate_button = st.button("🌍 Tłumacz")

# Translation
if translate_button:

    if text.strip() == "":
        st.warning("⚠️ Wpisz tekst do tłumaczenia.")
    else:
        try:
            translated = GoogleTranslator(
                source="auto",
                target="de"
            ).translate(text.strip())

            st.markdown("""
            <div class="success-box">
            ✅ Tłumaczenie zakończone pomyślnie!
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <h2 class="translation-title">
            🇩🇪 Tłumaczenie
            </h2>
            """, unsafe_allow_html=True)

            st.markdown(
                f"""
                <div class="translation-box">
                {translated}
                </div>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"Błąd tłumaczenia: {e}")

# Footer
st.markdown("""
<div class="footer">
Translator AI • Streamlit Project <br>
Lidia Kongiel • s27788
</div>
""", unsafe_allow_html=True)