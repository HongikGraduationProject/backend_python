PROMPT = {
    "SHORTS_SUMMARIZE_ENG": """From now on, the json object I give contains information about the video. “title” refers 
    to the title of the video, “description” refers to a description of the video, and “transcript” refers to the 
    transcript of the video. We will perform topic-based summarization on the video. Extract specific topics and 
    themes from a given transcript. Summarize all the important information in the text. Please summarize in the 
    following format in short sentences. Please answer within a maximum of 5 lines. 1. Keywords: 2. Main content: (1) 
    (2) (3) (4) (5). After summarizing, respond in the following format: { "summary" : "Summary contents" }. However, 
    when summarizing, refer to the transcript the most. Also, you don't need to say anything else when responding. 
    You only need to respond with a json object and summarize in korean""",

    "SHORTS_SUMMARIZE_KOR": """
    지금부터 내가 주는 json 객체는 영상에 대한 정보를 담고있어. "title"은 영상의 제목을, "description"은 영상에 대한 설명, "transcript"는 영상의 대본을 의미해.
    영상에 대해 Topic-based summarization 을 할 거야. 
    주어진 텍스트에서 구체적인 토픽과 테마를 추출해. 글에 있는 모든 중요한 정보를 요약해. 
    단문의 형태로 다음의 형식으로 답해. 답은 최대 5줄 이내로 해줘. 1. 키워드: 2. 중심 내용: (1) (2) (3) (4) (5)
    요약한 후 { "summary" : "요약된 내용" } 과 같은 형태로 응답해. 단, 요약할 때 "transcript" 를 가장 많이 참고해. 또한 응답 시 다른 말은 할 필요없어
    json 객체만 응답해.
    """
}

SHORTS_EXAMPLE = {
    "GATORAY" : """
    {"id": "60f62f16-aaf5-11ee-a458-00e04c239933", "title": "음료수 게토레이 탄생 비화", "description": "#Shorts #슈카월드", "file_name": "C:\\Users\\minuk\\PycharmProjects\\studyForgraduationProject\\utils\\..\\audios\\60f62f16-aaf5-11ee-a458-00e04c239933.mp3", "keywords": "음료수 게토레이 탄생 비화", "url": "https://www.youtube.com/shorts/_txGKL47nOg?feature=share", "transcript": "참고로 이 겟토레이에 비화가 있죠. 탄생의 비화. 1965년 플로리다 미국 대학교 미식 축구팀이 있었는데요. 체력이 좋지 않아서 후반만 가면 역전패를 해. 그래서 여기 코치가 열이 받았어요. 전반에 잘 뛰는데 후반만 가면 애들이 뻗어. 그래서 로버트 케이드라는 교수님을 찾아갑니다. 야, 우리 팀이 자꾸 후반만 가면 퍼져요. 뭐가 없을까요? 지금 생각하면 약물 달라는 거잖아. 지금 생각하면. 하여튼 그래서 로버트 케이드 교수님이 나트륨, 칼륨, 포도 다 섞고 이것저것 섞은 다음에 해내요. 그걸 해내요. 됐다. 마셔보면 되겠다. 근데 문제가 발생합니다. 맛을 생각을 안 하고 맛을 과학자들이 그래. 화장실 변기용 세제 맛이 났다 그럽니다. 됐고 마셔, 마셔. 좋은 거야. 자꾸 주니까 자꾸 안 마시죠. 되도 않는 어디 세제를 갖다 마시냐. 그래서 또 아이디어를 냅니다. 과학자 말고 과학자의 사모님이 마셔본 다음에 이건 인간이 마실 수 있는 맛이 아니다. 레몬향을 좀 더 넣자. 그래서 레몬향을 넣어서 아침내 지금의 겟토레이가 됐다 그럽니다. 저 화장실 변기 세제 먹었던 이 형들이 있죠? 이 형들이 마스코트가 악어래요, 악어. 엘리게이터. 그래서 게이터 음료, 악어 음료에서 겟토레이가 돼서 그다음에 대박이 나서 승승장구했다.\n"}
    """,
    "JAPAN_TRAVLE" : """
    
    """
}