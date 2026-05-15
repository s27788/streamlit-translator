import streamlit as st
from deep_translator import GoogleTranslator

# Page config
st.set_page_config(
    page_title="Translator AI",
    page_icon="🌍",
    layout="centered"
)

# CSS
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: Arial, sans-serif;
    background-color: #0E1117;
}

/* Main container */
.block-container {
    max-width: 700px;
    padding-top: 1rem;
    padding-bottom: 1rem;
    margin: auto;
}

/* Title */
.title {
    text-align: center;
    color: white;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #CCCCCC;
    font-size: 18px;
    margin-bottom: 20px;
}

/* Image center */
.image-center {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
}

/* Label */
.label {
    text-align: center;
    color: white;
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
}

/* Text area */
textarea {
    text-align: center;
    font-size: 18px !important;
}

/* Button */
div.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    font-size: 20px;
    font-weight: bold;
}

/* Success */
.success-box {
    background-color: #123524;
    padding: 14px;
    border-radius: 12px;
    color: #7CFC98;
    font-size: 18px;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 20px;
}

/* Translation title */
.translation-title {
    text-align: center;
    color: white;
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 15px;
}

/* Translation box */
.translation-box {
    background-color: #1E1E1E;
    padding: 18px;
    border-radius: 14px;
    color: white;
    font-size: 26px;
    text-align: center;
    border: 1px solid #333333;
}

/* Footer */
.footer {
    text-align: center;
    color: gray;
    margin-top: 30px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="title">
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
st.markdown('<div class="image-center">', unsafe_allow_html=True)

st.image(
    "https://cdn-icons-png.flaticon.com/512/3898/3898082.png",
    width=150
)

st.markdown('</div>', unsafe_allow_html=True)

# Input label
st.markdown("""
<div class="label">
✍️ Wpisz tekst po angielsku
</div>
""", unsafe_allow_html=True)

# Text input
text = st.text_area(
    "",
    placeholder="Przykład: How are you?",
    height=120
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