import json
import pika
from utils import youtube_util as yt
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
                                                                 credentials=self.__cred))

    def send_summary(self, url):
        video_info = yt.download_video_as_audio(url)
        print(video_info)
        text_converted = whisper.convert_audio(video_info)
        print(json.dumps(asdict(text_converted), ensure_ascii=False))
        summarized_video = chatGPT.summarize_short(text_converted)
        self.channel.basic_publish(
            exchange=MQ['EXCHANGE_NAME'],
            routing_key=MQ['SUMMARY_ROUTING_KEY'],
            body=json.dumps({"url": summarized_video + "dfsddf"})
        )

    def close_connection(self):
        self.connection.close()
