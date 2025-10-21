from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig
import time

# '''video link'''
# video_id = "d-U9a9PzwIw"

def getter(id, lang):
    video = id,
    language = lang
    ytt_api = YouTubeTranscriptApi(
    proxy_config=WebshareProxyConfig(
       proxy_username = "http://cfmamrji:hijvyqtzb4el@proxy.webshare.io:80",
       proxy_password = "http://cfmamrji:hijvyqtzb4el@proxy.webshare.io:80"
    )
)
    yttp = ytt_api.fetch(video, languages=[language])
    transcript_text = "\n".join(snippet.text for snippet in yttp.snippets)
    return transcript_text    

if __name__ == "__main__":
    pass
#   print(getter("d-U9a9a9PzwIw", "en"))