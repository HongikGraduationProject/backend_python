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
        shorts = yt.download_video_as_audio(url)
        print(shorts)
        audio_converted = whisper.convert_audio(shorts)
        print(json.dumps(asdict(audio_converted), ensure_ascii=False))
        chatGPT.summarize_short(audio_converted)
        self.channel.basic_publish(
            exchange=MQ['EXCHANGE_NAME'],
            routing_key=MQ['SUMMARY_ROUTING_KEY'],
            body=json.dumps({"url": url + "dfsddf"})
        )

    def close_connection(self):
        self.connection.close()
