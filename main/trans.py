from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from deep_translator import GoogleTranslator






def chunk_text(text, max_length=4000):
    chunks = []
    current = ""
    for sentence in text.split('. '):
        if len(current) + len(sentence) < max_length:
            current += sentence + ". "
        else:
            chunks.append(current.strip())
            current = sentence + ". "
    if current:
        chunks.append(current.strip())
    return chunks

text = transcript_text
chunks = chunk_text(text)

translator = GoogleTranslator(source='auto', target=language)
translated_chunks = [translator.translate(chunk) for chunk in chunks]
full_translation = " ".join(translated_chunks)

print(full_translation)













# https://www.youtube.com/watch?v=dm470ObSMB4
# Replace with an actual YouTube video ID (NOT a playlist ID)
video_id = "dm470ObSMB4"

try:
    # Initialize the API object
    ytt_api = YouTubeTranscriptApi()

    # Fetch the transcript (defaults to English if available)
    fetched = ytt_api.fetch(video_id)

    # Combine all snippet texts into one string
    transcript_text = "\n".join(snippet.text for snippet in fetched.snippets)

    # Print or save the transcript
    print(len(transcript_text))
    print(transcript_text)

except TranscriptsDisabled:
    print("Transcripts are disabled for this video.")
except NoTranscriptFound:
    print("No transcript found for this video.")
except Exception as e:
    print(f"Unexpected error: {e}")
