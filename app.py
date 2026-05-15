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
    .main {
        background-color: #0E1117;
    }

    h1 {
        text-align: center;
        color: white;
        font-size: 52px !important;
    }

    .subtitle {
        text-align: center;
        color: #CCCCCC;
        font-size: 20px;
        margin-bottom: 30px;
    }

    .success-box {
        background-color: #123524;
        padding: 15px;
        border-radius: 12px;
        color: #7CFC98;
        font-size: 20px;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .translation-box {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 15px;
        color: white;
        font-size: 24px;
        border: 1px solid #333333;
    }

    .footer {
        text-align: center;
        color: gray;
        margin-top: 40px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<h1>🇬🇧 English ➜ 🇩🇪 German</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Aplikacja tłumaczy tekst z języka angielskiego na niemiecki przy użyciu AI.
</div>
""", unsafe_allow_html=True)

# Graphic
st.image(
    "https://cdn-icons-png.flaticon.com/512/3898/3898082.png",
    width=220
)

# Input
text = st.text_area(
    "✍️ Wpisz tekst po angielsku",
    placeholder="Przykład: Hello, how are you?",
    height=180
)

# Button
translate_button = st.button("🌍 Tłumacz", use_container_width=True)

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

            st.markdown("## 🇩🇪 Tłumaczenie")

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
Translator AI • Streamlit + GoogleTranslator
</div>
""", unsafe_allow_html=True)