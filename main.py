from utils import youtube_util as yt
from utils.open_ai import whisper
video_url = input("Enter the URL of the video you want to download: \n>> ")
shorts = yt.download_video_as_audio(video_url)
print(shorts)
audio_converted = whisper.convert_audio(shorts)
print(audio_converted)
