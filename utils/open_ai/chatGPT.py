from openai import OpenAI
from env import settings
from dataclasses import asdict
from resources.static.prompts import PROMPT
import json

API_KEY = settings.API_KEYS['OPENAI']

client = OpenAI(api_key=API_KEY)


def summarize_short(shorts):
    shorts_json = json.dumps(asdict(shorts), ensure_ascii=False)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": shorts_json},
            {"role": "system", "content": PROMPT["SHORTS_SUMMARIZE"]}
        ]
    )
    print(completion)


def summarize_short_tmp():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": """
            {"id": "60f62f16-aaf5-11ee-a458-00e04c239933", "title": "음료수 게토레이 탄생 비화", "description": "#Shorts #슈카월드", "file_name": "C:\\Users\\minuk\\PycharmProjects\\studyForgraduationProject\\utils\\..\\audios\\60f62f16-aaf5-11ee-a458-00e04c239933.mp3", "keywords": "음료수 게토레이 탄생 비화", "url": "https://www.youtube.com/shorts/_txGKL47nOg?feature=share", "transcript": "참고로 이 겟토레이에 비화가 있죠. 탄생의 비화. 1965년 플로리다 미국 대학교 미식 축구팀이 있었는데요. 체력이 좋지 않아서 후반만 가면 역전패를 해. 그래서 여기 코치가 열이 받았어요. 전반에 잘 뛰는데 후반만 가면 애들이 뻗어. 그래서 로버트 케이드라는 교수님을 찾아갑니다. 야, 우리 팀이 자꾸 후반만 가면 퍼져요. 뭐가 없을까요? 지금 생각하면 약물 달라는 거잖아. 지금 생각하면. 하여튼 그래서 로버트 케이드 교수님이 나트륨, 칼륨, 포도 다 섞고 이것저것 섞은 다음에 해내요. 그걸 해내요. 됐다. 마셔보면 되겠다. 근데 문제가 발생합니다. 맛을 생각을 안 하고 맛을 과학자들이 그래. 화장실 변기용 세제 맛이 났다 그럽니다. 됐고 마셔, 마셔. 좋은 거야. 자꾸 주니까 자꾸 안 마시죠. 되도 않는 어디 세제를 갖다 마시냐. 그래서 또 아이디어를 냅니다. 과학자 말고 과학자의 사모님이 마셔본 다음에 이건 인간이 마실 수 있는 맛이 아니다. 레몬향을 좀 더 넣자. 그래서 레몬향을 넣어서 아침내 지금의 겟토레이가 됐다 그럽니다. 저 화장실 변기 세제 먹었던 이 형들이 있죠? 이 형들이 마스코트가 악어래요, 악어. 엘리게이터. 그래서 게이터 음료, 악어 음료에서 겟토레이가 돼서 그다음에 대박이 나서 승승장구했다.\n"}
            """},
            {"role": "system", "content": PROMPT["SHORTS_SUMMARIZE_KOR"]}
        ]
    )
    print(completion)


summarize_short_tmp()
