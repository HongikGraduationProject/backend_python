from dto.shortform import ShortFormDownLoaded
from utils import file_util
import instaloader
import os
import re
from env import settings
from datetime import datetime

import time
SHORTCODE_REGEX = r'(?:https?:\/\/)?(?:www\.)?instagram\.com\/?([a-zA-Z0-9\.\_\-]+)?\/([p]+)?([reel]+)?([tv]+)?([stories]+)?\/([a-zA-Z0-9\-\_\.]+)\/?([0-9]+)?'


def download_reels_as_audio(reels_url, video_code):
    start = time.time()
    L = instaloader.Instaloader(compress_json=False,
                                download_pictures=False,
                                download_comments=False,
                                download_video_thumbnails=False,
                                download_geotags=False,
                                max_connection_attempts=1
                                )
    L.load_session("hongikmu",
                   {"sessionid": settings.INSTAGRAM["SESSION_ID"],
                    "csrftoken": settings.INSTAGRAM["CSRF_TOKEN"]})
    end = time.time()
    print(f"로그인 : {end - start:.5f} sec")

    post = instaloader.Post.from_shortcode(L.context, extract_shortcode(reels_url))

    now = datetime.now()
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'audios', video_code+now.strftime('%Y-%m-%d_%H-%M-%S-%f'))
    start = time.time()
    L.download_pic(url=post.video_url, filename=filename, mtime=post.date_local)
    end = time.time()
    print()
    print(f"다운로드 : {end - start:.5f} sec")

    start = time.time()
    new_filename = file_util.convert_video_to_audio(filename)
    end = time.time()
    print(f"비디오 -> 오디오 : {end - start:.5f} sec")
    return ShortFormDownLoaded(
        video_code=video_code,
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
