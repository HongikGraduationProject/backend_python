from pytube import YouTube
import uuid
import os


def download_video_as_audio(video_url):
    # url input from user
    yt = YouTube(str(video_url))


    print('downloading video')
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    print(yt.title)
    print(yt.description)
    print(yt.keywords)

    # download the file
    output_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'audios')
    out_file = video.download(output_path=output_directory, filename=str(uuid.uuid1()))
    base, ext = os.path.splitext(out_file)
    new_name = base + '.mp3'

    os.rename(out_file, new_name)
    print(yt.title + " has been successfully downloaded.")

    return new_name