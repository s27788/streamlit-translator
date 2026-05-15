```python
import streamlit as st
from transformers import pipeline

# Page configuration
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

# Graphics
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
2. Kliknij przycisk "Translate"
3. Poczekaj chwilę na tłumaczenie
4. Odczytaj wynik
""")

# Text area
text = st.text_area(
    "✏️ Wpisz tekst po angielsku",
    placeholder="Example: Hello my friend"
)

# Translate button
translate_button = st.button("🌍 Translate")

# Translation logic
if translate_button and text:

    with st.spinner("⏳ Trwa tłumaczenie..."):

        translator = pipeline(
            "text2text-generation",
            model="google/flan-t5-base"
        )

        prompt = f"Translate English to German: {text}"

        result = translator(
            prompt,
            max_length=100
        )

        translated_text = result[0]["generated_text"]

        st.success("✅ Tłumaczenie zakończone pomyślnie!")

        st.markdown("## 🇩🇪 Tłumaczenie")

        st.code(translated_text, language=None)

# Empty text validation
elif translate_button and not text:

    st.warning("⚠️ Wpisz tekst do tłumaczenia.")

# Sidebar
st.sidebar.title("📚 Menu")

st.sidebar.info("""
Technologie użyte w projekcie:
- Python
- Streamlit
- Hugging Face
- Transformers
- FLAN-T5
""")

st.sidebar.success("Projekt laboratoryjny AI")

# Footer
st.write("---")

st.caption("👩‍💻 Autor: Lidia Kongiel")
st.caption("🎓 Numer indeksu: s27788")
```
