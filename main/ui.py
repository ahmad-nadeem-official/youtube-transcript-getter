# import streamlit as st
# import transcript as tr

# # --- Page setup ---
# # st.set_page_config(page_title="Youtube Transcript getter", page_icon="💬", layout="centered")

# # # --- Initialize session state ---
# # if "chat_history" not in st.session_state:
# #     st.session_state.chat_history = []

# # # --- Title ---
# # st.markdown("<h2 style='text-align:center; color:white;'>💬 AI Chatbot</h2>", unsafe_allow_html=True)

# # # --- Chat display ---
# # for role, text in st.session_state.chat_history:
# #     if role == "user":
# #         st.markdown(
# #             f"""
# #             <div style="
# #                 border: 2px solid #00FF00; 
# #                 border-radius: 8px; 
# #                 padding: 10px; 
# #                 margin: 8px 0; 
# #                 background-color: #0d0d0d;
# #                 color: white;
# #             ">
# #                 <b style="color:#00FF00;">You:</b> {text}
# #             </div>
# #             """,
# #             unsafe_allow_html=True,
# #         )
# #     else:
# #         st.markdown(
# #             f"""
# #             <div style="
# #                 border: 2px solid #00BFFF; 
# #                 border-radius: 8px; 
# #                 padding: 10px; 
# #                 margin: 8px 0; 
# #                 background-color: #0d0d0d;
# #                 color: white;
# #             ">
# #                 <b style="color:#00BFFF;">AI:</b> {text}
# #             </div>
# #             """,
# #             unsafe_allow_html=True,
# #         )

# # # --- User input ---
# # user_input = st.chat_input("Type your message...")

# # # --- Chat logic ---
# # if user_input:
# #     # Add user message to chat
# #     st.session_state.chat_history.append(("user", user_input))

# #     # Basic AI reply (replace with your own logic or LLM call)
# #     ai_response = f"I received: {user_input}"
# #     st.session_state.chat_history.append(("ai", ai_response))

# #     # Rerun to refresh the UI
# #     st.rerun()



import streamlit as st
import sys, os

# Fix import path (important!)
sys.path.append(os.path.dirname(__file__))

# import transcript as tr  # uncomment only if you need it AND it exists

st.set_page_config(page_title="YouTube Transcript Getter", page_icon="💬", layout="centered")

# --- Title ---
st.title("YouTube Transcript Getter")

# --- Sidebar ---
st.sidebar.title("Transcript Settings")

video_id = st.sidebar.text_input("Enter video ID", key="video_id")

language = st.sidebar.selectbox(
    "Select language",
    options=["en", "hi", "es", "fr", "de", "it", "ja", "ko", "ru", "zh"],
    index=0,
    key="lang_select"
)

custom_lang = st.sidebar.text_input("Or enter custom language code", key="custom_lang")

# --- Main page content ---
if video_id:
    st.write(f"Video ID: `{video_id}`")
    st.write(f"Language selected: `{custom_lang or language}`")
else:
    st.info("Enter a YouTube video ID in the sidebar to begin.")
