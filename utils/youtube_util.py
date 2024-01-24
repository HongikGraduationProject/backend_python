from pytube import YouTube
from dto.shorts import ShortFormDownLoaded
import os


def download_shorts_as_audio(video_url, uuid):
    yt = YouTube(str(video_url))

    video = yt.streams.filter(only_audio=True).first()

    output_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'audios')

    out_file = video.download(output_path=output_directory, filename=uuid)
    base, ext = os.path.splitext(out_file)
    new_name = base + '.mp3'

    os.rename(out_file, new_name)

    return ShortFormDownLoaded(
        uuid=uuid,
        title=yt.title,
        description=yt.description,
        file_name=new_name,
        keywords=yt.keywords,
        url=video_url)
