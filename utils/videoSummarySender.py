import json
import pika
from utils import youtube_util as yt
from utils import instagram_util as insta
from utils.open_ai import chatGPT
from utils.open_ai import whisper
from dataclasses import asdict
from env.settings import MQ


class Publisher:
    def __init__(self):
        self.__url = MQ['HOST']
        self.__port = MQ['PORT']
        self.__cred = pika.PlainCredentials(MQ['USERNAME'], MQ['PASSWORD'])
        self.__queue = MQ['SUMMARY_QUEUE_NAME']
        self.connection = self._establish_connection()
        self.channel = self.connection.channel()
        return

    def _establish_connection(self):
        return pika.BlockingConnection(pika.ConnectionParameters(host=self.__url,
                                                                 port=self.__port,
                                                                 credentials=self.__cred,
                                                                 heartbeat=0))

    def send_summary(self, url, uuid):
        if 'instagram' in url:
            video_info = insta.download_reels_as_audio(url, uuid)
        else:
            video_info = yt.download_shorts_as_audio(url, uuid)

        text_converted = whisper.convert_audio(video_info)

        summarized_video = chatGPT.summarize_short(text_converted)
        # print(json.dumps(asdict(summarized_video), ensure_ascii=False))
        print("uuid = " + uuid + " sent")
        self.channel.basic_publish(
            exchange=MQ['EXCHANGE_NAME'],
            routing_key=MQ['SUMMARY_ROUTING_KEY'],
            body=json.dumps(asdict(summarized_video), ensure_ascii=False))

    def close_connection(self):
        self.connection.close()
