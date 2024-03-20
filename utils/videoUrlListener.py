import json
import threading
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
        return

    @staticmethod
    def on_message(channel, method_frame, header_frame, body):
        body_json = json.loads(body.decode('utf-8'))
        print(body_json['url'])
        print(body_json['videoCode'])
        print('Received %s' % body)
        t = threading.Thread(target=publisher.send_summary, args=(body_json['url'], body_json['videoCode']))
        t.start()

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
