from env import settings
from openai import OpenAI
from dto.shorts import ShortsTextConverted
import json

API_KEY = settings.API_KEYS['OPENAI']
client = OpenAI(api_key=API_KEY)


def convert_audio(downloaded_shorts):
    print('open file')
    audio_file = open(downloaded_shorts.file_name, 'rb')
    print('converting audio')
    transcript = client.audio.transcriptions.create(model='whisper-1', file=audio_file, response_format='text')
    print(transcript)
    print(type(transcript))
    return ShortsTextConverted(
        id=downloaded_shorts.id,
        title=downloaded_shorts.title,
        description=downloaded_shorts.description,
        file_name=downloaded_shorts.file_name,
        keywords=downloaded_shorts.title,
        url=downloaded_shorts.url,
        transcript=transcript
    )
