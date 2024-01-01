import youtube_util as yt
from openai_utils import whisper_api as whisper
video_url = input("Enter the URL of the video you want to download: \n>> ")
audio_name = yt.download_video_as_audio(video_url)
print(audio_name)
whisper.convert_audio(audio_name)