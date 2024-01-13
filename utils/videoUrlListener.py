import json

from utils.videoSummarySender import Publisher
from env import settings
import pika

publisher = Publisher()


class Consumer:
    def __init__(self):
        self.__url = settings.MQ['HOST']
        self.__port = settings.MQ['PORT']
        self.__cred = pika.PlainCredentials(settings.MQ['USERNAME'], settings.MQ['PASSWORD'])
        self.__queue = settings.MQ['URL_QUEUE_NAME']
        # self.publisher = Publisher()
        return

    @staticmethod
    def on_message(channel, method_frame, header_frame, body):
        url = json.loads(body.decode('utf-8'))['url']
        print(url)
        print('Received %s' % body)
        publisher.send_summary(url)
        return

    def main(self):
        conn = pika.BlockingConnection(pika.ConnectionParameters(host=self.__url,
                                                                 port=self.__port,
                                                                 credentials=self.__cred))
        chan = conn.channel()
        chan.basic_consume(
            queue=self.__queue,
            on_message_callback=Consumer.on_message,
            auto_ack=True
        )
        print('Consumer is starting...')
        chan.start_consuming()
        return
