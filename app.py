import streamlit as st
from deep_translator import GoogleTranslator

# Page config
st.set_page_config(
    page_title="English to German Translator",
    page_icon="🌍",
    layout="centered"
)

# Title
st.markdown(
    """
    # 🇬🇧 English ➜ 🇩🇪 German
    ### AI Translator App
    """
)

st.write(
    "Translate English text into German using AI translation."
)

# Input
text = st.text_area(
    "✏️ Enter English text",
    height=200,
    placeholder="Type your text here..."
)

# Button
if st.button("🌍 Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            translated = GoogleTranslator(
                source="en",
                target="de"
            ).translate(text)

            st.success("✅ Translation completed successfully!")

            st.markdown("## 🇩🇪 Translation")

            st.code(translated)

        except Exception as e:
            st.error(f"Error: {e}")