from env import settings
from openai import OpenAI
import json

API_KEY = settings.API_KEYS['OPENAI']
client = OpenAI(api_key=API_KEY)


def convert_audio(file_name):
    print('open file')
    audio_file = open(file_name, 'rb')
    print('converting audio')
    transcript = client.audio.transcriptions.create(model='whisper-1', file=audio_file, response_format='text')
    print(transcript)
