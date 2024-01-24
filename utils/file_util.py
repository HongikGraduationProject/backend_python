from moviepy.editor import *
import os


def convert_video_to_audio(filename):
    if os.path.isfile(filename):
        video = VideoFileClip(filename + ".mp4")
        new_filename = filename + ".mp3"
        video.audio.write_audiofile(new_filename)
        return new_filename
