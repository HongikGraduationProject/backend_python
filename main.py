# from utils import youtube_util as yt
# from utils.open_ai import chatGPT
# from utils.open_ai import whisper
# from dataclasses import asdict
from utils.videoUrlListener import Consumer
import json


consumer = Consumer()
consumer.main()
print('consumer created')


# video_url = input("Enter the URL of the video you want to download: \n>> ")
# shorts = yt.download_video_as_audio(video_url)
# print(shorts)
# audio_converted = whisper.convert_audio(shorts)
#
# print(json.dumps(asdict(audio_converted), ensure_ascii=False))
# chatGPT.summarize_short(audio_converted)
