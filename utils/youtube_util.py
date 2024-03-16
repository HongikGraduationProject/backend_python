import time

from pytube import YouTube
from dto.shortform import ShortFormDownLoaded
import os


def download_shorts_as_audio(video_url, video_code):
    yt = YouTube(str(video_url))

    video = yt.streams.filter(only_audio=True).first()

    output_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'audios')
    start = time.time()
    out_file = video.download(output_path=output_directory, filename=video_code)
    end = time.time()
    print(f"다운로드 : {end - start:.5f} sec")

    base, ext = os.path.splitext(out_file)
    new_filename = base + '.mp3'

    os.rename(out_file, new_filename)
    return ShortFormDownLoaded(
        video_code=video_code,
        title=yt.title,
        description=yt.description,
        file_name=new_filename,
        keywords=yt.keywords,
        url=video_url)
