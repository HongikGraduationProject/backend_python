from pytube import YouTube
import os


def download_video_as_audio(video_url):
    # url input from user
    yt = YouTube(str(video_url))

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # check for destination to save file
    dest_dir = 'audios'

    # download the file
    out_file = video.download(output_path=dest_dir)
    print('downloading video')
    # save the file
    base, ext = os.path.splitext(out_file)
    new_name = base + '.mp3'

    os.rename(out_file, new_name)

    # result of success
    print(yt.title + " has been successfully downloaded.")

    return new_name
