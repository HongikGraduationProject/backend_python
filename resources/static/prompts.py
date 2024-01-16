PROMPT = {
    "SHORTS_SUMMARIZE_ENG": """From now on, the json object I give contains information about the video. “title” refers 
    to the title of the video, “description” refers to a description of the video, and “transcript” refers to the 
    transcript of the video. We will perform topic-based summarization on the video. Extract specific topics and 
    themes from a given transcript. Summarize all the important information in the text. Please summarize in the 
    following format in short sentences. Please answer within a maximum of 5 lines. 1. Keywords: 2. Main content: (1) 
    (2) (3) (4) (5). After summarizing, respond in the following format: { "summary" : "Summary contents" }. However, 
    when summarizing, refer to the transcript the most. Also, you don't need to say anything else when responding. 
    You only need to respond with a json object and summarize in korean""",

    # "SHORTS_SUMMARIZE_KOR": """
    # 지금부터 내가 주는 json 객체는 영상에 대한 정보를 담고있어. "title"은 영상의 제목을, "description"은 영상에 대한 설명, "transcript"는 영상의 대본을 의미해.
    # 영상에 대해 Topic-based summarization 을 할 거야.
    # 주어진 텍스트에서 구체적인 토픽과 테마를 추출해. 글에 있는 모든 중요한 정보를 요약해.
    # 단문의 형태로 다음의 형식으로 답해. 답은 최대 5줄 이내로 해줘. 1. 키워드: 2. 중심 내용: (1) (2) (3) (4) (5)
    # 요약한 후 { "summary" : "요약된 내용", "keywords" : "키워드" } 과 같은 형태로 응답해. 단, 요약할 때 "transcript" 를 가장 많이 참고해. 또한 응답 시 다른 말은 할 필요없어
    # json 객체만 응답해.
    # """
    "SHORTS_SUMMARIZE_KOR": """
    지금부터 내가 주는 json 객체는 유튜브의 숏츠나 인스타의 릴스에 대한 정보를 담고있어. "title"은 영상의 제목을, "description"은 영상에 대한 설명, "transcript"는 영상의 대본을 의미해.
    영상에 대해 Topic-based summarization 을 할 거야. 
    주어진 객체들을 기반으로 영상의 구체적인 토픽과 테마를 추출해. 영상의 모든 중요한 정보를 요약해. 단, 요약할 때 "transcript" 를 가장 많이 참고해.
    내용 요약은 각 문장을 단문의 형태로 (1) (2) (3) (4)...와 같이 번호를 붙여 정리해. 최대 5줄 이내로 요약해줘.
    단 여기서, 구독자에게 "좋아요" 버튼 누르기를 요청하는 등, 영상의 주제와 관련없는 내용은 요약에서 제외해.
    요약한 후 { "summary" : "요약된 내용", "keywords" : ["키워드1","키워드2","키워드3"] } 과 같은 형태로 응답해. 
    """
}

