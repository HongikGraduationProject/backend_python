from dto.shortform import ShortFormDownLoaded
from utils import file_util
import instaloader
import os
import re

SHORTCODE_REGEX = r'(?:https?:\/\/)?(?:www\.)?instagram\.com\/?([a-zA-Z0-9\.\_\-]+)?\/([p]+)?([reel]+)?([tv]+)?([stories]+)?\/([a-zA-Z0-9\-\_\.]+)\/?([0-9]+)?'


def download_reels_as_audio(reels_url, uuid):
    L = instaloader.Instaloader(compress_json=False,
                                download_pictures=False,
                                download_comments=False,
                                download_video_thumbnails=False,
                                download_geotags=False)
    post = instaloader.Post.from_shortcode(L.context, extract_shortcode(reels_url))
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'audios', uuid)
    L.download_pic(url=post.video_url, filename=filename, mtime=post.date_local)
    new_filename = file_util.convert_video_to_audio(filename)
    return ShortFormDownLoaded(
        uuid=uuid,
        description=post.caption,
        file_name=new_filename,
        url=reels_url
    )


def extract_shortcode(reels_url):
    match = re.search(SHORTCODE_REGEX, reels_url)

    if match:
        shortcode = match.group(6)
        return shortcode

    return None
