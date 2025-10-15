from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import asyncio
from googletrans import Translator

# Replace with an actual YouTube video ID (NOT a playlist ID)
video_id = "fZM3oX4xEyg"

try:
    # Initialize the API object
    ytt_api = YouTubeTranscriptApi()

    # Fetch the transcript (defaults to English if available)
    fetched = ytt_api.fetch(video_id)

    # Combine all snippet texts into one string
    transcript_text = "\n".join(snippet.text for snippet in fetched.snippets)

    # Print or save the transcript
    print(transcript_text)

except TranscriptsDisabled:
    print("Transcripts are disabled for this video.")
except NoTranscriptFound:
    print("No transcript found for this video.")
except Exception as e:
    print(f"Unexpected error: {e}")




translator = Translator()
text = transcript_text

# dt = translator.detect(text)
# tr = translator.translate(text, dest="de")

# print(dt)
# print(tr.text)    