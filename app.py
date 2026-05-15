import streamlit as st
from deep_translator import GoogleTranslator

# Page configuration
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
    background-color: #0E1117;
}

.main {
    background-color: #0E1117;
}

.block-container {
    max-width: 900px;
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* Main centered wrapper */
.center-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

/* Title */
.main-title {
    text-align: center;
    color: white;
    font-size: 64px;
    font-weight: bold;
    margin-bottom: 15px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #CCCCCC;
    font-size: 24px;
    margin-bottom: 20px;
}

/* Image */
.image-wrapper {
    display: flex;
    justify-content: center;
    margin-bottom: 10px;
}

/* Labels */
.input-label {
    color: white;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
    text-align: center;
}

/* Text area */
textarea {
    font-size: 24px !important;
    text-align: center;
}

/* Button */
div.stButton > button {
    width: 100%;
    height: 65px;
    border-radius: 16px;
    font-size: 24px;
    font-weight: bold;
}

/* Success */
.success-box {
    background-color: #123524;
    padding: 18px;
    border-radius: 14px;
    color: #7CFC98;
    font-size: 22px;
    margin-top: 25px;
    margin-bottom: 25px;
    text-align: center;
}

/* Translation title */
.translation-title {
    text-align: center;
    color: white;
    font-size: 38px;
    font-weight: bold;
    margin-bottom: 15px;
}

/* Translation box */
.translation-box {
    background-color: #1E1E1E;
    padding: 25px;
    border-radius: 18px;
    color: white;
    font-size: 36px;
    text-align: center;
    border: 1px solid #333333;
}

/* Footer */
.footer {
    text-align: center;
    color: gray;
    margin-top: 35px;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# Main centered container
st.markdown('<div class="center-wrapper">', unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-title">
🇬🇧 English ➜ 🇩🇪 German
</div>
""", unsafe_allow_html=True)

# Subtitle
st.markdown("""
<div class="subtitle">
Aplikacja tłumaczy tekst z języka angielskiego na niemiecki przy użyciu AI.
</div>
""", unsafe_allow_html=True)

# Image
st.markdown('<div class="image-wrapper">', unsafe_allow_html=True)

st.image(
    "https://cdn-icons-png.flaticon.com/512/3898/3898082.png",
    width=230
)

st.markdown('</div>', unsafe_allow_html=True)

# Label
st.markdown("""
<div class="input-label">
✍️ Wpisz tekst po angielsku
</div>
""", unsafe_allow_html=True)

# Text input
text = st.text_area(
    "",
    placeholder="Przykład: How are you?",
    height=140
)

# Translate button
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
            <div class="translation-title">
            🇩🇪 Tłumaczenie
            </div>
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
numer indeksu: s27788
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)