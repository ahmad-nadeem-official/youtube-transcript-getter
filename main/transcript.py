from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig, GenericProxyConfig
import time

# '''video link'''
# video_id = "d-U9a9PzwIw"

proxy_config = GenericProxyConfig(
    http_url="http://cfmamrji:hijvyqtzb4el@142.111.48.253:7030/",
    https_url="http://cfmamrji:hijvyqtzb4el@142.111.48.253:7030/"
)

def getter(id, lang):
    video = id,
    language = lang
    ytt_api = YouTubeTranscriptApi(proxy_config=proxy_config)
    yttp = ytt_api.fetch(video, languages=[language])
    transcript_text = "\n".join(snippet.text for snippet in yttp.snippets)
    return transcript_text    

if __name__ == "__main__":
    getter("ynBcam9yt-g", "en")
#   print(getter("d-U9a9a9PzwIw", "en"))