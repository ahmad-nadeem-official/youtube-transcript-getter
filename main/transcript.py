from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig
import time

'''video link'''

video_id = "d-U9a9PzwIw"

'''initial fetch to detect language'''
ytt_api = YouTubeTranscriptApi(
    proxy_config=WebshareProxyConfig(
        proxy_username="cfmamrji",
        proxy_password="hijvyqtzb4el",
    )
)

'''
language choosing logic
'''

_lang = str(input("Enter language code (e.g., 'en' for English, 'hi' for Hindi): "))


yttp = ytt_api.fetch(video_id, languages=[_lang])
transcript_text = "\n".join(snippet.text for snippet in yttp.snippets)
print(len(transcript_text))
print(transcript_text)