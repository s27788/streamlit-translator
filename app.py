import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="AI Translator",
    page_icon="🌍",
    layout="centered"
)

# Header
st.title("🌍 AI Translator")

st.write(
    "Aplikacja tłumaczy tekst z języka angielskiego na niemiecki przy użyciu modeli AI z Hugging Face."
)

st.markdown(
    """
    <div style="text-align: center; font-size: 80px;">
        🇬🇧 ➜ 🇩🇪
    </div>

    <p style="text-align: center; font-size: 28px; font-weight: bold;">
        English to German AI Translator
    </p>
    """,
    unsafe_allow_html=True
)

# Instruction
st.info("""
📌 Instrukcja:
1. Wpisz tekst po angielsku
2. Poczekaj chwilę na przetworzenie
3. Odczytaj tłumaczenie po niemiecku
""")

# Text input
text = st.text_area(
    "✏️ Wpisz tekst po angielsku",
    placeholder="Example: Hello my friend"
)

# Translation
if text:

    with st.spinner("⏳ Trwa tłumaczenie..."):

        translator = pipeline(
            "translation_en_to_de",
            model="Helsinki-NLP/opus-mt-en-de"
        )

        result = translator(text)

        translated_text = result[0]["translation_text"]

        st.success("✅ Tłumaczenie zakończone pomyślnie!")

        st.markdown("## 🇩🇪 Tłumaczenie")

        st.code(translated_text, language=None)

# Sidebar
st.sidebar.title("📚 Menu")

st.sidebar.info("""
Aplikacja wykorzystuje:
- Streamlit
- Hugging Face
- Transformers
- MarianMT Model
""")

st.sidebar.success("Projekt laboratoryjny - Python + AI")

# Footer
st.write("---")

st.caption("🎓 Numer indeksu: s27788")