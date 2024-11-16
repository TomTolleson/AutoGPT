import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client with API key
client = OpenAI(api_key=api_key)

# Open and transcribe the audio file
audio_file = open("/Users/tomtolleson/AutoGPT/autogpt_platform/shared/gosubcoda/audio/chunk_1.wav", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)
print(transcription.text)