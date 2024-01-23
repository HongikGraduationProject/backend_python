import instaloader
import os

output_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'audios', 'fff')

L = instaloader.Instaloader(compress_json=False,
                            dirname_pattern=output_directory,
                            download_pictures=False,
                            download_comments=False,
                            download_video_thumbnails=False,
                            download_geotags=False)
print(L.dirname_pattern)
post = instaloader.Post.from_shortcode(L.context, "C2XAeNXxv36")
video_url = post.video_url
print(video_url)
print(post.date_utc)
print(post.caption)
print(post.location)

# output_directory = 'your_output_directory'
# filename = L.download_pic(filename='filename', url=video_url, mtime=post.date_utc)
L.download_pic(url=video_url, filename=output_directory, mtime=post.date_local)
# L.download_pic()
# metadata_filename = os.path.join(output_directory, 'metadata_json')
# L.save_metadata_json(structure=post, filename=metadata_filename)
# https://www.instagram.com/reel/CyW1-izS_DX/?utm_source=ig_web_copy_link
# https://www.instagram.com/reel/C2XAeNXxv36/?utm_source=ig_web_copy_link
