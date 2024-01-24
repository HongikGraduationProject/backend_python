import instaloader
import os
import file_util


def download_reels_as_audio(video_url, uuid):
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'audios', uuid)

    L = instaloader.Instaloader(compress_json=False,
                                dirname_pattern=filename,
                                download_pictures=False,
                                download_comments=False,
                                download_video_thumbnails=False,
                                download_geotags=False)
    post = instaloader.Post.from_shortcode(L.context, "C2XAeNXxv36")
    # print(video_url)
    # print(post.date_utc)
    # # print(post.title)
    # print(post.caption)
    # print(post.location)
    # print(filename)
    L.download_pic(url=post.video_url, filename=filename, mtime=post.date_local)
    new_filename = file_util.convert_video_to_audio(filename)


