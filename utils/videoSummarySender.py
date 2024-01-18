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

    def send_summary(self, url, uuid):
        video_info = yt.download_video_as_audio(url, uuid)

        text_converted = whisper.convert_audio(video_info)

        summarized_video = chatGPT.summarize_short(text_converted)
        print(json.dumps(asdict(summarized_video), ensure_ascii=False))
        self.channel.basic_publish(
            exchange=MQ['EXCHANGE_NAME'],
            routing_key=MQ['SUMMARY_ROUTING_KEY'],
            # body="""{"summary": "1. 동쿄호텔에서 여권으로 10% 세금 돌려받을 수 있음\n
            # 2. 카카오톡에 일본 여행 할인 쿠폰 채널 추가하면 5% 추가 할인 가능\n
            # 3. 드럭스토어 등의 할인 쿠폰을 챙겨서 구매할 때 사용\n
            # 4. 은행에서 환전 시 90% 환율 우대 받을 수 있음\n
            # 5. 구글맵을 이용하여 일본어로된 메뉴판이나 설명 번역 가능",
            # "keywords": ["일본여행", "일본여행꿀팁", "동쿄호텔", "할인쿠폰", "환율우대"]}""")
        body=json.dumps(asdict(summarized_video), ensure_ascii=False))

    def close_connection(self):
        self.connection.close()
