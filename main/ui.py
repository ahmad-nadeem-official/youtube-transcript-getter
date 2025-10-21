import streamlit as st
from langu import lang, lang_flags
from transcript import getter

# ---------------------------------- PAGE CONFIG ----------------------------------
st.set_page_config(page_title="YouTube Transcript Getter", page_icon="💬", layout="centered")
st.title("YouTube Transcript Getter")
st.sidebar.title("Transcript Settings")

# ---------------------------------- FORM ----------------------------------
with st.sidebar.form("choose_video_parameters", clear_on_submit=False):
    # Input: YouTube link or ID
    video_input = st.text_input(
        "Enter YouTube video link or ID",
        key="video_id",
        placeholder="e.g., d-U9a9PzwIw or https://www.youtube.com/watch?v=d-U9a9PzwIw",
    )

    # Language selection (with flags)
    options = [f"{name} {lang_flags.get(name, '')}" for name in lang.keys()]
    language_display = st.selectbox("Select language", options)

    # Submit button
    submit_button = st.form_submit_button(label="Get Transcript")

# ---------------------------------- ACTION AFTER SUBMIT ----------------------------------
if submit_button:
    try:
        if not video_input:
            st.warning("Please enter a valid YouTube video ID or link.")
        else:
            # Extract video ID safely
            if "v=" in video_input:
                video_id = video_input.split("v=")[1].split("&")[0]
            else:
                video_id = video_input.strip()

            # Extract language name and code
            selected_lang = language_display.split(" ")[0]
            selected_code = lang[selected_lang]

            # Show thumbnail
            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
            st.image(thumbnail_url, caption="YouTube Thumbnail", use_container_width=True)

            # Show details
            st.write(f"**Video ID:** `{video_id}`")
            st.write(f"**Language:** {selected_lang} ({selected_code})")

            # Fetch transcript
            with st.spinner("Fetching transcript..."):
                transcript_text = getter(video_id, selected_code)

            if transcript_text:
                st.subheader("Transcript:")
                st.text_area("Transcript", value=transcript_text, height=400)
            else:
                st.info("Transcript not found for this video.")
    except Exception as e:
        st.error(f"Error: {e}")
