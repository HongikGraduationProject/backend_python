from utils import youtube_util as yt

video_url = input("Enter the URL of the video you want to download: \n>> ")
shorts = yt.download_video_as_audio(video_url)
print(shorts)
# whisper.convert_audio(audio_name)
