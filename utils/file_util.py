from moviepy.editor import *
import os


def convert_video_to_audio(filename):
    video_filename = filename + ".mp4"
    if os.path.isfile(video_filename):
        video = VideoFileClip(video_filename)
        new_filename = filename + ".mp3"
        video.audio.write_audiofile(new_filename)
        video.close()
        delete_file(video_filename)
        return new_filename


def delete_file(filename):
    if os.path.isfile(filename):
        os.remove(filename)
