from env import settings
from openai import OpenAI
from dto.shortform import ShortFormTextConverted
import os

API_KEY = settings.API_KEYS['OPENAI']
client = OpenAI(api_key=API_KEY)


def convert_audio(downloaded_shorts):
    audio_file = open(downloaded_shorts.file_name, 'rb')
    transcript = client.audio.transcriptions.create(model='whisper-1', file=audio_file, response_format='text')
    audio_file.close()

    os.remove(downloaded_shorts.file_name)
    return ShortFormTextConverted(
        video_code=downloaded_shorts.video_code,
        title=downloaded_shorts.title,
        description=downloaded_shorts.description,
        file_name=downloaded_shorts.file_name,
        keywords=downloaded_shorts.title,
        url=downloaded_shorts.url,
        transcript=transcript,
        platform=downloaded_shorts.platform
    )

