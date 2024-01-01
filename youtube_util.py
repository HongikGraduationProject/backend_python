from pytube import YouTube
import os


def downloadVideoAsAudio():
    # url input from user
    yt = YouTube(str(input("Enter the URL of the video you want to download: \n>> ")))

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # check for destination to save file
    print("Enter the destination (leave blank for current directory)")
    dest_dir = str(input(">> ")) or '.'

    # download the file
    out_file = video.download(output_path=dest_dir)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_name = base + '.mp3'

    os.rename(out_file, new_name)

    # result of success
    print(yt.title + " has been successfully downloaded.")
