import streamlit as st
import sys, os
from langu import lang, lang_flags

# # Fix import path (important!)
# sys.path.append(os.path.dirname(__file__))
# import transcript as tr  # uncomment only if you need it AND it exists


################################## --- Streamlit page configuration ---##########################
st.set_page_config(page_title="YouTube Transcript Getter", page_icon="💬", layout="centered")
st.title("YouTube Transcript Getter")
st.sidebar.title("Transcript Settings")

#############################video id input############################

video_id = st.sidebar.text_input("Enter video ID", key="video_id", placeholder="e.g., d-U9a9PzwIw", icon="🎥")
video_id = video_id.split("v=")[1].split("&")[0]

############################language selection############################
# options = [name + " " + lang_flags.get(name, "") for name in lang.keys()]
language = st.sidebar.selectbox("Select language", lang.keys())

###########################################custom language code############################
if language:
    st.sidebar.write(lang_flags[language] + lang[language])

############################get selected language code############################
selected_lang = language.split(" ")[0]
selected_code = lang[selected_lang]

##############################display video id and language code############################
try:
  if video_id:
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
    st.image(thumbnail_url, caption="YouTube Thumbnail", use_container_width=True)
    st.write(f"**Video ID:** {video_id}")
    st.write(f"**Selected Language:** {selected_lang} ({selected_code})")
    
  else:
      st.info("Enter a YouTube video ID in the sidebar to begin.")
except Exception as e:
    st.info(f"invalid id : {e}")