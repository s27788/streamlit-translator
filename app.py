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

.block-container {
    padding-top: 2rem;
}

h1 {
    text-align: center;
    color: white;
    font-size: 58px !important;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #CCCCCC;
    font-size: 22px;
    margin-bottom: 25px;
}

.image-container {
    display: flex;
    justify-content: center;
    margin-bottom: 25px;
}

.success-box {
    background-color: #123524;
    padding: 16px;
    border-radius: 12px;
    color: #7CFC98;
    font-size: 20px;
    margin-top: 20px;
    margin-bottom: 20px;
}

.translation-box {
    background-color: #1E1E1E;
    padding: 22px;
    border-radius: 15px;
    color: white;
    font-size: 24px;
    border: 1px solid #333333;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 50px;
    font-size: 15px;
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

# Centered image
st.markdown('<div class="image-container">', unsafe_allow_html=True)

st.image(
    "https://cdn-icons-png.flaticon.com/512/3898/3898082.png",
    width=220
)

st.markdown("</div>", unsafe_allow_html=True)

# Input
text = st.text_area(
    "✍️ Wpisz tekst po angielsku",
    placeholder="Przykład: How are you?",
    height=180
)

# Button
translate_button = st.button(
    "🌍 Tłumacz",
    use_container_width=True
)

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
numer indeksu s27788
</div>
""", unsafe_allow_html=True)