SHORTS_EXAMPLE = {
    "GATORAY": """
    {"id": "60f62f16-aaf5-11ee-a458-00e04c239933", "title": "음료수 게토레이 탄생 비화", "description": "#Shorts #슈카월드", "file_name": "C:\\Users\\minuk\\PycharmProjects\\studyForgraduationProject\\utils\\..\\audios\\60f62f16-aaf5-11ee-a458-00e04c239933.mp3", "keywords": "음료수 게토레이 탄생 비화", "url": "https://www.youtube.com/shorts/_txGKL47nOg?feature=share", "transcript": "참고로 이 겟토레이에 비화가 있죠. 탄생의 비화. 1965년 플로리다 미국 대학교 미식 축구팀이 있었는데요. 체력이 좋지 않아서 후반만 가면 역전패를 해. 그래서 여기 코치가 열이 받았어요. 전반에 잘 뛰는데 후반만 가면 애들이 뻗어. 그래서 로버트 케이드라는 교수님을 찾아갑니다. 야, 우리 팀이 자꾸 후반만 가면 퍼져요. 뭐가 없을까요? 지금 생각하면 약물 달라는 거잖아. 지금 생각하면. 하여튼 그래서 로버트 케이드 교수님이 나트륨, 칼륨, 포도 다 섞고 이것저것 섞은 다음에 해내요. 그걸 해내요. 됐다. 마셔보면 되겠다. 근데 문제가 발생합니다. 맛을 생각을 안 하고 맛을 과학자들이 그래. 화장실 변기용 세제 맛이 났다 그럽니다. 됐고 마셔, 마셔. 좋은 거야. 자꾸 주니까 자꾸 안 마시죠. 되도 않는 어디 세제를 갖다 마시냐. 그래서 또 아이디어를 냅니다. 과학자 말고 과학자의 사모님이 마셔본 다음에 이건 인간이 마실 수 있는 맛이 아니다. 레몬향을 좀 더 넣자. 그래서 레몬향을 넣어서 아침내 지금의 겟토레이가 됐다 그럽니다. 저 화장실 변기 세제 먹었던 이 형들이 있죠? 이 형들이 마스코트가 악어래요, 악어. 엘리게이터. 그래서 게이터 음료, 악어 음료에서 겟토레이가 돼서 그다음에 대박이 나서 승승장구했다.\n"}
    """,
    "JAPAN_TRAVEL": """
    { "id" : "6add5cab-aaed-11ee-9a01-00e04c239933","title" : "모르면 진짜 손해보는 일본 여행 꿀팁 5개! 🙊","description" : "#일본여행 #일본여행꿀팁 #일본여행준비\n\n📢본 채널의 모든 콘텐츠 (초상권,성명권,영상 녹화,영상 일부 캡쳐 등)에 대한 무단 도용과 협의되지 않은 상업적 목적의 사용을 금합니다. \n\n------------------------------\n비지니스 이메일 :  s_the92@naver.com\n인스타그램 @esther__park\n네이버카페 : https://cafe.naver.com/esthertv\n------------------------------\nCOPYRIGHT ⓒ 2023 PARKESTHER ALL RIGHTS RESERVED.","transcript" : "모르면 손에 모는 일본 여행 꿀팁스쇼! 요즘 일본 여행 가시는 분들 많잖아요 근데 이거 모르시는 분들 의외로 많더라고요 먼저 일본 가면 동쿄호텔 많이 가잖아요 계산하시고 면세 받는 곳이 있어요 거기서 여권 보여드리면 10% 세금 돌려받을 수 있으니까 동쿄호텔 갈 때 여권 꼭 챙겨가세요 대신 면세 받은 제품은 일본 안에서 사용하면 안 되기 때문에 일본에 있을 동안 사용하거나 드실 건 빼야 돼요 그리고 카카오톡에 일본 여행 할인 쿠폰 채널을 친구 추가해 놓으시면 추가로 5% 더 할인받을 수 있는 쿠폰 받을 수 있어요 그 외에 많은 분들이 애용하는 드럭스토어 다이마루 백화점, 빅카메라, 에디온 등 할인 쿠폰들도 있으니 잊지 말고 챙겨서 계산할 때 보여주시고 더 저렴하게 구매하세요 또 환절하실 때 주거래 은행에서 가시면 90% 환율 우대되거든요 저는 어플로 미리 신청해놓고 가까운 은행이나 공항에서 수령해요 또 일본어로 된 메뉴판이나 설명 등은 파파고 번역기로 사진 찍어서 클릭만 하면 바로 번역되니까 당황하지 마시고 이렇게 써보세요 길이 잘 모르겠는데 어떻게 가지? 구글맵에 치시면 친절하게 경로 안내 다 해주니까 구글맵도 꼭 깔아주세요 또 여러분이 아는 좋은 꿀팁이 있다면 댓글에 저도 알려주세요 안녕\n')" }
    """
}
