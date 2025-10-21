from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain


from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig
import time

video_id = "d-U9a9PzwIw" # Replace with your video ID
ytt_api = YouTubeTranscriptApi()
# Fetch the transcript in Hindi
vid = ytt_api.fetch(video_id, languages=['hi'])
lang = vid.language_code
print(lang)
time.sleep(10)

ytt_api = YouTubeTranscriptApi(
    proxy_config=WebshareProxyConfig(
        proxy_username="cfmamrji",
        proxy_password="hijvyqtzb4el",
    )
)

# all requests done by ytt_api will now be proxied through Webshare
# Corrected method call: use list_transcripts on the instance
transcripts = ytt_api.list_transcripts(video_id)


# Step 2: Pick the manually created transcript if possible, else auto-generated
# (This automatically detects the language)
if transcripts.find_manually_created_transcript(transcripts._manually_created_transcripts.keys()):
    transcript_obj = transcripts.find_manually_created_transcript(transcripts._manually_created_transcripts.keys())
else:
    transcript_obj = transcripts.find_generated_transcript(transcripts._generated_transcripts.keys())

lang = transcript_obj.language_code
print(f"Detected language: {lang}")


# all requests done by ytt_api will now be proxied through Webshare
yttp = ytt_api.fetch(video_id, languages=[lang])


transcript_text = "\n".join(snippet.text for snippet in yttp.snippets)
# Print or save the transcript
print(len(transcript_text))
print(transcript_text)